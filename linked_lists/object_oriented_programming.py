class MyClass:
    def method(self):
        #print("Instance Method Called", self)
        return "Instance Method Called", self

    
    @classmethod
    def classmethod(cls):
        return "Class Method Called", cls


    @staticmethod
    def staticmethod():
        return "Static Method Called"

#Instancia Objeto de la Clase
obj2 = MyClass()
obj = MyClass()
print(obj.method())
print("\n", MyClass.method(obj2))

#Instancia para el @classmethod
objeto = MyClass()
objeto.classmethod()
print("\n", objeto.classmethod())

#Instancia para usar el @staticmethod
objeto2 = MyClass()
objeto2.staticmethod()
print("\n", objeto2.staticmethod())
