class Customer:

    def __init__(self, name: str, social_number: str):
        self.__name = name
        self.__social_number = social_number

    @property
    def name(self) -> str:
        return self.__name

    @property
    def social_number(self) -> str:
        return self.__social_number

