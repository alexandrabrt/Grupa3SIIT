import datetime

categorii = []
lista_dictionare = []


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD HH:MM")
        return False


def adaugare_categorii(nume_categorie: str):
    if nume_categorie not in categorii:
        return categorii.append(nume_categorie)


def creare_dictionare() -> list:
    dictionar = {"Task": "",
                 "Deadline": "",
                 "Persoana responsabila": "",
                 "Categorie": ""}
    task = input("Va rog sa introduceti un task: ")
    dictionar["Task"] = task
    while True:
        deadline = input("Va rog sa introduceti un deadline in formatul YYYY-MM-DD HH:MM: ")
        if validate(deadline):
            dictionar["Deadline"] = deadline
            break
    persoana_responsabila = input("Va rog sa introduceti o persoana responsabila: ")
    dictionar["Persoana responsabila"] = persoana_responsabila
    print(f"Categorii disponibile: {categorii}")
    categorie = input("Va rog sa introduceti o categorie: ")
    if categorie in categorii:
        dictionar["Categorie"] = categorie
    while categorie not in categorii:
        print("Categorie inexistenta.")
        categorie = input("Va rog sa introduceti o categorie din lista de categorii: ")
        dictionar["Categorie"] = categorie
    lista_dictionare.append(dictionar)
    return lista_dictionare


def ciclu_adaugare_categorii() -> list:
    loop_categorii = False
    while not loop_categorii:
        adaugare_categorii(input("Va rog sa introduceti o categorie: "))
        a = input("Doriti sa introduceti o alta categorie? y/n ")
        # print(categorii)
        if a == "n":
            loop_categorii = True
    return categorii


def ciclu_lista_de_dictionare() -> list:
    loop_creare_dictionare = False
    lista_noua_dictionare = []
    while not loop_creare_dictionare:
        lista_noua_dictionare = creare_dictionare()
        b = input("Doriti sa introduceti un alt task? y/n ")
        if b == "n":
            loop_creare_dictionare = True
    return lista_noua_dictionare


def ordonare_lambda(orice_lista_dictionare: list, cheia_de_ordonare: str = "Categorie", tip_de_ordonare: bool = False) -> list:
    return sorted(orice_lista_dictionare, key=lambda i: i[cheia_de_ordonare], reverse=tip_de_ordonare)


def afisare_date(lista_dictionare: list):
    variabila, antet, chei = "", "", []
    for dictionar_de_iterat in lista_dictionare:
        chei = dictionar_de_iterat.keys()
        for valori in list(dictionar_de_iterat.values()):
            variabila += f"{valori} \t"
        variabila += '\n'
    for iterator_cheie in list(chei):
        antet += f"{iterator_cheie} \t"
    print(f"{antet} \n {variabila}")
    return f"{antet} \n {variabila}"


def alegere_afisare(orice_lista_de_dictionare: list):
    cheie_locala = ""
    directia_sortarii_locala = ""
    while True:
        criteriul = input("Lista criterii: \n Task \n Deadline \n Persoana responsabila \n Categorie \n Alegeti criteriul de sortare: ")
        if criteriul.upper() == "TASK":
            cheie_locala = "Task"
            break
        elif criteriul.upper() == "DEADLINE":
            cheie_locala = "Deadline"
            break
        elif criteriul.upper() == "Persoana responsabila".upper():
            cheie_locala = "Persoana responsabila"
            break
        elif criteriul.upper() == "Categorie".upper():
            cheie_locala = "Categorie"
            break
        else:
            print("Valoare incorecta. Alegeti din lista: \n Task \n Deadline \n Persoana responsabila \n Categorie")
    while True:
        criteriul = input(
            "Directia sortarii: \n Ascendent \n Descendent \n Alegeti directia de sortare: ")
        if criteriul.upper() == "ascendent".upper():
            directia_sortarii_locala = False
            break
        elif criteriul.upper() == "descendent".upper():
            directia_sortarii_locala = True
            break
        else:
            print("Valoare incorecta. Alegeti din lista: \n Ascendent \n Descendent")
    afisare_date(ordonare_lambda(orice_lista_de_dictionare, cheie_locala, directia_sortarii_locala))


def main():
    categorii = ciclu_adaugare_categorii()
    lista_dictionare = ciclu_lista_de_dictionare()
    #De afisat pct 2
    alegere_afisare(lista_dictionare)

main()

#2020-12-12 12:12