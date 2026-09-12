# Premissas para Projeções Econômico-Financeiras RTC (2027-2033)

> Base de conhecimento canônica e estática. Extraída de código-fonte real (não é
> spec de intenção) em 25/08/2026. Cada regra abaixo cita o arquivo de onde veio.
> Onde a fonte não deixa algo claro, isso é dito explicitamente — não foi inventado.

## Duas plataformas distintas, mesmo domínio de negócio

Os arquivos lidos pertencem a **dois sistemas diferentes** que tratam de premissas
de Reforma Tributária, mas não compartilham schema:

1. **mcp-planejamento-RTC** (`c:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\`) —
   um MCP Python que carrega e valida um arquivo `premissas.json` por cliente.
   Fonte: `mcp_planejamento_rtc/premissas.py`.
2. **Guerra RTC** (`c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\`) —
   a plataforma web (multi-schema Postgres) usada pelos clientes/mentorias, com
   tabelas `premissas` (genérica, livre) e `receita_projecao` (estruturada, anos
   fixos 2027-2033). Fontes: `26_criar_tabela_premissas.sql`,
   `25_criar_tabela_receita_projecao.sql`.

Não há, nos arquivos lidos, nenhuma rotina que sincronize as duas — a integração
entre o `premissas.json` do MCP e as tabelas do Guerra RTC não está documentada
no código disponível. Isso deve ser tratado como lacuna (ver final do documento).

## 1. Premissas exigidas pelo mcp-planejamento-RTC (`premissas.py`)

Fonte: `c:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\mcp_planejamento_rtc\premissas.py`.

O contrato de entrada da plataforma é um `premissas.json` por empresa, com três
blocos de dados declarados no docstring do módulo (linhas 4-7):

- **Fonte A — `ecf`**: valores brutos do último exercício da ECF (Escrituração
  Contábil Fiscal), campos vistos no exemplo real (`NOVO_FRIO_premissas.json`):
  `receita_bruta`, `exportacao`, `mercado_interno`, `pis_cofins`, `icms`, `iss`,
  `ipi`.
- **Fonte B — `serie_anual`**: série CBS/IBS 2027-2033 vinda da "memória 08 da
  plataforma RTC" (não detalhado no arquivo — a estrutura interna de cada item da
  série não está definida em `premissas.py`; o exemplo real trouxe a lista vazia
  `"serie_anual": []`, então o formato de cada elemento é uma lacuna).
  A única regra explícita sobre essa série é a de validação: precisa cobrir os
  anos 2027 a 2033 sem faltar nenhum (`premissas.py`, linhas 73-77).
- **Derivados — calculados, nunca copiados de outra empresa** (comentário
  explícito na linha 7, reforçado pela função `calcular_derivados`):
  - `extracao_art12 = (PIS/COFINS + ICMS + ISS) / mercado_interno`
  - `icms_efetivo = ICMS / mercado_interno`
  Ambos calculados a partir do bloco `ecf`, arredondados a 6 casas decimais
  (`premissas.py`, linhas 20-29). O nome "art. 12" remete ao dispositivo legal da
  LC 214/2025 sobre extração da carga tributária embutida no preço — o cálculo em
  si, porém, é só a fórmula acima; a fundamentação jurídica do artigo não está no
  código.

Regras de negócio adicionais impostas por `validar()` (linhas 32-79):

- O JSON é validado contra um **JSON Schema externo**, que não vive no
  repositório de código, e sim no Drive: caminho padrão
  `G:\Meu Drive\Projetos de Execução\MCP\mcp-planejamento-RTC\premissas.schema.json`
  (linha 16). Esse schema não foi lido nesta tarefa (fica fora da pasta de código
  C:), então seu conteúdo é uma lacuna aqui — `schema-premissas.json` neste pacote
  foi montado a partir da estrutura observável no `.py` e no SQL, não do schema
  real do Drive.
- Se `jsonschema` não estiver instalado, a validação estrutural é pulada e um
  aviso é anexado à lista de problemas (não interrompe o fluxo).
- **Consistência receita bruta x mercado interno/exportação**: `exportacao +
  mercado_interno` não pode divergir de `receita_bruta` em mais de 5% (linha 59).
- **Derivados informados x recalculados**: se o JSON já trouxer `extracao_art12`
  ou `icms_efetivo` prontos, eles precisam bater (tolerância `1e-4`) com o que
  seria recalculado a partir da `ecf` — nunca aceitos "de olho" (linhas 64-71).
- **Série anual completa 2027-2033**: nenhum ano do intervalo pode faltar
  (linhas 73-77).
- A validação **nunca lança exceção**: sempre devolve uma lista de strings
  (vazia = OK), anexada no próprio dicionário de premissas sob a chave
  `_validacao` quando carregado via `carregar()` (linhas 82-88).

## 2. Premissas na plataforma Guerra RTC (banco de dados)

### 2.1 Tabela `PROJETOBEF.premissas` — genérica

Fonte: `26_criar_tabela_premissas.sql`.

Esta tabela **não tem colunas fixas de premissa tributária** — é uma grade
livre, definida pelo usuário por empresa:

- `id`, `companyId` (FK para `companies`), `name`, `description`
- `columns` (JSONB): definição de colunas — lista de objetos `{id, label}`
- `rows` (JSONB): linhas preenchidas pelo usuário, cada uma com valores por
  coluna
- `metadata` (JSONB, sem estrutura definida no SQL)

Ou seja: o schema SQL não impõe quais premissas existem (sazonalidade,
alíquotas, cronograma etc.) — isso é decidido pelo usuário/consultor ao montar
a grade na tela, e fica registrado como dado livre, não como schema. Qualquer
regra de "quais colunas uma premissa RTC deveria ter" não está no banco — se
existe em algum lugar do frontend, esse código não foi lido nesta tarefa.

### 2.2 Tabela `PROJETOBEF.receita_projecao` — projeção de receita estruturada

Fonte: `25_criar_tabela_receita_projecao.sql`.

Esta é a tabela que **efetivamente estrutura a projeção 2027-2033**, uma linha
por item de receita, vinculada 1:1 (`UNIQUE`) a uma receita consolidada
importada (`consolidated_revenues`, fora do escopo lido):

- Identificação do item: `data_projetada`, `tipo_receita`,
  `codigo_item_servico`, `descricao_produto_servico`
- Premissas de crescimento e redução aplicadas à série:
  - `percentual_crescimento` — crescimento ano a ano (armazenado 0-100)
  - `reducao_ibs_percentual` / `reducao_cbs_percentual` — reduções de alíquota
    aplicáveis (ex.: regimes diferenciados/específicos previstos na LC 214)
- Para **cada ano de 2027 a 2033** (bloco repetido 7x), cinco campos:
  `valor_operacao_AAAA`, `percentual_ibs_AAAA`, `valor_ibs_AAAA`,
  `percentual_cbs_AAAA`, `valor_cbs_AAAA`
- Índices: unicidade por `receita_id`, índice por `data_projetada`

Isso mostra que a premissa mínima de "ano-base + horizonte" da consultoria é
**2027-2033 fixo, ano a ano**, com valor de operação e alíquota efetiva de IBS
e CBS discriminados por ano — não um crescimento composto calculado em tempo
de leitura, e sim uma matriz pré-calculada e persistida (a fórmula que gera
esses valores a partir de `percentual_crescimento` não está neste SQL; vive em
código de aplicação/backend não lido nesta tarefa).

### 2.3 `30_check_formulas_glossario.py` e `30_importar_lote_dorna.py`

- `30_check_formulas_glossario.py`: script de diagnóstico que verifica se a
  tabela `public.formulas_glossario` existe e lista fórmulas cadastradas para
  `receita_projecao.valor_operacao_*` (linhas 130-144). Confirma que existe um
  **glossário de fórmulas versionado no banco** (tabela `tabela`/`coluna`/
  `sigla`/`expressao_texto`/`descricao`) que documenta como cada coluna de
  `receita_projecao` é calculada — mas o conteúdo das fórmulas em si (a
  expressão de `valor_operacao_2027`, por exemplo) não foi lido nesta tarefa,
  só a existência do mecanismo.
- `30_importar_lote_dorna.py`: script de importação em lote de empresas/usuários
  (CNPJ, regime tributário, responsável) a partir de planilha Excel. **Não
  contém lógica de premissas ou de projeção** — é cadastro cadastral (cria
  `users`/`companies`/`user_companies`), fora do escopo de premissas
  propriamente dito. Citado aqui só para registrar que foi lido e não trouxe
  regra de negócio relevante para este documento.

## 3. Como as premissas alimentam a DRE projetada / fluxo de caixa

Os arquivos lidos **não contêm** a lógica que transforma `receita_projecao` (ou
o `premissas.json`) em DRE projetada ou fluxo de caixa — isso não está em
nenhum dos arquivos-fonte desta tarefa. O que se pode afirmar apenas a partir
do que foi lido:

- A unidade básica de saída é a série anual 2027-2033 de `valor_operacao`,
  `valor_ibs` e `valor_cbs` por item de receita (`receita_projecao`).
- Os "derivados" do `premissas.py` (`extracao_art12`, `icms_efetivo`) são a
  ponte entre a carga tributária efetiva histórica (regime atual) e a
  projeção sob IBS/CBS — mas o cálculo que os usa para gerar a DRE/fluxo de
  caixa projetados não está nos arquivos lidos.
- A tabela de fórmulas (`formulas_glossario`) sugere que o cálculo de
  `valor_operacao_AAAA` etc. é documentado e versionado no banco, não
  hardcoded — mas o conteúdo dessas fórmulas é uma lacuna aqui.

## Lacunas explícitas (não inventadas, para não confundir o futuro MCP de mentorias)

1. **Schema formal do `premissas.json`** (`premissas.schema.json` no Drive) não
   foi lido — só inferido da leitura de `premissas.py` + exemplo real. O
   `schema-premissas.json` deste pacote é uma reconstrução, não uma cópia do
   schema oficial.
2. **Formato de cada item de `serie_anual`** não está definido em código lido
   (o exemplo real tinha lista vazia).
3. **Conteúdo das fórmulas** em `formulas_glossario` (como `valor_operacao_AAAA`
   é calculado a partir de `percentual_crescimento` e do ano anterior) não foi
   lido.
4. **Integração entre `premissas.json` (MCP) e as tabelas SQL do Guerra RTC**
   (premissas / receita_projecao) não aparece em nenhum arquivo lido — pode
   existir em outro serviço/rota do backend não coberto por este escopo.
5. **Lógica de DRE projetada e fluxo de caixa** (2027-2033) não está nos
   arquivos lidos — só a estrutura de dados de entrada/saída de receita.
6. **Sazonalidade de vendas/compras e cronograma de transição** (mencionados no
   pedido original) não aparecem como campos explícitos em nenhum dos arquivos
   lidos — não há evidência de que existam como conceito modelado no código
   atual; se existem, vivem em outro lugar não coberto aqui.

## Referências

- `c:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\mcp_planejamento_rtc\premissas.py`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\26_criar_tabela_premissas.sql`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\26.01_executar_26_criar_tabela_premissas.py`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\25_criar_tabela_receita_projecao.sql`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\30_check_formulas_glossario.py`
- `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\30_importar_lote_dorna.py`
- `c:\MCPs\05_Consultor_Tributario\mcp-planejamento-RTC\dados_clientes\NOVO_FRIO_premissas.json`
  (referência de formato — dados específicos de cliente não replicados aqui)
