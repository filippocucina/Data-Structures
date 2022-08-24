class drink:
    def __init__(self, name):
        self.__name = name
        ##self.__apellido = " __ " encapsula atributos de las clases,
        ##El equivalente a " private " en Java

    def getDetail(self):
        return "La bebida es: " + self.__name

    

bebida1 = drink("Agua")
print(bebida1.getDetail())
