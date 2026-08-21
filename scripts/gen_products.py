#!/usr/bin/env python3
"""Gera as páginas de produto individuais a partir dos dados abaixo.
Reexecutar este script sempre que a copy de produto mudar."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "produtos")
os.makedirs(OUT_DIR, exist_ok=True)

WA_NUMBER = "5562996061223"

CHAMPIONS = [
    dict(
        slug="balsa-bomba-bloc",
        title="Balsa para Bomba Bloc.",
        img="produto-balsa-bloc.jpg",
        gancho="Plataforma flutuante robusta para captação direta em rios e represas, com fácil acesso para manutenção da bomba.",
        bullets=[
            "Plataforma de manutenção e montagem",
            "Suporte para PEAD",
            "Telhado de proteção da bomba",
            "Olhal de ancoragem e içamento",
            "Ajuste de altura da bomba",
            "Ajuste de equilíbrio da balsa",
        ],
        wa="Olá! Vim pelo site e quero um orçamento para a Balsa para Bomba Bloc.",
    ),
    dict(
        slug="balsa-bomba-mancalizada",
        title="Balsa para Bomba Mancalizada",
        img="produto-balsa-mancalizada.jpg",
        gancho="Mesma robustez da linha Bloc, projetada para bombas mancalizadas de maior porte.",
        bullets=[
            "Plataforma de manutenção e montagem",
            "Suporte para PEAD",
            "Telhado de proteção da bomba",
            "Olhal de ancoragem e içamento",
            "Ajuste de equilíbrio da balsa",
        ],
        wa="Olá! Vim pelo site e quero um orçamento para a Balsa para Bomba Mancalizada.",
    ),
    dict(
        slug="flutuante-pead",
        title="Flutuante para PEAD",
        img="produto-flutuante-pead.jpg",
        gancho="Sustentação e estabilidade para linhas de PEAD em operação na água.",
        bullets=["Ajuste de equilíbrio do flutuante"],
        wa="Olá! Vim pelo site e quero um orçamento para o Flutuante para PEAD.",
    ),
    dict(
        slug="flutuante-valvula-pe",
        title="Flutuante para Válvula de Pé",
        img="produto-flutuante-valvula.jpg",
        gancho="Flutuação dedicada para proteger e posicionar a válvula de pé do seu sistema de captação.",
        bullets=["Mesma linha construtiva do flutuante para PEAD"],
        wa="Olá! Vim pelo site e quero um orçamento para o Flutuante para Válvula de Pé.",
    ),
    dict(
        slug="reservatorio-agua",
        title="Reservatório de Água",
        img="produto-reservatorio.jpg",
        gancho="Torre elevada em aço para armazenar água com pressão e autonomia para a propriedade.",
        bullets=["Torre elevada / caixa d'água metálica"],
        wa="Olá! Vim pelo site e quero um orçamento para um Reservatório de Água.",
    ),
]

OUTROS = [
    dict(
        slug="articulador-pead",
        title="Articulador de PEAD",
        img="outros-articulador-pead.jpg",
        gancho="Articulação galvanizada a fogo com mangote de trama de aço, para movimento seguro da linha.",
    ),
    dict(
        slug="conexoes-aco-zincado",
        title="Conexões de Aço Zincado",
        img="outros-conexoes-zincado.jpg",
        gancho="Curvas, luvas e adaptadores zincados para montagem da linha de captação.",
    ),
    dict(
        slug="cestos-succao",
        title="Cestos para Sucção",
        img="outros-cestos-succao.jpg",
        gancho="Proteção da bomba contra detritos, em aço telado resistente.",
    ),
    dict(
        slug="valvula-pe-inox",
        title="Válvula de Pé de Inox",
        img="outros-valvula-inox.jpg",
        gancho="Corpo em inox com cesto de sucção integrado, para maior durabilidade.",
    ),
    dict(
        slug="ipsilon-aco-zincado",
        title="Ípsilon de Aço Zincado",
        img="outros-ipsilon-zincado.jpg",
        gancho='Peça em "Y" para dividir ou unir linhas de captação.',
    ),
    dict(
        slug="pipe-rack",
        title="Pipe Rack",
        img="outros-pipe-rack.jpg",
        gancho="Estrutura elevada para sustentar tubulações com segurança.",
    ),
    dict(
        slug="barrilete",
        title="Barrilete",
        img="outros-barrilete.jpg",
        gancho="Coletor metálico para distribuir as linhas de água da instalação.",
    ),
]

for item in OUTROS:
    item.setdefault("bullets", [])
    item.setdefault(
        "wa",
        f"Olá! Vim pelo site e quero um orçamento para o(a) {item['title']}.",
    )

ALL_PRODUCTS = CHAMPIONS + OUTROS

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | 2J.A Estruturas Metálicas</title>
<meta name="description" content="{gancho}">
<link rel="stylesheet" href="../styles.css">
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a href="../index.html" class="logo-link">
      <img src="../assets/logo/logo_2ja_transparente.png" alt="2J.A Estruturas Metálicas" class="logo-img">
    </a>
    <a href="#" class="btn btn-accent btn-sm" data-wa="Olá! Quero falar com a 2J.A Estruturas Metálicas.">WhatsApp</a>
  </div>
</header>

<main>
  <section class="section produto-detalhe">
    <div class="wrap">
      <a href="../index.html#produtos" class="voltar-link">&larr; Voltar para todos os produtos</a>

      <div class="produto-grid">
        <div class="produto-foto" style="background-image:url('../assets/img/{img}')"></div>
        <div class="produto-info">
          <p class="eyebrow">{eyebrow}</p>
          <h1>{title}</h1>
          <p class="gancho-lg">{gancho}</p>
{bullets_html}
          <a href="#" class="btn btn-accent btn-lg" data-wa="{wa}">Pedir orçamento</a>
        </div>
      </div>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-col">
      <img src="../assets/logo/logo_2ja_transparente.png" alt="2J.A Estruturas Metálicas" class="footer-logo">
      <p class="footer-extra">Também fabricamos: galpões, estrutura para placa solar, pergolados e flutuante de lazer.</p>
    </div>
    <div class="footer-col">
      <p class="footer-label">Endereço</p>
      <p>Rodovia GO-222, sentido Nerópolis, KM 7 (à direita), Portal da Serra, Q-03 L-18, S/N — Nova Veneza-GO, CEP 75470-000</p>
    </div>
    <div class="footer-col">
      <p class="footer-label">Contato</p>
      <p><a href="#" data-wa="Olá! Quero falar com a 2J.A Estruturas Metálicas.">(62) 9 9606-1223</a></p>
      <p><a href="#" data-wa="Olá! Quero falar com a 2J.A Estruturas Metálicas.">(62) 9 9815-1581</a></p>
      <p><a href="mailto:2j.asolucoes@gmail.com">2j.asolucoes@gmail.com</a></p>
      <p><a href="https://instagram.com/2j.asolucoes" target="_blank" rel="noopener">@2j.asolucoes</a></p>
    </div>
  </div>
  <p class="copyright">© 2026 2J.A Estruturas Metálicas. Todos os direitos reservados.</p>
</footer>

<a href="#" class="wa-float" data-wa="Olá! Quero falar com a 2J.A Estruturas Metálicas." aria-label="Falar no WhatsApp">
  <svg viewBox="0 0 32 32" width="28" height="28" fill="currentColor" aria-hidden="true"><path d="M16.001 3C9.11 3 3.5 8.607 3.5 15.5c0 2.44.71 4.71 1.94 6.63L3 29l7.05-2.4a12.4 12.4 0 0 0 5.95 1.5c6.89 0 12.5-5.607 12.5-12.5S22.89 3 16 3zm0 22.6c-1.94 0-3.75-.53-5.3-1.46l-.38-.22-4.19 1.43 1.4-4.09-.25-.4a10.05 10.05 0 0 1-1.56-5.36c0-5.6 4.55-10.15 10.15-10.15s10.15 4.55 10.15 10.15S21.6 25.6 16 25.6zm5.55-7.6c-.3-.15-1.78-.88-2.06-.98-.28-.1-.48-.15-.68.15-.2.3-.78.98-.96 1.18-.18.2-.35.22-.65.08-.3-.15-1.27-.47-2.42-1.5-.9-.8-1.5-1.79-1.68-2.09-.18-.3-.02-.46.13-.6.14-.14.3-.35.45-.53.15-.18.2-.3.3-.5.1-.2.05-.38-.02-.53-.08-.15-.68-1.65-.94-2.26-.25-.6-.5-.5-.68-.51h-.58c-.2 0-.53.08-.8.38-.28.3-1.05 1.02-1.05 2.5s1.08 2.9 1.23 3.1c.15.2 2.13 3.25 5.16 4.56.72.31 1.28.5 1.72.64.72.23 1.38.2 1.9.12.58-.09 1.78-.73 2.03-1.43.25-.7.25-1.3.18-1.43-.08-.13-.28-.2-.58-.35z"/></svg>
</a>

<script src="../script.js"></script>
</body>
</html>
"""


def render(item, eyebrow):
    if item["bullets"]:
        items = "\n".join(f"            <li>{b}</li>" for b in item["bullets"])
        bullets_html = f'          <ul class="bullets-lg">\n{items}\n          </ul>'
    else:
        bullets_html = ""
    return PAGE_TEMPLATE.format(
        title=item["title"],
        img=item["img"],
        gancho=item["gancho"],
        wa=item["wa"],
        bullets_html=bullets_html,
        eyebrow=eyebrow,
    )


for item in CHAMPIONS:
    html = render(item, "Produto Campeão")
    with open(os.path.join(OUT_DIR, f"{item['slug']}.html"), "w") as f:
        f.write(html)

for item in OUTROS:
    html = render(item, "Complemento Técnico")
    with open(os.path.join(OUT_DIR, f"{item['slug']}.html"), "w") as f:
        f.write(html)

print(f"Geradas {len(ALL_PRODUCTS)} páginas em {OUT_DIR}")
for item in ALL_PRODUCTS:
    print(f"  produtos/{item['slug']}.html")
