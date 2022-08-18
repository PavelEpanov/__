# class C1:
#     def meth1(self):
#         self.X = 88 # Я предпогалаю, что атрибут X мой
#     def meth2(self):
#         print(self.X)
# class C2:
#     def meth1(self):
#         self.X = 99 # Я тоже
#     def meth2(self):
#         print(self.X)
#
# class C3(C1, C2):
#     pass
#
# I = C3() # В I есть только один атрибут X
class C1:
    def meth1(self): # Теперь я имею свой атрибут X
        self.__X = 88 # Становится _C1__X в I
    def meth2(self):
        print(self.__X)
class C2:
    def metha(self): # Теперь я имею свой атрибут X
        self.__X = 99 # Становится _C2__X в I
    def methb(self):
        print(self.__X)

class C3(C1, C2):
    def __init__(self):
        self.X = 100
        print(self.X)


I = C3() # В I есть 2 имени X
print(I.__dict__)
I.meth1(), I.metha()
print(I.__dict__)
I.meth2()
I.methb()