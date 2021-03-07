from dataclass import dataclass


@dataclass
class AddressDTO:
    street: str
    number: int
    zip_code: str
    complement: str
