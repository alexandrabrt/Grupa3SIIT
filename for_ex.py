# for variabila_tempora in functie / lista / string:
#     pass
# functie =>> range, enumerate, item
# for i in range(10):
#     print(i)

# range(pas_inceput, pas_final, pasul)
#incepe mereu de la 0 daca nu este specificat pasul de inceput

# for i in range(2, 5):
#     print(i)

# for i in range(3, 7, 2):
#     print(i)

# for i in range(3, 7, -2):
#     print(i)

# for i in range(10, -11, -2):
#     print(i)

# list_a = [1, 2, 3, 4]
# for index, value in enumerate(list_a):
#     print(index, '=>', value)

# a = "Ana are mere"
# print(list(a))
# for i in a:
#     print(i)
import datetime

# a = "Ana are mere"
# print(a[4])
# print(a[-1])
# print(a[1:5])
# print(a[2:])
# print(len(a)) #lungime
# print(a[1:5:2])
# print(a.find('are'))
# cnp = '1234567890123'
# an = cnp[1:3]
# luna = cnp[3:5]
# zi = cnp[5:7]
# print(f"19{an}", luna, zi)
# print(datetime.datetime.strftime())

# x = "mere"
# x[0] = 'p'
# print(x.replace("e", "p"))
# print(y)
# print(x.find("e"))
# a = "ana are mere"
# print(a.split(" "))
# print(a.replace(a[0], "e"))
# a = a.replace(a[0:3], "esdsdsd")
# print(a)
# for i, v in enumerate(x):
#     print(i, v)
#tuple
# a = ("re",)
# print(type(a))
# a = ("a", False, 4, ("tuple", 3), "soare")
# print(type(a))
# y = ("b", 4)
# print(a+y)
# for i in y:
#     print(i)
# print(y[0])
# print()
# y[0] = "a"

#lista
# x = ["a", False, 4, ("tuple", 3), "soare"]
# for i in x:
#     print(i)
# print(x[-1])
# x[0] = "b"
# print(x)
# print(type(list(a)))
# x = ["A", True, '4', ["1", "4", False, True, ["1"], ["7", "b", None]]]
# print(x[3][5][2])
# y = [[123, False, "abc", "e"], ["1"], "a", True, ["7", "cdef"]]
# print(y[2])
# print(y[0][2][1])
# print(y[4][1][3])
# print(str(y[0][0])[2])
# y.append(2)
# print(y)
# y.remove("a")
# y.pop(2)
# y.insert(2, "alo")
# print(y[-1])
# s = {1, 7, 'A', 'a', 3, 4, 5, 5}
# print(s)
# # print(type(s))
# # s.add(6)
# # print(list(s))
# # print(s[1])
# for x in set(s):
#     print(x)

# a = {'a', 'b'}
# a = [1, 2, 3]
# b = [4, 5, 2]
# print(set(b) - set(a))
# s.discard(5)
# print(s)
# x = {1}
# y = {1}
# ord(str(15))
# print(x <= y)
# print(x*3)
# y = "abc"
# print(y*3)

# a = {"3": 3, 1: "abv", "2": [1, 2, 3], (1, 2): "a"}
# if "3" in a:
#     print('da')
# a = {"3": 3,
#      1: "abv",
#      "2": [1, 2, 3],
#      (1, 2): "a",
#      "3": 2}
# for x in a.keys():
#     print(x)
# for x in a.values():
#     print(x)

# for i, v in a.items():
    # print(i, '=>', v)
    # print(a[i])

# print(a[1])
# print(a)
# a["2"] = "abc"
# print(a)
# a = {"4": 2}
# print(a)
# a[2] = "fff"
# print(a)

# b = [1, 2, 3]
# if 4 in b:
#     print('da')

# i = 10
# while i > 0:
#     print(i)
#     i -= 1
#
for i in range(10, 0, -1):
    print(i)

