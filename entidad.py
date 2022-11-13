class Entidad:
    def __init__(self) -> None:
        self.__ancho = 0
        self.__alto = 0
    
    @property
    def ancho(self):
        return self.__ancho;
    
    @property
    def alto(self):
        return self.__alto;