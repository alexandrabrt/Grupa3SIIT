# lambda argumente: expresie

x = lambda a: a + 10
print(x(2))


def suma(a):
    return a + 10


# dictionar = {"Task": "",
#                  "Deadline": "",
#                  "Responsabil": "",
#                  "Categorie": ""}


# def ordonare_lambda(cheia_de_ordonare: str = "Categorie"):
#     key = lambda i: i[cheia_de_ordonare]
#     return key
# # sorted(orice_lista_dictionare, key=lambda i: i[cheia_de_ordonare], reverse=tip_de_ordonare)
#
# ordonare_lambda("Task")

# y = []
# for x in range(10):
#     y.append(x ** 2)
# y = [x**2 for x in range(10)]
# print(y)
S = [0, 1, 2, 0, 3, 4, 0, 5, 6]
# z = []
# for x in S:
#     if x % 2 == 0:
#         z.append(x)
z = [x for x in S if x % 2 == 0]
#mai mare decat 0 si mai mic decat 2
print(z)
x = 2
print('citesc' if x == 1 else 'scriu')

feet = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
# print([x+1 if x >= 120000 else x+5 for x in feet])

list_of_list = [[1, 2, 3],[4, 5, 6],[7, 8]]
# print([y for x in list_of_list for y in x])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([[row[i] for row in matrix] for i in range(3)])
y = []
for i in range(3):
    for row in matrix:
        y.append(row[i])





