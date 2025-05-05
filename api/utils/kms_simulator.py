import base64


class kms_simulator():
    """
    Uma classe para simular o comportamento de decriptação do Key Management Service
    no GCP.

    Será utilizada apenas descriptação de base 64 bits. Não serão abordados métodos de autenticação
    da service_account, key_ring e outras funcionalidades do GCP.
    """

    def decrypt_text(text: str):
        
        # Decodifica para bytes
        decoded_bytes = base64.b64decode(text)
        # Converte bytes para string
        decoded_str = decoded_bytes.decode("utf-8")
        return decoded_str