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

- **Paleta** (definida no briefing, evita o verde saturado que Bauer/Valley/Hidrogeral/
  Irrigafort usam — diferenciação imediata):
  - `--bg: #F6F2EA` · `--surface: #FFFFFF` · `--surface-2: #EFE9DC`
  - `--text: #221F1A` · `--text-muted: #6B6357`
  - `--accent: #AE4B1D` (ferrugem, botões/CTAs) · `--accent-ink: #FFFFFF`
  - `--accent-2: #3D6B78` (aço/teal, detalhes e links)
  - `--line: #DFD6C4` · `--line-strong: #C9BEA6`
  - Dark mode automático via `prefers-color-scheme: dark`, tokens equivalentes já
    definidos no briefing (`#17181A` bg, `#E1834B` accent, etc.)
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

## Estrutura da página (one-page)

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
7. **Rodapé + Contato** — endereço, 2 WhatsApp, e-mail, Instagram, linha de serviços
   extra, copyright
8. **Botão WhatsApp flutuante** — fixo do hero ao rodapé, mensagem genérica de contato

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

## Fora de escopo (não fazer nesta rodada)

- Especificações técnicas dos campeões (vazão, CV, dimensões) — pendente de
  confirmação do Artur, não bloqueia esta primeira versão.
- Domínio/DNS/deploy na Hostinger — configurado depois que o layout for aprovado.
- Depoimentos ou nomes de fazendas atendidas (prova social) — não existem ainda.
- Vídeos institucionais — só fotos por enquanto.
- Analytics/tracking.
