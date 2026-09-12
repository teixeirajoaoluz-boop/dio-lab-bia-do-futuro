# Tabela `ncm_tributacao_rtc`

Fonte da estrutura: `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\07_criar_tabela_ncm_tributacao_rtc.sql`.
Fonte de população: `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\13_popular_ncm_tributacao_rtc.py`.
Fonte de consulta de exemplo: `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\consultar_anexo14_ncm.py`.
Fonte de verificação: `c:\Projetos Tecnologicos\02_Guerra RTC\backend\base_sql\verificar_ncm_populado.py`.

## Propósito

Tabela de classificação tributária por NCM/NBS para o IBS/CBS, existente em dois
schemas paralelos: `rtc_poc` (ambiente de prova de conceito) e `rtc_prod`
(produção). O schema legado `projetobef` está descontinuado — a tabela só é criada
e populada nesses dois schemas ativos.

## Estrutura de campos

| Campo | Tipo | Propósito |
|---|---|---|
| `id` | VARCHAR(255), PK | Identificador único do registro. Gerado na carga como `ncm_<NCM>_<sufixo hex aleatório>` — não é um ID estável/determinístico por NCM. |
| `ncm_nbs` | VARCHAR(20), obrigatório | O código NCM (produto) ou NBS (serviço) classificado. Campo de busca principal. |
| `cst` | VARCHAR(10) | Código de Situação Tributária do IBS/CBS aplicável a esse NCM/NBS. |
| `cclass_trib` | VARCHAR(20) | Código de Classificação Tributária — desambigua a hipótese específica de tratamento dentro do CST (qual regra/anexo fundamenta o benefício). |
| `descricao_reduzida` | TEXT | Descrição textual curta do item/categoria, para leitura humana. |
| `reducao_ibs` | NUMERIC(5,2) | Percentual de redução da alíquota de IBS aplicável a esse NCM (0 = sem redução). |
| `reducao_cbs` | NUMERIC(5,2) | Percentual de redução da alíquota de CBS aplicável a esse NCM (0 = sem redução). |
| `anexo` | VARCHAR(10) | Qual anexo da LC 214/2025 fundamenta o tratamento diferenciado (ex.: `14` para medicamentos, art. 146). |
| `tipo` | VARCHAR(10) | Campo de categorização adicional do item (o significado dos valores possíveis não está documentado nos scripts lidos — vem do CSV fonte). |
| `legislacao` | TEXT | Referência textual ao dispositivo legal que ampara a classificação. |
| `hiperlink` | TEXT | Link de referência (provavelmente para a norma ou tabela oficial). |
| `createdAt` / `updatedAt` | TIMESTAMP | Auditoria de carga (preenchidos com o timestamp da execução do script de importação, iguais entre si na carga inicial). |

## Como a tabela é populada (regra de ETL, não regra tributária)

1. **Fonte de dados**: CSV `CAD_NCM_CST_CCLASSTRIB.csv`, localizado em
   `01_api_participantes/DADOS BASE/` na raiz do projeto — arquivo externo ao
   código, não lido nesta tarefa (é dado tabular, não regra de código).
2. **Leitura**: delimitador `;`, com detecção automática de encoding tentando, nesta
   ordem, `utf-8-sig`, `utf-8`, `latin-1`, `cp1252`, `iso-8859-1`.
3. **Colunas do CSV mapeadas para a tabela**: `NCM/NBS`, `CST`, `CClassTrib`,
   `Descrição Reduzida`, `Redução IBS`, `Redução CBS` (convertidos de string com
   vírgula decimal para float; vazio vira `0.0`), `Anexo`, `TIPO`, `Legislação`,
   `Hiperlink`.
4. **Validação mínima**: linhas com `NCM/NBS` vazio são descartadas e reportadas
   como erro de linha; não há outra validação de regra de negócio no script (não
   valida, por exemplo, se `cst`/`cclass_trib` são valores permitidos).
5. **Carga**: a tabela é esvaziada (`DELETE FROM`, mediante confirmação interativa
   do operador) e os registros são inseridos em lotes de 500, nos dois schemas
   (`rtc_poc` e `rtc_prod`) na mesma execução.
6. **Volume esperado**: conforme o script de verificação, o volume de referência é
   de **~3.487 registros** (linhas do CSV fonte).

## Consulta de exemplo documentada no repositório (Anexo 14)

O único uso de consulta com regra de negócio explícita encontrado
(`consultar_anexo14_ncm.py`) filtra `anexo = '14'` (ou `'14.0'`) e agrupa por
combinação de `reducao_ibs`/`reducao_cbs`, contando registros e NCMs distintos. A
conclusão fixada no próprio script identifica o Anexo 14 como **"Fornecimento de
medicamentos" — LC 214/2025, art. 146**. Isso confirma, a partir da tabela genérica
de NCM, o mesmo fundamento legal (art. 146) usado como base do balde
`medicamento_zero`/`medicamento_60` no módulo farma (ver `README.md`, seção 2) —
ainda que os dois mecanismos (tabela `ncm_tributacao_rtc` vs. motor `farma.py`) sejam
independentes no código.

## Lacunas

- O significado dos valores possíveis do campo `tipo` não está documentado em
  nenhum script lido — só existe como passagem direta do CSV fonte.
- O conteúdo real do CSV (quais NCMs específicos recebem quais CST/cClassTrib/
  reduções) não foi extraído nesta tarefa — está fora do escopo de "código-fonte"
  pedido e não foi fornecido como arquivo a ler.
- Não há, nos scripts lidos, nenhuma função que **decida** cst/cclass_trib a partir
  de regras (ex.: um NCM novo, sem entrada no CSV, não tem fallback algorítmico) —
  a tabela é puramente uma cópia estática do CSV curado externamente.
