# Fotos para tratar com IA

Pedido do Artur (2J.A): passar as fotos reais dos produtos por um tratamento com IA para **melhorar o fundo**, antes de entrarem no site. O layout do site não muda; a mudança é só nas fotos.

## Decisões

- **O produto fica idêntico** (forma, cor, logo 2J.A, proporções, quantidade de peças). Muda só o fundo e a iluminação.
- **São tratadas** as fotos dos cartões da home, das páginas de produto e o fundo do topo da home.
- **A seção "Veja o produto pronto" não muda**: continua com as fotos reais da fábrica e os textos atuais, como prova de que a 2J.A fabrica de verdade. Quando a mesma foto aparece na seção e num cartão ou página, só o cartão ou página passa a usar a versão tratada.
- **Cenários**: balsas e flutuantes em represa/lago com mata nativa do cerrado; peças (conexões, tubos, cestos, válvulas) em piso de concreto limpo, com luz natural e lavoura desfocada ao fundo. Nenhuma peça solta na água.
- **Fotos antigas de cerca de 600 px não são tratadas agora**: dependem do original do cliente.
- As versões tratadas vão em `assets/img/ia/`, com o mesmo nome do arquivo original (sem a pasta `galeria/`). As originais não são apagadas nem sobrescritas.
- Referência de estilo: as duas artes da balsa preta em lago (mata ao fundo, céu azul, água refletindo), usadas no anúncio patrocinado do Instagram.

## 1. Tratar agora (7 fotos, resolução boa)

| Arquivo (em `assets/img/`) | Produto | Onde a versão tratada entra | Fundo atual | Cenário | Precisa do original |
|---|---|---|---|---|---|
| `galeria/balsa-galvanizada-2.jpg` | Balsa galvanizada | Fundo do topo da home | pátio | Margem de represa, água e mata ao fundo | não |
| `galeria/balsa-telhado-3.jpg` | Balsa preta com telhado | Página Balsa Bloc (galeria) | pátio, outras balsas ao fundo | Represa/lago com mata do cerrado | não |
| `galeria/balsa-telhado-2.jpg` | Balsa preta com telhado | Página Balsa Bloc (galeria) | pátio de cascalho | Represa/lago com mata do cerrado | não |
| `galeria/balsa-azul.jpg` | Balsa azul | Página Balsa Bloc (galeria) | pátio, caminhão ao fundo | Represa/lago com mata do cerrado | não |
| `galeria/conexoes-lote.jpg` | Conexões galvanizadas (lote) | Cartão "Conexões" na home · página Conexões (foto principal) | pátio, estruturas e placas ao fundo | Piso de concreto limpo, luz natural, lavoura desfocada ao fundo | não |
| `galeria/conexao-te.jpg` | Tê com flange | Página Conexões (galeria) | galpão | Piso de concreto limpo, luz natural, lavoura desfocada ao fundo | não |
| `galeria/conexao-curva.jpg` | Curva com flange | Página Conexões (galeria) | pátio | Piso de concreto limpo, luz natural, lavoura desfocada ao fundo | não |

## 2. Depende do original do cliente (12 fotos)

Estas fotos foram ampliadas a partir de imagens de cerca de 600 px e estão borradas. Trocar o fundo não recupera a nitidez do produto. Pedir ao Artur a foto original (do celular ou da câmera, enviada como arquivo/documento, não como foto comprimida do WhatsApp).

| Arquivo (em `assets/img/`) | Produto | Onde aparece | Fundo atual | Precisa do original | Depois de receber |
|---|---|---|---|---|---|
| `produto-flutuante-pead.jpg` | Flutuante para PEAD | Cartão na home · página do produto | chão de oficina | sim | Tratar o fundo: represa/lago com mata do cerrado |
| `outros-articulador-pead.jpg` | Articulador de PEAD | Cartão na home · página do produto | oficina | sim | Tratar o fundo: piso de concreto limpo, luz natural, lavoura desfocada ao fundo |
| `outros-conexoes-zincado.jpg` | Conexões de Aço Zincado | Página Conexões (4ª foto) | oficina, pneus ao fundo | sim | Tratar o fundo: piso de concreto limpo, luz natural, lavoura desfocada ao fundo |
| `outros-cestos-succao.jpg` | Cestos para Sucção | Cartão na home · página do produto | chão de oficina | sim | Tratar o fundo: piso de concreto limpo, luz natural, lavoura desfocada ao fundo |
| `outros-valvula-inox.jpg` | Válvula de Pé de Inox | Cartão na home · página do produto | galpão | sim | Tratar o fundo: piso de concreto limpo, luz natural, lavoura desfocada ao fundo |
| `outros-ipsilon-zincado.jpg` | Ípsilon de Aço Zincado | Cartão na home · página do produto | oficina | sim | Tratar o fundo: piso de concreto limpo, luz natural, lavoura desfocada ao fundo |
| `outros-barrilete.jpg` | Barrilete | Cartão na home · página do produto | pátio de terra | sim | Tratar o fundo: piso de concreto limpo, luz natural, lavoura desfocada ao fundo |
| `produto-balsa-bloc.jpg` | Balsa para Bomba Bloc | Destaque da home · página do produto | rio, em uso | sim | Só substituir pela versão nítida; o fundo já é bom |
| `produto-balsa-mancalizada.jpg` | Balsa para Bomba Mancalizada | Cartão na home · página do produto | represa, em uso | sim | Só substituir pela versão nítida; o fundo já é bom |
| `produto-flutuante-valvula.jpg` | Flutuante para Válvula de Pé | Cartão na home · página do produto | lago, em uso | sim | Só substituir pela versão nítida; o fundo já é bom |
| `produto-reservatorio.jpg` | Reservatório de Água | Cartão na home · página do produto | campo, céu azul | sim | Só substituir pela versão nítida; o fundo já é bom |
| `outros-pipe-rack.jpg` | Pipe Rack | Cartão na home · página do produto | instalado sobre rio | sim | Só substituir pela versão nítida; o fundo já é bom |

## 3. Não tratar

- **Seção "Veja o produto pronto"** (12 fotos reais, em `assets/img/thumb/`): `balsa-telhado-3`, `balsa-galvanizada-2`, `balsa-azul`, `balsa-telhado-1`, `balsa-galvanizada-1`, `flutuante-galpao`, `tubos-flangeados-2`, `conexoes-lote`, `conexao-curva`, `cesto-succao-1`, `tubos-flangeados-1`, `cesto-succao-2`.
- `area-atuacao-bg.jpg`, `fabrica-aerea.jpg`: fundos de seção (lavoura e vista aérea da fábrica).
- `instagram/ig-*.jpg`: bastidores da equipe.
- `hero-balsa-rio.jpg` e a pasta `assets/fotos/`: fora de uso.

## 4. Conferência de cada resultado

Comparar a versão tratada com a original antes de aceitar: formato e número de flutuadores, telhado, plataforma, flanges e furos, tela dos cestos, quantidade de peças e logo. Se a IA alterou o produto, descartar e gerar de novo. Um cliente que recebe um produto diferente da foto vira problema de venda.

## 5. Prompts

Anexar a foto original na ferramenta de IA e colar o prompt correspondente.

### Tratar agora

**`galeria/balsa-galvanizada-2.jpg`** — Balsa galvanizada

```
Troque apenas o fundo desta foto. Mantenha a balsa galvanizada com os dois flutuadores longos e a estrutura com telhado exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado na margem de represa, em chão de cascalho limpo, com a água e a mata nativa do cerrado ao fundo e céu azul. Ajuste só a iluminação e as sombras para combinar com o cenário. Mantenha o formato horizontal e a balsa no lado direito da imagem, com área mais livre à esquerda. Foto realista, sem texto e sem pessoas.
```

**`galeria/balsa-telhado-3.jpg`** — Balsa preta com telhado

```
Troque apenas o fundo desta foto. Mantenha a balsa preta com dois flutuadores, plataforma e telhado exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto flutuando na água de uma represa ou lago calmo, com mata nativa do cerrado ao fundo, céu azul com poucas nuvens e reflexo na água. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`galeria/balsa-telhado-2.jpg`** — Balsa preta com telhado

```
Troque apenas o fundo desta foto. Mantenha a balsa preta com dois flutuadores, plataforma e telhado exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto flutuando na água de uma represa ou lago calmo, com mata nativa do cerrado ao fundo, céu azul com poucas nuvens e reflexo na água. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`galeria/balsa-azul.jpg`** — Balsa azul

```
Troque apenas o fundo desta foto. Mantenha a balsa azul com dois flutuadores e a estrutura azul exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto flutuando na água de uma represa ou lago calmo, com mata nativa do cerrado ao fundo, céu azul com poucas nuvens e reflexo na água. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`galeria/conexoes-lote.jpg`** — Conexões galvanizadas (lote)

```
Troque apenas o fundo desta foto. Mantenha todas as conexões galvanizadas sobre os paletes, na mesma quantidade e posição exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`galeria/conexao-te.jpg`** — Tê com flange

```
Troque apenas o fundo desta foto. Mantenha o tê galvanizado com as três flanges exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`galeria/conexao-curva.jpg`** — Curva com flange

```
Troque apenas o fundo desta foto. Mantenha a curva galvanizada com as duas flanges exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

### Quando o original chegar

**`produto-flutuante-pead.jpg`** — Flutuante para PEAD

```
Troque apenas o fundo desta foto. Mantenha os dois flutuadores pretos cilíndricos com as abraçadeiras exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto flutuando na água de uma represa ou lago calmo, com mata nativa do cerrado ao fundo, céu azul com poucas nuvens e reflexo na água. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`outros-articulador-pead.jpg`** — Articulador de PEAD

```
Troque apenas o fundo desta foto. Mantenha o articulador galvanizado com o mangote preto exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`outros-conexoes-zincado.jpg`** — Conexões de Aço Zincado

```
Troque apenas o fundo desta foto. Mantenha os tubos e as conexões zincadas, na mesma quantidade e posição exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`outros-cestos-succao.jpg`** — Cestos para Sucção

```
Troque apenas o fundo desta foto. Mantenha os cestos telados com flange, na mesma quantidade exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`outros-valvula-inox.jpg`** — Válvula de Pé de Inox

```
Troque apenas o fundo desta foto. Mantenha a válvula de inox com o cesto telado e o adesivo 2J.A exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`outros-ipsilon-zincado.jpg`** — Ípsilon de Aço Zincado

```
Troque apenas o fundo desta foto. Mantenha a peça zincada em formato de Y com as flanges exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

**`outros-barrilete.jpg`** — Barrilete

```
Troque apenas o fundo desta foto. Mantenha o barrilete metálico com as saídas flangeadas exatamente como está: mesma forma, mesma cor, mesmas proporções, mesmo ângulo e o logo 2J.A, sem adicionar nem remover peças. Novo cenário: produto apoiado sobre piso de concreto limpo e claro, com luz natural e lavoura irrigada desfocada ao fundo. Ajuste só a iluminação e as sombras para combinar com o cenário. Foto realista, sem texto e sem pessoas.
```

## 6. Plano de troca (ainda não aplicado)

Executar quando as versões tratadas estiverem em `assets/img/ia/`.

1. **Receber e conferir.** Listar o que chegou em `assets/img/ia/` contra a lista da seção 1 e montar uma folha de comparação original × tratada para aprovação (seção 4). Foto reprovada fica de fora e o site segue com a original.
2. **Otimizar.** Cada foto aprovada: no máximo 1600 px de largura, cerca de 200 KB, em JPG (ou WebP, se o arquivo vier nesse formato). Gerar a miniatura de 720 px do cartão em `assets/img/ia/thumb/`. As miniaturas de `assets/img/thumb/` não são tocadas, porque a seção "Veja o produto pronto" depende delas.
3. **Trocar as referências.**
   - `index.html`, fundo do topo: `assets/img/hero-balsa-patio.jpg` → `assets/img/ia/balsa-galvanizada-2.jpg`. Rever em `styles.css` o enquadramento (`.hero{background-position}`) e o escurecimento atrás do texto, no computador e no celular.
   - `index.html`, cartão "Conexões de Aço Zincado" em Peças e acessórios: `assets/img/thumb/conexoes-lote.jpg` → `assets/img/ia/thumb/conexoes-lote.jpg`. A figura "Conexões galvanizadas" da seção "Veja o produto pronto" continua em `assets/img/thumb/conexoes-lote.jpg`.
   - `scripts/gen_products.py`, Balsa Bloc: na lista `galeria`, `galeria/balsa-telhado-3.jpg`, `galeria/balsa-telhado-2.jpg` e `galeria/balsa-azul.jpg` → `ia/…`.
   - `scripts/gen_products.py`, Conexões: `img` `galeria/conexoes-lote.jpg` → `ia/conexoes-lote.jpg`; na `galeria`, `conexao-te` e `conexao-curva` → `ia/…`; atualizar o conjunto `RETRATOS` para os novos caminhos.
   - Rodar `python3 scripts/gen_products.py` para regenerar as páginas em `produtos/`.
4. **Textos alternativos.** Conferir o `alt` de cada foto trocada: deve descrever o produto, sem citar pátio, galpão ou fábrica. Os cartões da home usam `alt=""` (o nome do produto está ao lado) e continuam assim.
5. **Verificar.** Checagem de links em todas as páginas; capturas no celular (390 px) e no computador do topo, do cartão de Conexões e das páginas Balsa Bloc e Conexões; confirmar que a seção "Veja o produto pronto" continua apontando só para as fotos originais.
6. **Publicar.** Commit e envio para a `main` só depois da aprovação visual; conferir a publicação do GitHub Pages no ar.
7. **Segunda rodada.** Quando chegarem os originais da seção 2: tratar as 7 de fundo ruim, apenas otimizar as 5 de fundo bom, salvar em `assets/img/ia/` com o mesmo nome e repetir os passos 1 a 6. As referências a trocar são o `img` de cada produto em `scripts/gen_products.py`, a imagem de destaque da Balsa Bloc e as miniaturas dos cartões em `index.html`.

Para desfazer, basta reverter o commit da troca: as originais continuam no repositório.

**Aviso de cenário (decidido):** incluir a linha "Produto real, cenário ilustrativo." em fonte pequena, logo abaixo da foto principal, apenas nas páginas de produto que usarem foto tratada. Não colocar na home. Entra no passo 3, via `scripts/gen_products.py`.

## 7. Situação da primeira rodada

Aplicadas (prévia local, sem commit): `balsa-galvanizada-2` (topo da home), `balsa-telhado-3`, `balsa-azul`, `conexoes-lote`, `conexao-te` (versão "b") e `conexao-curva`.

Pendente: `balsa-telhado-2`. A versão tratada recebida (`balsa-preta-1`) mostra outro produto: dois telhados, duas estruturas de bomba e outro ângulo. A página da Balsa Bloc continua com a foto original até chegar uma versão fiel.

O aviso "Produto real, cenário ilustrativo." aparece abaixo da foto principal sempre que a foto exibida é uma das tratadas.
