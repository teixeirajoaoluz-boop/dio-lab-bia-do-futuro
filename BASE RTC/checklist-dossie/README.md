# Checklist de Entrega e Estrutura do Dossiê — mcp-planejamento-RTC

Fontes analisadas: `mcp_planejamento_rtc/checklist.py` (47 linhas) e
`mcp_planejamento_rtc/dossie.py` (320 linhas).

## 1. Checklist de entrega (`checklist_entrega`)

Gate de qualidade citado no código como "MODELO_DE_ENTREGA.md §6" — roda sobre
a pasta de um cliente e devolve verde/pendências antes de liberar a entrega.
Verifica três blocos, na ordem:

1. **`premissas.json` presente e válido** — em `00_ENTRADA/premissas.json`.
   Se o arquivo não existe, item falha direto. Se existe, é carregado com
   validação (`premissas_mod.carregar(..., validar_tambem=True)`); qualquer
   problema de validação (`_validacao`) reprova o item e lista o(s) motivo(s).
2. **Artefatos numerados presentes** — um item de checklist por artefato
   esperado (ver seção 2). O conjunto de artefatos depende do perfil da
   empresa: perfil padrão (exportadora) exige 6 artefatos; perfil farma
   exige 2. Cada item procura no disco um arquivo que bata com o padrão
   `{numero}_*{tema}.{extensao}`.
3. **Pasta `99_ENTREGA` presente** — pasta de empacotamento final do pacote
   de entrega.

Resultado: `{pasta, pronto (bool), score "N/M", itens: [{item, ok, detalhe}]}`.
`pronto` só é `true` quando todos os itens estão OK.

Esse checklist depende de um módulo `premissas` (validação de premissas) que
não foi lido nesta tarefa — a regra de validação em si (o que torna um
`premissas.json` "válido") está fora do escopo analisado aqui.

## 2. Estrutura de artefatos do dossiê (`dossie.py`)

O dossiê é gerado a partir de um único `premissas.json` normalizado. Existem
dois pacotes de artefatos, escolhidos pelo perfil da empresa
(`eh_farma()`: perfil contém "farma"/"farmac" ou existe bloco `farma` nas
premissas):

- **Perfil padrão (exportadora), 6 artefatos** — gerados por dois scripts
  geradores **externos ao repositório**, que vivem no Google Drive
  (`G:\...\mcp-planejamento-RTC\Dados Base\gerar_modelo_nf.py` e
  `gerar_versao_final.py`). Esses scripts NÃO estão presentes no
  arquivo-fonte lido — apenas a lista de artefatos que eles devem produzir e
  a convenção de chamada (`python <gerador> <premissas.json> <pasta_saida>`).
  Ver `estrutura-dossie.md` para a lista completa.
- **Perfil farma, 2 artefatos** — gerados em Python puro, dentro do próprio
  `dossie.py` (sem depender dos geradores externos). Ver `estrutura-dossie.md`
  para o esqueleto de seções do artefato principal (Comportamento Farma, MD).

### Pasta do cliente

Cada cliente ganha uma pasta `"{RAZAO_SOCIAL EM MAIÚSCULO} — {CNPJ}"` com três
subpastas: `00_ENTRADA`, `00_ENTRADA/Memorias_Calculo`, `99_ENTREGA`. As
premissas normalizadas são gravadas em `00_ENTRADA/premissas.json` (UTF-8,
indentado) antes de qualquer geração.

### Nomenclatura de arquivo

Cada artefato é nomeado `{numero}_{slugEmpresa}_{tema}.{extensao}`, onde
`slugEmpresa` é a razão social em TitleCase sem caracteres não-alfanuméricos
(ex.: `EmpresaExemploLtda`).

### Veredito de geração

Ao final, cada artefato recebe status `"gerado"` (arquivo existe no disco) ou
`"FALHOU (arquivo ausente)"`. O veredito geral é `"OK"` só se todos os
artefatos do pacote foram gerados; caso contrário `"INCOMPLETO"`.

## 3. Lacunas explícitas

- Os dois scripts geradores do pacote exportadora (`gerar_modelo_nf.py`,
  `gerar_versao_final.py`) são templates/scripts externos não presentes nesta
  análise — apenas a lista de artefatos e a convenção de chamada são
  conhecidas. O conteúdo/estrutura interna do Parecer (01), Apresentação (02),
  DRE (03), Modelo de NF (04, 05) e Implementação da Plataforma (06) não pôde
  ser extraído porque esses geradores não foram lidos.
- A regra de validação de `premissas.json` (o que é "válido") está no módulo
  `premissas`, não lido nesta tarefa.
