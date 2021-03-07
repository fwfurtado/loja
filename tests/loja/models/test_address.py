import pytest
from loja.models.address import Address


class TestAddress:

    def test_address_attribute(self):
        with pytest.raises(ValueError):
            Address("Rua Jose", 0, "05900-000", "casa 9557")
