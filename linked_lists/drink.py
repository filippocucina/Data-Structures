class Drink:
    def __init__(self, name):
        self.__name = name

        #self._name = name, encapsula atributos de las claes
        #es el equivalente a " Protected " en Java, C++, JavaScript, C# ect
        
        #self.__apellido = " __ " encapsula atributos de las clases,
        #El equivalente a " private " en Java, C++, JavaScript, C# ect
        #Solo puede ser usado por la misma clase, si se usa private

    def getDetail(self):
        return "La bebida es: " + self.__name


#Herencia, nos permite reutilizar codigo, sin necesidad de reescribir metodos.
#Para poder Heredar de una clase Padre, debemos pasarlo como parametro a la
#clase hija.

class Beer(Drink):
    def __init__(self, name, brand, alcohol):
        super().__init__(name)
        self.__brand = brand
        self.__alcohol = alcohol

    def getDetail(self):
        return super().getDetail() + " de la marca" + self.__brand + "con alcohol " + str(self.__alcohol)
    
    #Esto es polimorfismo
    #Tambien podriamos reutilizar exactamente lo del padre,
    #usando super().getDetail()


bebida1 = Drink("Agua")
print(bebida1.getDetail())

beer1 = Beer("Negrita", "Polar", 4.5)
print(beer1.getDetail())
