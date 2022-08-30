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


#Algo que es muy cool de Python es que tiene Multi Herencia, en otros lenguajes
#De Programacion la herencia multiple no existe, es decir, que yo pueda
#Heredar de 2 Elementos

class Product:

    def __init__(self, cost, price):
        self.cost = cost
        self.price = price

    def getGain(self):
        return self.price - self.cost


class Beer(Drink, Product):
    
    #En la programacion Orientada a Objetos tenemos algo llamado un Elemento Estatico
    #Un Elemento Estatico pertenece a la Clase y no al Objeto
    #Es una forma de centralizar informacion

    Count = 0   #Elemento Estatico
    
    
    def __init__(self, name, brand, alcohol, cost, price):
        #super().__init__(name)    -  Herencia, pero vamos hacer Herencia Multiple
        Drink.__init__(self, name) #Cuando Invocamos los Padres y ahora sin la
                                   #Palabra super(), tenemos que mandar al self
        Product.__init__(self, cost, price) #Herencia Multiple
        self.__brand = brand
        self.__alcohol = alcohol
        Beer.Count += 1
    
    #Por ultimo, Python permite tambien tener atributos que son Opcionales. Ej:
    #text = ""
    def getDetail(self, text = ""):
        return text + super().getDetail() + " de la marca" + self.__brand + "con alcohol " + str(self.__alcohol)
    
    #Esto es polimorfismo
    #Tambien podriamos reutilizar exactamente lo del padre,
    #usando super().getDetail()
    
    #Tambien se puede crear Metodos Estaticos
    @staticmethod
    def getClassInfo():
        return "Se ha creado " + str(Beer.Count) + " objetos"

    #Tambien hay Clase Estatica usando:
    #@classmethod

bebida1 = Drink("Agua")
print(bebida1.getDetail())

beer1 = Beer("Negrita", "Polar", 4.5, 10, 20)
print(beer1.getDetail())
print(beer1.getGain())
print(beer1.getDetail("Info: ")) #Parametros Opcionales

beer2 = Beer("Verde", "Polar", 4.5, 7, 14)
print(beer2.getDetail())
print(beer2.getGain())

print(Beer.Count)
print(Beer.Count)
print(Beer.getClassInfo())
print("\n")


for i in range(0,3):
    print(Beer.Count)

