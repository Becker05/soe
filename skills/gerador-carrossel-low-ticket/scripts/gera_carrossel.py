#!/usr/bin/env python3
"""
Gerador de carrossel de feed (1080x1350) — Método das Vendas Reais.
Uso: python3 gera_carrossel.py carrossel.json pasta_base/

Saída no PADRÃO N8N: dentro de pasta_base/, cria UMA subpasta por post
    post-AAAA-MM-DD-<slug>/
        img-01.jpg
        img-02.jpg
        ...            (JPG, numerados na ordem dos slides do Instagram)
        legenda.txt    (só o texto da legenda; criado se o JSON trouxer "legenda")
O N8N detecta a pasta nova, pega as imagens ordenadas + a legenda, monta a
prévia, manda aprovar no WhatsApp e publica.

JSON de entrada:
{
  "slug": "merito-ou-sorte",
  "pasta": "post-2026-07-06-merito-ou-sorte",   // opcional; se ausente, gerado como post-<hoje>-<slug>
  "legenda": "Foi mérito da campanha ou sorte?\n\n...corpo...\n\n#ga4 #ecommerce #atribuicao",  // opcional
  "slides": [
    {"tipo": "capa",     "kicker": "DONO DE E-COMMERCE", "titulo": "Foi mérito da campanha... *ou só sorte?*", "foto": false},
    {"tipo": "gancho2",  "titulo": "Você aumenta o orçamento e as vendas sobem.", "sub": "Mas você sabe *o que* gerou cada venda?"},
    {"tipo": "ponto",    "numero": "01", "titulo": "Somar leituras diferentes cria uma contradição", "corpo": "Reconcilie as fontes antes de transformar o número em decisão."},
    {"tipo": "vs",       "titulo": "Qual leitura sustenta a decisão?", "esq_label": "LEITURA ISOLADA", "esq_valor": "sem contexto", "dir_label": "LEITURA RECONCILIADA", "dir_valor": "decisão segura"},
    {"tipo": "cta",      "kicker": "CARTILHA DAS MÉTRICAS REAIS", "titulo": "Veja *de onde cada venda veio*", "sub": "Reconcilie as fontes antes de decidir.", "cta": "LINK NA BIO"}
  ]
}

Tipos de slide: capa, gancho2, ponto, lista, vs, quote, prova, cta
Markup nos textos: *texto* = destaque em verde | ~texto~ = destaque em vermelho (leitura no escuro/contradição; nunca uma plataforma)
"foto": true na capa => reserva zona inferior direita p/ foto (indicador visual no rascunho)
"""
import datetime
import json
import math
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ---------------------------------------------------------------- identidade
W, H = 1080, 1350
BG_TOP = (11, 18, 32)        # #0B1220 azul-noite
BG_BOTTOM = (6, 10, 20)      # gradiente sutil
VERDE = (34, 229, 143)       # #22E58F acento primário (venda real)
VERMELHO = (255, 90, 95)     # #FF5A5F leitura sem estrutura / contradição
BRANCO = (245, 247, 250)     # #F5F7FA texto
CINZA = (139, 150, 168)      # #8B96A8 apoio
CINZA_ESCURO = (30, 40, 58)  # linhas / cards
MARCA = "@souarturbecker"

FONTS_DIR = Path(__file__).parent.parent / "assets" / "fonts"


def F(fam, peso, tam):
    return ImageFont.truetype(str(FONTS_DIR / f"{fam}-{peso}.ttf"), tam)


# ---------------------------------------------------------------- base
def fundo():
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOTTOM))
        d.line([(0, y), (W, y)], fill=c)
    # glow verde sutil no canto superior direito
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    dg = ImageDraw.Draw(glow)
    dg.ellipse([W - 500, -350, W + 350, 400], fill=(10, 55, 38))
    glow = glow.filter(ImageFilter.GaussianBlur(180))
    img = Image.blend(img, Image.composite(glow, Image.new("RGB", (W, H), (0, 0, 0)), Image.new("L", (W, H), 255)), 0.0)
    base = img.copy()
    img = Image.blend(base, glow, 0.35)
    # grid de pontos discreto (textura "dados")
    d = ImageDraw.Draw(img)
    for gy in range(90, H, 84):
        for gx in range(90, W, 84):
            d.ellipse([gx, gy, gx + 3, gy + 3], fill=(28, 38, 56))
    return img


def rodape(d, idx, total, e_cta=False):
    y = H - 88
    d.text((90, y), MARCA, font=F("inter", 600, 30), fill=CINZA)
    if not e_cta and idx < total:
        seta = "deslize  →"
        f = F("inter", 700, 30)
        w = d.textlength(seta, font=f)
        d.text((W - 90 - w, y), seta, font=f, fill=VERDE)
    # progresso
    n_dots = total
    dot_w, gap = 14, 10
    total_w = n_dots * dot_w + (n_dots - 1) * gap
    x0 = (W - total_w) // 2
    for i in range(n_dots):
        cor = VERDE if i == idx - 1 else CINZA_ESCURO
        d.ellipse([x0 + i * (dot_w + gap), y + 8, x0 + i * (dot_w + gap) + dot_w, y + 8 + dot_w], fill=cor)


# ---------------------------------------------------------------- texto rico
def _tokeniza(texto):
    """Divide em (palavra, cor) respeitando *verde* e ~vermelho~."""
    tokens, cor, buf = [], None, ""
    modo = "normal"
    for ch in texto:
        if ch == "*":
            if buf:
                tokens.append((buf, modo)); buf = ""
            modo = "verde" if modo != "verde" else "normal"
        elif ch == "~":
            if buf:
                tokens.append((buf, modo)); buf = ""
            modo = "vermelho" if modo != "vermelho" else "normal"
        else:
            buf += ch
    if buf:
        tokens.append((buf, modo))
    # explode em palavras mantendo modo
    palavras = []
    for txt, m in tokens:
        for i, p in enumerate(txt.split(" ")):
            if p == "":
                continue
            palavras.append((p, m))
    return palavras


CORES = {"normal": BRANCO, "verde": VERDE, "vermelho": VERMELHO}


def texto_rico(d, texto, x, y, font, max_w, line_h=None, cor_base=BRANCO, align="left"):
    """Desenha texto com wrap + destaques. Retorna y final."""
    palavras = _tokeniza(texto)
    lh = line_h or int(font.size * 1.22)
    espaco = d.textlength(" ", font=font)
    linhas, atual, w_atual = [], [], 0
    for p, m in palavras:
        wp = d.textlength(p, font=font)
        if atual and w_atual + espaco + wp > max_w:
            linhas.append(atual)
            atual, w_atual = [(p, m)], wp
        else:
            w_atual += (espaco if atual else 0) + wp
            atual.append((p, m))
    if atual:
        linhas.append(atual)
    for linha in linhas:
        lw = sum(d.textlength(p, font=font) for p, _ in linha) + espaco * (len(linha) - 1)
        cx = x if align == "left" else (x + (max_w - lw) / 2 if align == "center" else x + max_w - lw)
        for p, m in linha:
            cor = CORES[m] if m != "normal" else cor_base
            d.text((cx, y), p, font=font, fill=cor)
            cx += d.textlength(p, font=font) + espaco
        y += lh
    return y


def _ajusta_fonte(d, texto, fam, peso, tam_ini, max_w, max_linhas):
    """Reduz o tamanho até o texto caber em max_linhas."""
    tam = tam_ini
    while tam > 40:
        f = F(fam, peso, tam)
        palavras = [p for p, _ in _tokeniza(texto)]
        espaco = d.textlength(" ", font=f)
        linhas, w = 1, 0
        for p in palavras:
            wp = d.textlength(p, font=f)
            if w and w + espaco + wp > max_w:
                linhas += 1
                w = wp
            else:
                w += (espaco if w else 0) + wp
        if linhas <= max_linhas:
            return f
        tam -= 6
    return F(fam, peso, tam)


def kicker(d, txt, x, y):
    f = F("inter", 700, 34)
    d.rectangle([x, y + 6, x + 8, y + 40], fill=VERDE)
    d.text((x + 26, y), txt.upper(), font=f, fill=VERDE)
    return y + 64


def zona_foto(img, d):
    """Marca a zona reservada pra foto (capa com foto=true)."""
    x0, y0 = W - 560, H - 720
    d.rounded_rectangle([x0, y0, W - 60, H - 130], radius=28, outline=CINZA_ESCURO, width=4)
    f = F("inter", 600, 32)
    msg = "ZONA DA SUA FOTO"
    msgw = d.textlength(msg, font=f)
    d.text((x0 + (500 - msgw) / 2, y0 + 280), msg, font=f, fill=CINZA)
    f2 = F("inter", 400, 26)
    msg2 = "(recorte PNG sem fundo)"
    d.text((x0 + (500 - d.textlength(msg2, font=f2)) / 2, y0 + 330), msg2, font=f2, fill=CINZA)


# ---------------------------------------------------------------- slides
def slide_capa(s, idx, total):
    img = fundo(); d = ImageDraw.Draw(img)
    y = 150
    if s.get("kicker"):
        y = kicker(d, s["kicker"], 90, y) + 26
    tem_foto = s.get("foto")
    max_w = W - 180 if not tem_foto else W - 180
    f = _ajusta_fonte(d, s["titulo"], "sora", 800, 108, max_w, 5 if not tem_foto else 4)
    y = texto_rico(d, s["titulo"], 90, y, f, max_w, line_h=int(f.size * 1.14))
    if s.get("sub"):
        y += 30
        texto_rico(d, s["sub"], 90, y, F("inter", 400, 44), max_w, cor_base=CINZA)
    if tem_foto:
        zona_foto(img, d)
    rodape(d, idx, total)
    return img


def slide_gancho2(s, idx, total):
    img = fundo(); d = ImageDraw.Draw(img)
    f = _ajusta_fonte(d, s["titulo"], "sora", 700, 88, W - 180, 4)
    alt_titulo = f.size * 1.16 * 3
    y = 320
    y = texto_rico(d, s["titulo"], 90, y, f, W - 180, line_h=int(f.size * 1.16))
    if s.get("sub"):
        y += 44
        d.rectangle([90, y, 240, y + 6], fill=VERDE)
        y += 44
        texto_rico(d, s["sub"], 90, y, F("sora", 600, 56), W - 180, cor_base=BRANCO)
    rodape(d, idx, total)
    return img


def slide_ponto(s, idx, total):
    img = fundo(); d = ImageDraw.Draw(img)
    y = 150
    if s.get("numero"):
        f_num = F("sora", 800, 150)
        d.text((92, y + 2), s["numero"], font=f_num, fill=(18, 60, 44))  # sombra
        d.text((86, y - 4), s["numero"], font=f_num, fill=VERDE)
        y += 210
    f = _ajusta_fonte(d, s["titulo"], "sora", 700, 76, W - 180, 3)
    y = texto_rico(d, s["titulo"], 90, y, f, W - 180, line_h=int(f.size * 1.18))
    if s.get("corpo"):
        y += 40
        texto_rico(d, s["corpo"], 90, y, F("inter", 400, 46), W - 200, line_h=64, cor_base=CINZA)
    rodape(d, idx, total)
    return img


def slide_lista(s, idx, total):
    img = fundo(); d = ImageDraw.Draw(img)
    y = 140
    if s.get("titulo"):
        f = _ajusta_fonte(d, s["titulo"], "sora", 700, 72, W - 180, 3)
        y = texto_rico(d, s["titulo"], 90, y, f, W - 180, line_h=int(f.size * 1.16)) + 50
    for item in s.get("itens", []):
        # check verde
        cy = y + 14
        d.ellipse([90, cy, 90 + 44, cy + 44], outline=VERDE, width=5)
        d.line([102, cy + 22, 110, cy + 32], fill=VERDE, width=6)
        d.line([110, cy + 32, 124, cy + 12], fill=VERDE, width=6)
        y = texto_rico(d, item, 164, y, F("inter", 600, 44), W - 260, line_h=60)
        y += 34
    rodape(d, idx, total)
    return img


def slide_vs(s, idx, total):
    img = fundo(); d = ImageDraw.Draw(img)
    y = 150
    if s.get("titulo"):
        f = _ajusta_fonte(d, s["titulo"], "sora", 700, 72, W - 180, 2)
        y = texto_rico(d, s["titulo"], 90, y, f, W - 180, line_h=int(f.size * 1.16)) + 60
    ch = 420
    cw = (W - 180 - 40) // 2
    # card esquerdo (leitura sem estrutura/vermelho)
    x1 = 90
    d.rounded_rectangle([x1, y, x1 + cw, y + ch], radius=24, fill=(40, 20, 26), outline=VERMELHO, width=4)
    f_lab = F("inter", 700, 32)
    d.text((x1 + (cw - d.textlength(s["esq_label"], font=f_lab)) / 2, y + 60), s["esq_label"], font=f_lab, fill=VERMELHO)
    f_val = F("sora", 800, 84)
    vv = s["esq_valor"]
    fv = f_val if d.textlength(vv, font=f_val) < cw - 60 else F("sora", 800, 60)
    d.text((x1 + (cw - d.textlength(vv, font=fv)) / 2, y + 150), vv, font=fv, fill=BRANCO)
    if s.get("esq_sub"):
        f_s = F("inter", 400, 30)
        d.text((x1 + (cw - d.textlength(s["esq_sub"], font=f_s)) / 2, y + ch - 90), s["esq_sub"], font=f_s, fill=CINZA)
    # card direito (leitura reconciliada/verde)
    x2 = x1 + cw + 40
    d.rounded_rectangle([x2, y, x2 + cw, y + ch], radius=24, fill=(12, 44, 32), outline=VERDE, width=4)
    d.text((x2 + (cw - d.textlength(s["dir_label"], font=f_lab)) / 2, y + 60), s["dir_label"], font=f_lab, fill=VERDE)
    vv2 = s["dir_valor"]
    fv2 = f_val if d.textlength(vv2, font=f_val) < cw - 60 else F("sora", 800, 60)
    d.text((x2 + (cw - d.textlength(vv2, font=fv2)) / 2, y + 150), vv2, font=fv2, fill=BRANCO)
    if s.get("dir_sub"):
        f_s = F("inter", 400, 30)
        d.text((x2 + (cw - d.textlength(s["dir_sub"], font=f_s)) / 2, y + ch - 90), s["dir_sub"], font=f_s, fill=CINZA)
    y += ch + 60
    if s.get("corpo"):
        texto_rico(d, s["corpo"], 90, y, F("inter", 400, 44), W - 200, line_h=62, cor_base=CINZA)
    rodape(d, idx, total)
    return img


def slide_quote(s, idx, total):
    img = fundo(); d = ImageDraw.Draw(img)
    d.text((80, 130), "\u201c", font=F("sora", 800, 260), fill=(20, 70, 50))
    f = _ajusta_fonte(d, s["titulo"], "sora", 600, 78, W - 220, 5)
    y = texto_rico(d, s["titulo"], 110, 360, f, W - 220, line_h=int(f.size * 1.24))
    if s.get("autor"):
        y += 50
        d.rectangle([110, y + 8, 190, y + 14], fill=VERDE)
        d.text((214, y - 8), s["autor"], font=F("inter", 600, 38), fill=CINZA)
    rodape(d, idx, total)
    return img


def slide_prova(s, idx, total):
    """Barra comparativa simples (ex.: leitura isolada x leitura reconciliada)."""
    img = fundo(); d = ImageDraw.Draw(img)
    y = 150
    if s.get("titulo"):
        f = _ajusta_fonte(d, s["titulo"], "sora", 700, 70, W - 180, 3)
        y = texto_rico(d, s["titulo"], 90, y, f, W - 180, line_h=int(f.size * 1.16)) + 70
    for barra in s.get("barras", []):
        pct = max(4, min(100, int(barra.get("pct", 50))))
        cor = VERMELHO if barra.get("cor") == "vermelho" else VERDE
        d.text((90, y), barra["label"].upper(), font=F("inter", 700, 32), fill=CINZA)
        y += 52
        bw = int((W - 180) * pct / 100)
        d.rounded_rectangle([90, y, W - 90, y + 64], radius=14, fill=CINZA_ESCURO)
        d.rounded_rectangle([90, y, 90 + max(bw, 70), y + 64], radius=14, fill=cor)
        vtxt = barra.get("valor", f"{pct}%")
        f_v = F("sora", 800, 40)
        d.text((104, y + 8), vtxt, font=f_v, fill=(8, 12, 20))
        y += 120
    if s.get("corpo"):
        y += 10
        texto_rico(d, s["corpo"], 90, y, F("inter", 400, 44), W - 200, line_h=62, cor_base=CINZA)
    rodape(d, idx, total)
    return img


def slide_cta(s, idx, total):
    img = fundo(); d = ImageDraw.Draw(img)
    # moldura verde no slide de CTA
    d.rounded_rectangle([40, 40, W - 40, H - 40], radius=36, outline=VERDE, width=5)
    y = 260
    if s.get("kicker"):
        f_k = F("inter", 700, 34)
        kw = d.textlength(s["kicker"].upper(), font=f_k)
        d.text(((W - kw) / 2, y), s["kicker"].upper(), font=f_k, fill=VERDE)
        y += 80
    f = _ajusta_fonte(d, s["titulo"], "sora", 800, 96, W - 240, 4)
    y = texto_rico(d, s["titulo"], 120, y, f, W - 240, line_h=int(f.size * 1.16), align="center")
    if s.get("sub"):
        y += 40
        y = texto_rico(d, s["sub"], 120, y, F("inter", 400, 44), W - 240, line_h=62, cor_base=CINZA, align="center")
    # botão
    cta = s.get("cta", "LINK NA BIO")
    f_b = F("sora", 800, 52)
    bw = d.textlength(cta, font=f_b) + 140
    bx = (W - bw) / 2
    by = H - 360
    d.rounded_rectangle([bx, by, bx + bw, by + 120], radius=60, fill=VERDE)
    d.text((bx + 70, by + 30), cta, font=f_b, fill=(8, 12, 20))
    rodape(d, idx, total, e_cta=True)
    return img


RENDER = {
    "capa": slide_capa, "gancho2": slide_gancho2, "ponto": slide_ponto,
    "lista": slide_lista, "vs": slide_vs, "quote": slide_quote,
    "prova": slide_prova, "cta": slide_cta,
}


def _slugifica(txt):
    txt = re.sub(r"[^a-z0-9]+", "-", txt.lower().strip())
    return re.sub(r"-+", "-", txt).strip("-") or "carrossel"


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    dados = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    base = Path(sys.argv[2]); base.mkdir(parents=True, exist_ok=True)

    slides = dados["slides"]
    total = len(slides)
    slug = _slugifica(dados.get("slug", "carrossel"))

    # nome da pasta do post (padrão N8N): uma pasta NOVA por post
    pasta_nome = dados.get("pasta") or f"post-{datetime.date.today():%Y-%m-%d}-{slug}"
    pasta_nome = _slugifica(pasta_nome) if not pasta_nome.startswith("post-") else pasta_nome
    out = base / pasta_nome
    # não reaproveitar pasta antiga: se já existir, sufixa -2, -3...
    if out.exists():
        n = 2
        while (base / f"{pasta_nome}-{n}").exists():
            n += 1
        out = base / f"{pasta_nome}-{n}"
    out.mkdir(parents=True)

    # renderiza cada slide -> img-NN.jpg (a ORDEM numérica = ordem no Instagram)
    for i, s in enumerate(slides, 1):
        tipo = s.get("tipo")
        if tipo not in RENDER:
            print(f"[ERRO] slide {i}: tipo desconhecido '{tipo}'"); sys.exit(2)
        img = RENDER[tipo](s, i, total)
        # PIL renderiza em RGB sobre #0B1220; achata p/ JPG sem transparência
        img = img.convert("RGB")
        nome = out / f"img-{i:02d}.jpg"
        img.save(nome, "JPEG", quality=92, optimize=True, progressive=True)
        print(f"ok  {nome}")

    # legenda.txt (mesmo nome exato, dentro da mesma pasta) — só se houver legenda
    legenda = dados.get("legenda")
    if legenda:
        (out / "legenda.txt").write_text(legenda.strip() + "\n", encoding="utf-8")
        print(f"ok  {out / 'legenda.txt'}")
    else:
        print("[aviso] sem campo 'legenda' no JSON — legenda.txt NÃO criado")

    print(f"\n{total} slides + legenda em: {out}/  (padrão N8N: img-01.jpg... + legenda.txt)")


if __name__ == "__main__":
    main()
