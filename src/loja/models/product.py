class Product:

    def __init__(self, name: str, value: float):
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> float:
        return self.__value
    def __str__(self):
        return f"Product({self.name,self.value})"