# Home 2J.A Estruturas Metálicas — Design

## Contexto

Site vitrine de página única (one-page) para a 2J.A Estruturas Metálicas, fabricante de
estruturas metálicas para captação de água na irrigação agrícola (balsas, flutuantes,
conexões, reservatórios), sediada entre Nerópolis e Nova Veneza-GO. A empresa não tem
site hoje, só Instagram. Objetivo do site: converter visita em contato via WhatsApp —
sem formulário, sem página institucional separada.

Este é o primeiro teste visual a ser mostrado ao Artur (sócio da 2J.A) para validar se a
linha de raciocínio (estrutura + direção visual) está no caminho certo antes de refinar
detalhes.

Fontes usadas: `Copy_2JA_Home_v2.pdf` (copy final linha por linha), `briefing_2ja.html`
(pesquisa de mercado + posicionamento + paleta), `PORTIFÓLIO 2J.A (1).pdf` (fotos reais
por produto), `cartao visitas (3).pdf` (serviços adicionais da empresa).

## Decisões de conteúdo

- **Headline do Hero**: opção C — "Balsas, flutuantes e estruturas metálicas para
  captação de água na sua fazenda".
- **Área de atuação**: nacional — "Atendemos produtores em todo o Brasil, com
  fabricação própria na Rodovia GO-222, entre Nerópolis e Nova Veneza."
- **Serviços fora do catálogo principal** (galpões, estrutura para placa solar,
  pergolados, flutuante de lazer — vistos no cartão de visita mas fora da copy
  aprovada): entram como uma linha discreta no rodapé, sem cards, sem destaque visual
  — ex.: "Também fabricamos: galpões, estrutura para placa solar, pergolados e
  flutuante de lazer."
- Todo o restante do texto (headlines de produto, bullets, diferenciais, contato, SEO)
  segue `Copy_2JA_Home_v2.pdf` literalmente, sem parafrasear.
- Números de WhatsApp convertidos para link `wa.me` em formato E.164:
  `5562996061223` e `5562998151581`. Cada botão de produto usa a mensagem
  pré-preenchida exata da copy.

## Direção visual — Editorial Premium

Confirmada com base no logo real e no cartão de visita (tipografia serifada refinada,
preto e branco, bastante espaço em branco) — não a linha industrial-brutalista
alternativa que também foi cogitada.

- **Paleta — revisada após feedback direto do Artur** (v2): a paleta ferrugem/aço do
  briefing inicial foi **substituída** por uma paleta monocromática (preto/branco/
  cinza-morno), porque o Artur pediu explicitamente para seguir a paleta de cores da
  própria logo — e todo o material de marca real do cliente (cartão de visita, van,
  fachada, polo, crachá na `ARPESENTAÇÃO VISUAL.pdf`) é 100% preto e branco, sem
  nenhuma cor. A logo em si (`logo_2ja_transparente.png`) é um glifo branco sobre
  fundo transparente — precisa de `filter: brightness(0) saturate(100%)` para ficar
  legível sobre as superfícies claras do site (header/rodapé) e nenhum filtro sobre
  fundos escuros.
  - `--bg: #F7F5F1` · `--surface: #FFFFFF` · `--surface-2: #EDEAE3`
  - `--text: #141414` · `--text-muted: #5C5A55`
  - `--accent: #141414` (preto, botões/CTAs) · `--accent-ink: #FFFFFF`
  - `--accent-2: #5C5A55` (cinza médio, detalhes e links)
  - `--line: #E2DFD7` · `--line-strong: #C9C5B9`
  - Dark mode automático via `prefers-color-scheme: dark` — inverte para fundo quase
    preto (`#141414`) com texto e acentos quase brancos (`#F2F0EC`).
- **Tipografia**: display serifado (Georgia/"Iowan Old Style"/"Palatino Linotype") nos
  títulos, ecoando o serifado do wordmark "2J.A"; corpo em sans-serif do sistema;
  rótulos técnicos/badges em monoespaçada (reforça o caráter técnico sem virar
  brutalista).
- **Fotografia real** em destaque em todo o site — hero, cards de produto, diferenciais
  — nunca ilustração genérica ou ícone de estoque. As fotos usadas em cada produto
  seguem exatamente o agrupamento que o `PORTIFÓLIO 2J.A (1).pdf` já define página a
  página (ex.: pág. 4 = fotos da Balsa Bloc., pág. 5 = fotos da Balsa Mancalizada).
  Mapeamento final foto↔produto é conferido visualmente contra o PDF durante a
  implementação, não de memória.
- Logo: usar o PNG transparente (`assets/logo/logo_2ja_transparente.png`) — funciona
  tanto sobre fundo claro quanto escuro.

## Estrutura da página (one-page + páginas de produto)

Ordem exata, sem menu institucional — toda navegação empurra para o WhatsApp:

1. **Cabeçalho fixo** — logo + botão "WhatsApp"
2. **Hero** — headline C, subheadline, botão "Falar no WhatsApp", linha de confiança,
   foto de fundo de balsa em operação no rio
3. **Produtos Campeões** — 5 cards grandes (Balsa Bloc., Balsa Mancalizada, Flutuante
   PEAD, Flutuante Válvula de Pé, Reservatório de Água), cada um com foto real, título,
   gancho, bullets de componentes e botão de orçamento com mensagem própria
4. **Outros Produtos** — grade compacta de 7 itens (nome + descrição de uma linha +
   foto pequena), um único CTA no fim da grade
5. **Diferenciais** — 5 cards curtos (Preço Justo, Agilidade, Mão de Obra Qualificada,
   Parceria, Estrutura Própria)
6. **Área de Atuação** — título + texto (nacional)
7. **Faixa da fábrica** — foto aérea real da fábrica (extraída do portfólio) com legenda
8. **Onde estamos** — card escuro com endereço completo + botões "Traçar rota" e
   "Abrir no Google Maps" (deep links do Google Maps) ao lado de um mapa incorporado
   do OpenStreetMap (sem necessidade de chave de API), com marcador aproximado sobre a
   GO-222 entre Nerópolis e Nova Veneza. Padrão pedido pelo Artur a partir de um site
   de referência.
9. **Rodapé + Contato** — endereço, 2 WhatsApp, e-mail, Instagram, linha de serviços
   extra, copyright
10. **Botão WhatsApp flutuante** — fixo do hero ao rodapé, mensagem genérica de contato

**Páginas de produto dedicadas** (pedido do Artur, revisão do escopo one-page
original): cada um dos 12 produtos (5 campeões + 7 outros) tem uma página própria em
`produtos/<slug>.html` — foto grande, gancho completo, bullets e CTA de orçamento. Os
cards da Home linkam para essas páginas (foto e título clicáveis); o botão "Pedir
orçamento" continua indo direto pro WhatsApp, não para a página do produto. As páginas
são geradas por `scripts/gen_products.py` a partir de uma lista de dados — reexecutar
o script sempre que a copy de produto mudar, em vez de editar os HTMLs gerados à mão.

## Abordagem técnica

HTML/CSS/JS estático, sem framework e sem build step — apropriado para uma página
única com deploy simples na Hostinger (`deployStaticWebsite`) depois que o cliente
aprovar.

Arquivos:
- `index.html`
- `styles.css`
- `script.js` (comportamento do botão flutuante + qualquer micro-interação de scroll)
- `assets/logo/logo_2ja_transparente.png` (já presente)
- `assets/img/` — versões otimizadas (redimensionadas/comprimidas) das fotos
  selecionadas do portfólio, renomeadas de forma descritiva (ex.:
  `hero-balsa-rio.jpg`, `produto-balsa-bloc-1.jpg`) em vez dos nomes genéricos
  `img-0XX.jpg` da extração bruta em `assets/fotos/`

SEO: `<title>` e `<meta name="description">` exatamente como especificados na copy
(seção 7). Sem analytics/tracking nesta primeira versão — pode entrar depois se o
cliente pedir.

## Nota — revisão de layout (anti-slop, v3)

A v1/v2 usava a mesma família de layout (grade de cards brancos com sombra, radius
uniforme) em três seções seguidas (Produtos Campeões, Outros Produtos, Diferenciais) —
a assinatura visual mais reconhecível de "feito por IA" (skill `design-taste-frontend`,
regra de Section-Layout-Repetition). Revisado para três composições genuinamente
diferentes:
- **Produtos Campeões**: um destaque editorial full-bleed para o carro-chefe (Balsa
  Bloc., sem card, bullets em duas colunas) + bento assimétrico para os outros 4
  (tamanhos de célula variados, foto como fundo com texto sobreposto).
- **Outros Produtos**: lista compacta de duas colunas (miniatura + nome + descrição),
  separada por hairlines, sem cards nem sombra.
- **Diferenciais**: lista numerada editorial (numeral serifado grande + título +
  descrição), também sem cards.
Eyebrows (rótulos pequenos em caixa alta) reduzidos de 4 para 1 na página inteira.
Adicionado scroll-reveal leve (fade + translateY via IntersectionObserver,
`prefers-reduced-motion` respeitado) para dar ritmo sem ser decorativo.

## Nota — fotos adicionais da empresa

O Artur pediu para incorporar mais fotos reais da empresa (não só produto). O perfil
`@2j.asolucoes` no Instagram existe e é ativo, mas suas imagens ficam atrás de URLs de
CDN assinadas/expiráveis que não podem ser baixadas por ferramenta automatizada
(testado, bloqueado). Google Meu Negócio não retornou fotos via busca. Caminho mais
confiável: o próprio Artur exportar fotos do celular/Instagram e enviar diretamente.
Por ora, a foto aérea real da fábrica (já extraída do portfólio) foi adicionada como
uma faixa dedicada antes da seção "Onde estamos".

## Fora de escopo (não fazer nesta rodada)

- Especificações técnicas dos campeões (vazão, CV, dimensões) — pendente de
  confirmação do Artur, não bloqueia esta primeira versão.
- Domínio/DNS/deploy na Hostinger — configurado depois que o layout for aprovado.
- Depoimentos ou nomes de fazendas atendidas (prova social) — não existem ainda.
- Vídeos institucionais — só fotos por enquanto.
- Analytics/tracking.
