from src.loja.dtos.address import AddressDTO
from src.loja.models.address import Address


class AddressConverter:
    def convert(self, form: AddressDTO) -> Address:
        return Address(form.street, form.number, form.zip_code, form.complement)
