class Address:
    def __init__(self, street: str, number: int, zip_code: str, complement: str):
        if number is not None and number < 0:
            raise ValueError("Número inválido")

