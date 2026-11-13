"""User-facing text (pt-BR). Everything returned to MCP clients is defined here."""

LEGAL_NOTICE = (
    "Texto convertido automaticamente das fontes oficiais (pode conter erros de "
    "conversão/OCR). Não substitui a publicação no Diário Oficial."
)

SERVER_INSTRUCTIONS = """\
Acesso à legislação brasileira do repositório público ctresb/leis (Markdown convertido de fontes oficiais).
Antes de responder perguntas jurídicas, localize a norma (`buscar_norma`) e leia o dispositivo exato
(`ler_artigo`). Cite o texto literalmente, informe o link `fonte` e repasse os `avisos` (norma revogada,
texto não compilado, dispositivo revogado). O texto é conversão automática e não substitui o Diário Oficial.
Apelidos aceitos: CF/constituição, ADCT, CC/código civil, CPC, CP/código penal, CPP, CLT, CDC,
lei do inquilinato, lei dos juizados, CTN, ECA, LGPD e outros (recurso leis://apelidos).
"""

# Reference resolution
UNKNOWN_REFERENCE = (
    "Não entendi a referência {reference!r}. Exemplos: 'Lei 8.245/91', '8245/1991', "
    "'LC 123/2006', 'DL 5.452', 'CDC', 'constituição'."
)
NORM_REQUIRED = "Informe a norma."
NUMBER_REQUIRED = "Informe o número da norma (ex.: '8.245', 'Lei 8.245/91') ou um apelido."
PATH_NOT_INDEXED = "Caminho não encontrado no índice: {path}"
NORM_NOT_FOUND = "Nenhuma norma encontrada para {reference!r}. Use `buscar_norma` para pesquisar."
AMBIGUOUS_REFERENCE = "Referência ambígua {reference!r}: informe o ano (ex.: '{example}'). Opções: {options}"
NO_MATCHING_NORMS = "Nenhuma norma encontrada com esses filtros."
INVALID_SPHERE = "Esfera inválida: {sphere!r}. Use uma de: {options}."
INDEX_MISSING = "Índice não encontrado em {path}. Rode `leis-mcp index` primeiro."
INDEX_PREPARING = (
    "Preparando o índice das normas (primeira execução, leva de 1 a 3 minutos). Tente de novo em instantes."
)
INDEX_FAILED = "Não consegui preparar o índice: {error} Tento de novo daqui a pouco."
SNAPSHOT_FAILED = "Falha ao baixar o índice pronto de {url}: {details}"
SNAPSHOT_CORRUPTED = "O índice baixado está corrompido ({details}). Tente de novo mais tarde."
SNAPSHOT_WRITE_FAILED = "Não consegui gravar o índice em {path}: {details}"
INDEX_IN_USE = (
    "Não consegui substituir {path}: o arquivo está em uso. Feche os clientes MCP que usam o leis-mcp e tente de novo."
)
CONTENT_UNAVAILABLE = (
    "Não consegui baixar {path} do GitHub. Verifique a conexão; sem um clone local (`leis-mcp index --from-git`) "
    "não há outra fonte."
)
GIT_FAILED = "Falha ao executar git {command}: {details}"
CLI_ERROR = "erro: {error}"

# Provision lookup
INVALID_ARTICLE = "Número de artigo inválido: {value!r}."
INVALID_PARAGRAPH = "Parágrafo inválido: {value!r}."
INVALID_CLAUSE = "Inciso inválido: {value!r}."
INVALID_SUBCLAUSE = "Alínea inválida: {value!r}."
NO_ARTICLES = "Não encontrei artigos em {path} (formato não reconhecido). Fonte: {source}"
ARTICLE_NOT_FOUND = "Art. {article} não encontrado."
ARTICLE_NOT_IN_BLOCK = "Art. {article} não encontrado no bloco {block!r}."
PARAGRAPH_NOT_FOUND = "{paragraph} não encontrado no Art. {article}."
CLAUSE_NOT_FOUND = "Inciso {clause} não encontrado no Art. {article}{scope}."
CLAUSE_FOUND_IN_PARAGRAPHS = " Existe em: {paragraphs} (informe `paragrafo`)."
SUBCLAUSE_NOT_FOUND = "Alínea {subclause}) não encontrada no Art. {article}."
DUPLICATE_ARTICLE = "Há outro Art. {article} nesta norma em: {others}. Mostrando: {shown}."
BLOCK_REFERENCE = "bloco={index} ({title})"
BLOCK_OPTION = "bloco {index}: {title}"
ARTICLE_SUGGESTION = "Art. {article}"
SUGGESTIONS = " Sugestões: {items}."
IN_NORM = " Norma: {title}."
MAIN_TEXT_BLOCK = "texto principal"
SOLE_PARAGRAPH = "parágrafo único"
ARTICLE_CITATION = "art. {article}"
SUBCLAUSE_CITATION = "alínea {subclause}"

# Front matter defaults for the Constitution, which has no YAML header
CONSTITUTION_KIND = "Constituição"
CONSTITUTION_TEXT_VERSION = "compilada (texto compilado do Planalto)"

# Notices
STRUCK_TEXT = "O trecho contém texto tachado (dispositivo revogado ou alterado) no original."
PROVISION_REVOKED = "ATENÇÃO: este dispositivo está REVOGADO segundo o próprio texto: {note}."
PROVISION_VETOED = "Este dispositivo foi vetado: {note}."
PARTS_REVOKED = "O trecho contém {count} dispositivo(s) marcado(s) como revogado(s) no texto."
NORM_REVOKED = "ATENÇÃO: a norma está marcada como REVOGADA na fonte."
NORM_REVOKED_BY = "ATENÇÃO: a norma está marcada como REVOGADA na fonte ({repealed_by})."
NORM_NOT_IN_FORCE = "ATENÇÃO: a fonte informa que a norma NÃO está em vigor ({fields})."
VALIDITY_CONFLICT = "As fontes divergem sobre a vigência da norma ({fields}): confira na fonte oficial."
SOURCE_STATUS = "Situação informada na fonte: {status}."
VALIDITY_UNKNOWN = "A fonte não informa se a norma está vigente: não presuma que está."
NOT_CONSOLIDATED = "O texto NÃO é a versão compilada/vigente (versao_texto: {version!r}); pode estar desatualizado."
UNKNOWN_VERSION = "A fonte não informa se o texto é a versão compilada (vigente)."

# Validity and wording summaries, per `ValidityState`
VALIDITY_SUMMARIES = {
    "revogada": "A fonte marca a norma como revogada.",
    "sem_vigencia_na_fonte": "A fonte informa que a norma não está em vigor.",
    "vigente_segundo_a_fonte": "A fonte informa que a norma está em vigor.",
    "sem_revogacao_registrada": (
        "A fonte não registra revogação expressa. Isso não confirma vigência: pode haver revogação tácita, "
        "decisão judicial ou norma posterior."
    ),
    "outra": "A fonte informa uma situação específica (veja `situacao` em `campos`).",
    "nao_informada": "A fonte não informa a vigência desta norma. Não presuma que está vigente.",
    "conflitante": "Os campos da fonte divergem sobre a vigência. Confira na fonte oficial.",
}
VALIDITY_ORIGINS = {
    "acervo": "acervo ctresb/leis (cabeçalho e texto da norma)",
}
WORDING_CONSOLIDATED = "Texto compilado (redação vigente na data da captura), não a publicação original."
WORDING_ORIGINAL = "Texto da publicação original: alterações posteriores podem não estar refletidas."
WORDING_UNKNOWN = "A fonte não informa se o texto é compilado ou original."

# Text search and browsing
QUERY_TOO_SHORT = "A consulta precisa ter ao menos {minimum} caracteres."
NORM_SCOPE = "norma {path}"
CACHE_SCOPE = (
    "{count} normas em cache local (a busca não cobre o acervo inteiro; use `norma` para buscar "
    "numa norma específica, que é baixada sob demanda)"
)
BROWSE_HINT = "Ementas aparecem só para normas já em cache; use `buscar_norma` para ver metadados."
