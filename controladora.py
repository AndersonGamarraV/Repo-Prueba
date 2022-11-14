class Controladora:
    def __init__(self) -> None:
        self.__time = 0.0
        self.__entidades = 0
        self.__items = 0
    
    @property
    def time(self) -> float:
        return self.__time
    
    @property
    def entidades(self) -> int:
        return self.__entidades
    
    @property
    def items(self)->int:
        return self.__items