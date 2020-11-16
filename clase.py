# Tipuri animale: => clasa, restul subclase
# - mamifere
# - reptile
# - pasari
# - amfibieni

# orice obiect poate sa contina 3 grupuri de atribute:
# 1. un obiect are un nume care
# 2. set de proprietati individuale care il fac original  si unic (unele pot sa nu aiba)
# 3. set de abilitati pentru realizarea unei activitati specifice

# ex:
# Tom este o pisica mare care doarme toata ziua.
# Tom - object name
# pisica - clasa
# mare - proprietate
# doarme (toata ziua) - activitate


# deci: object name -> substantiv -> tom
#         proprietatea -> adjectiv -> marime (mare)
#         activitatatea -> verb -> doarme


class FirstClass(object):
    pass


# keyword: class
# class name: First Class
# class parent: object (nu e obligatoriu)
# pass-> indentarea

new_object = FirstClass()  # actiunea de adaugare a creare nou obiect se numeste instantiere, obiectul se numeste instanta a clasei

# exercitiu stiva
# stack = []


# def push(val):
#     stack.append(val)
#
#
# def pop():
#     val = stack[-1]
#     print(stack)
#     del stack[-1]
#     return val

# push(3)
# push(2)
# push(1)
#
# print(pop())
# print(pop())
# print(pop())


# class Stack:    # defining the Stack class
#     def __init__(self):    # defining the constructor function
#         print("Hi!")
#
#
# stackObject = Stack()    # instantiating the object
# stackObject2 = Stack()    # instantiating the object

# constructorul, adica initul practic se apeleaza de fiecare data cand se adauga un nou obiect

#
# class Stack:
#     def __init__(self):
#         self.stackList = []
#
#
# stackObject = Stack()
# print(len(stackObject.stackList))


# class Stack:
#     def __init__(self):
#         self.__stackList = [] ##invalideaza programul pentru ca devinde prival
#
# stackObject = Stack()
# print(len(stackObject.__stackList))


# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
#
# stackObject = Stack()
#
# stackObject.push(3)
# stackObject.push(2)
# stackObject.push(1)
#
# print(stackObject.pop())
# print(stackObject.pop())
# print(stackObject.pop())


# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
#
# stackObject1 = Stack()
# stackObject2 = Stack()
#
# stackObject1.push(3)
# stackObject2.push(stackObject1.pop())
#
# print(stackObject2.pop())


users = [
    {'name': 'John Doe', 'age': 19},
    {'name': 'Jack Fluffy', 'age': 22},
    {'name': 'Matthew Wu', 'age': 43},
    {'name': 'Heather Rafferty', 'age': 15},
    {'name': 'Randall Blackdall', 'age': 76},
    {'name': 'Marissa Raynaud', 'age': 34},
    {'name': 'Marlo Ranbot', 'age': 49},
]


class User(object):
    company = 'Py Future inc.'

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def este_major(self):
        return self.age >= 18

    def __str__(self):
        return f"Nume {self.first_name} {self.last_name} si varsta {self.age}"


matei = User('Matei', 'Barbu', 19)
print(f"{matei}")

users_object = []
for user in users:
    users_object.append(
        User(user['name'].split()[0],
             user['name'].split()[1],
             user['age'])
    )

for item in users_object:
    print(item)
