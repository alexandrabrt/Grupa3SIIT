# a = '123.12 b:'
# print(''.join(x for x in a if x.isdigit()))
# b = ''
# for x in a:
#     if x.isdigit():
#         b += ''.join((x))
# print(float(b))
#
# print(float(12.345, 2))

# animale: - clasa
# - mamifere
# - reptile
# - pasari

# Tom este o pisica mare care doarme toata ziua:
# - obiectul (Substantiv) - Tom
# - clasa (substantiv) - pisica
# - proprietatea (adjectiv) - mare
# - activitatea (verb) - doarme (toata ziua)


# Mazda este o masina frumoasa care merge toata ziua.
# - obiectul - Mazda
# - clasa - masina
# - proprietatea - frumoasa
# - activitatea - merge (toata ziua)
#
# class PrimaClasa(object):
#     pass

# keyword: class
# class name: Prima class
# class parent: object (nu e obligatoriu)
# corpul clasei: pass

#
# class Masina:
#     pass
#
#
# mazda = Masina() # actiunea de adaugare a unui obiect se numeste istantiere, obiectul este instanta al clasei
# bmw = Masina()


# 1 2 3 4 5 LIFO
# stiva LIFO - last in first out
# coada FIFO - first in first out

# stiva = []
# def push(val):
#     stiva.append(val)
# def pop():
#     val = stiva[-1]
#     print(val)
#     del stiva[-1]
#     return val
# push(3)
# push(2)
# push(1)
#
# print(pop())
# print(pop())
# print(pop())
#
# class Stiva:
#     def __init__(self):
#         self.__lista_stiva = []
#         # print('un nou obiect')
#
#     def push(self, val):
#         self.__lista_stiva.append(val)
#
#     def pop(self):
#         val = self.__lista_stiva[-1]
#         del self.__lista_stiva[-1]
#         return val
#
#
# obiect1_stiva = Stiva()
# # print(len(obiect1_stiva.lista_stiva))
# # obiect2_stiva = Stiva()
# obiect1_stiva.push(3)
# obiect1_stiva.push(2)
# obiect1_stiva.push(1)
#
# print(obiect1_stiva.pop())
# print(obiect1_stiva.pop())
# print(obiect1_stiva.pop())

# customer = 'AAA'


# class User:
#
#     company = 'SIIT'
#
#     def __init__(self, first_name='Matei', last_name='Barbu', age=20):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def este_major(self):
#         return self.age >= 18
#
#     def __str__(self):
#         return f"Nume: {self.first_name} {self.last_name} \nVarsta: {self.age}\nCompania: {self.company}"
#
#     def user_description(self):
#         return f"Utilizator {self.first_name} {self.last_name} {self.company} {customer}"

#
# class Student(User):
#
#     location = 'general'

    # def __init__(self, first_name, last_name, age, courses):
    #     self.courses = courses
    #     super(Student, self).__init__(first_name, last_name, age)

    # def este_inrolat(self, courses):
    #     return courses in self.courses
    #
    # def este_major(self):
    #     return self.age >= 21

    # def __str__(self):
    #     return f"{self.first_name}"


# matei = Student('ovidiu', 'Oprescu', 21)
# print(matei)
# print(f"{matei}")
# print(f"{matei.este_major()}")

# users = [
#     {'name': 'John SMIth', 'age': 19},
#     {'name': 'John1 SMIth', 'age': 20},
#     {'name': 'John2 SMIth', 'age': 21},
#     {'name': 'John3 SMIth', 'age': 17},
#     {'name': 'John4 SMIth', 'age': 18},
#     {'name': 'John5 SMIth', 'age': 21},
# ]

# users_object = []
# for user in users:
#     users_object.append(
#         User(user['name'].split()[0], user['name'].split()[1], user['age'])
#     )
#
# # print(users_object)
#
# for item in users_object:
#     print(item)


# class Clasa1:
#     def __init__(self, val=1):
#         self.__first = val
#         self.__second = None
#
#     def sec_method(self, val=2):
#         self.__second = val
#
#
# obiect1 = Clasa1()
# obiect2 = Clasa1(2)
#
# obiect2.sec_method(3)
#
# obiect3 = Clasa1(4)
# obiect3.__third = 5
#
# print(obiect1.__dict__)
# print(obiect2.__dict__)
# print(obiect3.__dict__)

# class Clasa1:
#
#     attr = 1
#
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#             self.b = 2
#         else:
#             self.a = 0
#             self.b = 1
#
#     def method(self):
#         return 'method'


# obiect1 = Clasa1(1)
# print(obiect1.a)
# print(obiect1.b)
# print(hasattr(Clasa1, 'attr'))
# print(hasattr(Clasa1, 'prop'))
# print(obiect1.method())

# class Clasa1:
#
#     varia = 1
#
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass

    # def metoda1(self):
    #     print('metoda 1')
    #
    # def metoda2(self):
    #     print('metoda 2')
    #     self.metoda1()


# obj = Clasa1()
# print(obj.__dict__)
# print(Clasa1.__dict__)
# obj = Clasa1()
# print(Clasa1.__dict__)


# class ExampleClass:
#     attrx = 1
#     propxs = 3
#
#
# print(hasattr(ExampleClass, 'attrx'))
# print(hasattr(ExampleClass, 'propxs'))


# class Classy:
#
#     variabila = 2
#
#     def method_new(self, parametru):
#         print('metoda', parametru, self.variabila, x.var)
#
#
# x = Classy()
# x.var = 3
# x.method_new(1)
# x.method_new(2)
# x.method_new(3)


# class Classy:
#
#     def __init__(self, value='222'):
#         # pass
#         self.var = value
#
#     def __str__(self):
#         return self.var
#
#
# obj1 = Classy("object")
# print(obj1)
# print(obj1.var)


# class Classy:
#
#     def visible(self):
#         print('visible')
#
#     def __hidden(self):
#         print('hidden')
#
#
# obj1 = Classy()
# # obj1.visible()
# # obj1.__hidden()
#
# try:
#     obj1.__hidden()
# except Exception:
#     print('failed')
#
#
# obj1._Classy__hidden()
# obj1.visible()

#
# class Classy:
#
#     variabila = 1
#
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass
#
#
# obj1 = Classy()
# # print(obj1.__dict__)
# # print(Classy.__dict__)
# # print(Classy.__name__)
# print(type(obj1).__name__)


# class SuperOne:
#     pass
#
#
# class SuperTwo:
#     pass
#
#
# class SuperThree(SuperOne, SuperTwo):
#     pass
#
#
# def print_bases(cls):
#     for x in cls.__bases__:
#         print(x.__name__)
#     return True
#
#
# print_bases(SuperOne)
# print_bases(SuperTwo)
# print_bases(SuperThree)


# class Star:
#
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#     def __str__(self):
#         return f"{self.name} {self.galaxy}"
#
#
# sun = Star("Sun", "Milky Way")
# print(sun)


# class Vehicule:
#     pass
#
#
# class VehiculeHibride(Vehicule):
#     pass
#
#
# class VehiculeElectrice(VehiculeHibride):
#     pass
#
#
# vehicule_obj = Vehicule()
# vehicule_hibride_obj = VehiculeHibride()
# vehicule_electrice_obj = VehiculeElectrice()

# for cls1 in [Vehicule, VehiculeHibride, VehiculeElectrice]:
#     for cls2 in [Vehicule, VehiculeHibride, VehiculeElectrice]:
#         print(cls1.__name__, cls2.__name__)
#         print(issubclass(cls1, cls2), end='\t')
#     print()

# print(issubclass(VehiculeElectrice, Vehicule))
# print(isinstance(vehicule_hibride_obj, Vehicule))


# class Classy:
#     def __init__(self, val):
#         self.var = val
#
#
# obj1 = Classy(0)
# obj2 = Classy(2)
# obj3 = obj1

# print(obj1 is obj2)
# print(obj2 is obj3)
# print(obj3 is obj1)

# str1 = 'Ana are mere '
# str2 = 'Ana are mere si pere'
# str1 += 'si pere'

# print(str1 == str2)
# print(str1 is str2)


# int1 = 1.0
# int2 = 2.0
# int1 += 1.0
#
# print(int1 == int2)
# print(int1 is int2)


# class SuperClass:
#     super_variabila = 1
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class SubClass(SuperClass):
#     sub_variabila = 2
#     # super_variabila = 3
#
#     def __init__(self, name, varsta=11):
#         self.varsta = varsta
#         # SuperClass.__init__(self, name)
#         super().__init__(name)
#
#     def __str__(self):
#         return f"Ma numesc"
#
#
# obj = SubClass('Ovidiu')
# print(obj.super_variabila)
# obj1 = SuperClass('Popescu')


class SuperClass:
    def __init__(self):
        self.super_variabila = 11
    def metoda1(self):
        return 'superclass'
class MiddleClass(SuperClass):
    def __init__(self):
        super().__init__()
        self.super_variabila = 13
        # print(self.super_variabila)
class SubClass(MiddleClass):
    def __init__(self):
        super().__init__()
        # super(SubClass, self).__init__()
        self.sub_variabila = 12
        self.super_variabila = 40
        # print(self.super_variabila)

        # self.super_variabila = 111
    def metoda1(self):
        return 'subclasa'

    def __str__(self):
        return f"{self.metoda1()} 1"
obj = SubClass()
# print(obj.sub_variabila)
print(obj.metoda1())
# print(obj.metoda1())
