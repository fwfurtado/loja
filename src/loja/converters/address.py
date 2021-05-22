from src.loja.dtos.address import AddressDTO
from src.loja.models.address import Address


class AddressConverter:
    @staticmethod
    def convert(form: AddressDTO) -> Address:
        return Address(
            street=form.street,
            number=form.number,
            zip_code=form.zip_code,
            complement=form.complement,
        )
