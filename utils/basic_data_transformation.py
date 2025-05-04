import re

def normalize_column_names(columns):
    """
    Essa função realiza a normalização dos nomes das colunas de forma dinâmica, independentemente do dataframe repassado.
    """
    normalized = []
    for col in columns:
        # 1. Substitui '24Hr' ou variações por '_24hr'
        col = re.sub(r'24[Hh][Rr]', '_24hr', col)
        # 2. Insere '_' antes de letras maiúsculas (exceto no começo)
        col = re.sub(r'(?<!^)(?=[A-Z])', '_', col)
        # 3. Converte tudo para minúsculo
        col = col.lower()
        normalized.append(col)
    return normalized