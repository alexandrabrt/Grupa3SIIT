# def add(x, y):
#     return x + y
#
#
# print(add(2, 3))


# def functia_mea(*args):
#     return args


# print(functia_mea(1, 2, 3, 4, 5))
# print(type(functia_mea(1, 2, 3, 4, 5)))
# print(functia_mea('a', 'b', [1, 2, 3, 4]))


# address = ("Bucuresti", 56, 'Cluj', 'ilfov', 'Romania')
# street, *rest = address
# print(street)
# print(rest)

# def functie_kwargs(**kwargs):
#     for x, y in kwargs.items():
#         print(x, y)
#     return kwargs


# print(functie_kwargs(city='Bucuresti', street='Pipera'))
# print(type(functie_kwargs(city='Bucuresti', street='Pipera')))

# def my_func(*args, **kwargs):
#     arguments = {
#         'args': args,
#         'kwargs': kwargs
#     }
#     return arguments


# print(my_func(1, 2, 3, 4, 5, city='Cluj', street='Strada Unirii'))
# print(my_func(city='Cluj'))
# print(my_func(city='Cluj', street='Unirii'))

# def my_function(any_number, other_number, *args, city='Cluj', **kwargs):
#     arguments = {
#         'args': args,
#         'kwargs': kwargs
#     }
#     return arguments

# print(my_function(1000, 2000, 44, 55, 66, city='Cluj', country='Romania'))
# print(my_function(1000, 2000, 44, 55, 66, country='Romania'))
# print(my_function(1000, 2000, 44, 55, 66, country='Romania'))


# var = None
#
#
# def myFunction():
#     global var
#     var = 20
#     return True
#
#
# var = 10
# print(var)
# myFunction()
# print(var)

def sum(x, y):
    return x / y

# suma = 0
#
# try:
#     # qqq
#     suma = sum(2, 0)
#     print('Hello')
# except ValueError:
#     print('value error')
# except ZeroDivisionError:
#     print('impartire la 0')
# except Exception as e:
#     print('exceptie', e)
# else:
#     print('nimic')
# finally:
#     print('final')

# if suma == 4:
#     print('succes')


class ExceptionIsDigit(Exception):

    def _init_(self, message):
        self.message = message

    def _str_(self):
        return self.message


class ExceptionFor3Characters(Exception):

    def _init_(self, message):
        self.message = message

    def _str_(self):
        return self.message


try:
    input1 = input('Numele utilizatorului: ')
    if input1.isdigit() is False:
        raise ExceptionIsDigit
    if len(input1) != 3:
        raise ExceptionFor3Characters
except ExceptionFor3Characters:
    print('Aloca doar 3 caractere in input')
    input1 = input('Numele utilizatorului: ')
except ExceptionIsDigit:
    print('nu este string')
    print(input1)
except Exception as e:
    print(e, '<<>>')
finally:
    print(input1)





