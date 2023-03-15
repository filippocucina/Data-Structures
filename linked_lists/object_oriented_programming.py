class MyClass:
    def method(self):
        #print("Instance Method Called", self)
        return "Instance Method Called", self

    
    @classmethod
    def classmethod(cls):
        return "Class Method Called", cls


    @staticmethod
    def stactimethod():
        return "Static Method Called"


obj = MyClass()
obj.method()
