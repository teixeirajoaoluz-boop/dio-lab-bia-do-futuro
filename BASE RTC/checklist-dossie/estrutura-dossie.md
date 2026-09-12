# Estrutura do Dossiê Técnico — mcp-planejamento-RTC

Fonte: `mcp_planejamento_rtc/dossie.py`. Dois pacotes de artefatos, conforme
o perfil da empresa (`eh_farma()`).

## Pacote padrão (perfil exportadora / geral) — 6 artefatos

Gerados por dois scripts externos ao repositório (vivem no Google Drive,
pasta `Dados Base`), invocados via `subprocess` com
`python <gerador> <premissas.json> <pasta_saida>`. **O conteúdo interno
desses geradores não está disponível nesta análise** — apenas a lista abaixo,
extraída da constante `ARTEFATOS`.

| # | Tema (nome do arquivo) | Formato | Gerador responsável |
|---|---|---|---|
| 01 | Parecer_ReformaTributaria | .docx | gerar_versao_final.py |
| 02 | Apresentacao_ReformaTributaria | .pptx | gerar_versao_final.py |
| 03 | DRE_Consolidada | .xlsx | gerar_versao_final.py |
| 04 | Modelo_NF_Precificacao | .docx | gerar_modelo_nf.py |
| 05 | Modelo_NF_Demonstrativo | .xlsx | gerar_modelo_nf.py |
| 06 | Implementacao_Plataforma | .md | gerar_versao_final.py |

Nome final de cada arquivo: `{numero}_{SlugEmpresa}_{tema}.{extensao}`.

> **Lacuna**: os geradores `gerar_modelo_nf.py` e `gerar_versao_final.py` não
> estão neste repositório nem foram lidos — não é possível descrever aqui o
> conteúdo/seções internas do Parecer, da Apresentação, da DRE ou dos
> Modelos de NF. Só a existência e o rótulo de cada artefato são conhecidos.

## Pacote perfil FARMA — 2 artefatos

Gerados em Python puro dentro do próprio `dossie.py` (funções
`_gerar_md_farma` e `_gerar_xlsx_farma`), sem depender dos geradores externos.

| # | Tema | Formato |
|---|---|---|
| 01 | Comportamento_Farma | .md |
| 02 | Comportamento_Farma | .xlsx |

### Esqueleto do artefato 01 (Comportamento_Farma.md)

Título: `Comportamento Tributário — Segmento Farma (IBS/CBS)`, com subtítulo
razão social + CNPJ, data do parecer (se houver), perfil da empresa e base
legal citada ("LC 214/2025 — regime diferenciado da saúde").

1. **Os 3 baldes do mix**
   Explica que toda venda cai em um "balde" tributário e que a alíquota
   efetiva = alíquota-padrão do ano × (1 − redução do balde). Contém tabela:
   Balde | Mix | Redução | Efetiva 2027 | Efetiva 2033 | CST / cClassTrib.
   Fecha com: alíquota cheia de referência em 2033, alíquota efetiva
   mesclada do mix e a economia percentual frente à tributação integral.

2. **Comportamento ano a ano (transição 2027-2033)**
   Tabela: Ano | Alíq. efetiva mesclada | Receita | Débito IBS/CBS | Crédito
   IBS/CBS | Posição líquida. Nota de rodapé explica que posição líquida =
   débito − crédito, e que o crédito é calculado por uma razão
   crédito/débito sobre o débito (não-cumulatividade plena sobre compras).

3. **As mudanças operacionais que mais pesam na drogaria**
   Lista numerada com as notas operacionais da empresa (ou uma lista padrão
   do módulo `farma`, se a empresa não tiver notas próprias nas premissas).

4. **Condição do benefício (CMED / compromisso)**
   Explica que o benefício de 60%/zero só se mantém enquanto a
   indústria/importador cumprir a regulação de preço da CMED ou o
   compromisso com a União e o Comitê Gestor do IBS. Mostra o status
   modelado: benefício considerado garantido, ou não garantido (com aviso de
   risco de incidência cheia).

Rodapé: fonte da classificação do mix (campo `_fonte_classificacao` das
premissas, ou uma fonte padrão do módulo `farma`) e aviso de que o
CST/cClassTrib deve ser confirmado contra a tabela oficial (NT 2025.002).

### Esqueleto do artefato 02 (Comportamento_Farma.xlsx)

Duas abas, com paleta fixa preto/branco/cinza/amarelo:

- **Aba "Comportamento"**: título com razão social/CNPJ; tabela idêntica à
  seção 2 do MD (Ano, Alíq. efetiva mesclada, Receita, Débito IBS/CBS,
  Crédito IBS/CBS, Posição líquida), com a coluna de alíquota em destaque
  amarelo e formatação percentual/monetária.
- **Aba "Baldes"**: tabela com Balde, Mix, Redução, Efetiva 2027, Efetiva
  2033, CST, cClassTrib — mesmos dados da seção 1 do MD, em formato de
  planilha.

> **Nota**: a geração do XLSX depende da biblioteca `openpyxl`; se ausente,
> o artefato simplesmente não é gerado (retorna `None`), sem erro fatal —
> isso é regra de negócio, não uma lacuna de leitura.

## Observação sobre o pacote padrão citado na proposta comercial

A tarefa mencionava que o dossiê provavelmente cobre "diagnóstico,
classificação fiscal, projeções, dashboard, treinamento" (linguagem da
proposta comercial). O que o código efetivamente define é a lista de 6
arquivos do pacote padrão (parecer, apresentação, DRE, modelos de NF,
implementação da plataforma) — não há seção de "dashboard" nem "treinamento"
como artefato numerado neste módulo. Se esses itens existem em outro lugar
do processo de entrega (fora de `dossie.py`/`checklist.py`), não foram
cobertos por esta leitura.
