from random import randint
import random
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

LIST_OF_CITIES = [[0, 1, 2, 3, 4, 5], [1, 0, 6, 7, 8, 9], [2, 6, 0, 10, 11, 12], [3, 7, 10, 0, 13, 14], [4, 8, 11, 13, 0, 15], [5, 9, 12, 14, 15, 0]]
NUM_OF_CITIES = len(LIST_OF_CITIES)
NUM_OF_PEOPLE = 3
POCET_ITERACI = 20
people = []


def people_generating():
    for n in range(NUM_OF_PEOPLE):
        numbers = []
        person = []
        cities = []
        for n1 in range(1, NUM_OF_CITIES + 1):
            numbers.append(n1)

        for n2 in range(1, NUM_OF_CITIES + 1):
            n3 = randint(0, NUM_OF_CITIES - n2)
            cities.append(numbers.pop(n3))
        person.append(cities)
        people.append(person)
    print("tady jsou lidi", people)
    return (people)



def value(people, LIST_OF_CITIES):
    for m in range(NUM_OF_PEOPLE):
        quality = 0
        for m1 in range(NUM_OF_CITIES - 1):
            quality = quality + LIST_OF_CITIES[people[m][0][m1] - 1][people[m][0][m1 + 1] - 1]
        people[m].insert(0, quality)
    print("tady se jim přidá kvalita", people)
    return(people)



def quality_sorting(people):
    sorted_people = sorted(people)
    people.clear()
    people.extend(sorted_people)
    print("serazeni podle kvality", people)
    return people



def selection(people, NUM_OF_PEOPLE):
    people_selection = []
    for element in range(len(people)):
        multipation = NUM_OF_PEOPLE - element
        index = 0
        while index < multipation :
            people_selection.append(people[element])
            index = index + 1
    print("tady se to vynásobí", people_selection)
    people.clear()
    people.extend(people_selection)
    print(people)
    return people


def odstraneni_kvality(people):
    print(len(people))
    n = 0
    for nn in range (0, NUM_OF_PEOPLE):
        print(n)
        del people[n][0]
        print(people)
        n = n + NUM_OF_PEOPLE - nn
    return people


def selection_final(people_selection):
    zuzeni_populace = []
    delka = NUM_OF_PEOPLE
    n = 0
    zuzeni_populace = []
    for x in range(NUM_OF_PEOPLE) :
        zuzeni_populace.append([])
    print("funguje zavorka?", zuzeni_populace)

    while n < delka:
        random_index = randint(0, len(people_selection) - 1)
        random_clovek = list(people_selection[random_index])
        zuzeni_populace[n] = list(random_clovek[0])
        n += 1
    print("tady se pocet zmensi", zuzeni_populace)
    return zuzeni_populace


def mutace(new_selection):
    print("DOLE JE FUNKCE MUTACE")
    print("tohle vstupuje do mutace", new_selection)
    mutace_jedinec = new_selection.pop(randint(0, NUM_OF_PEOPLE - 1))
    print("tohle je zmutovany jedinec PRED MUTACI", mutace_jedinec)
    poloha_prvek1 = randint(0, len(mutace_jedinec)-1)
    poloha_prvek2 = randint(0, len(mutace_jedinec)-1)
    while True:
        if poloha_prvek1 == poloha_prvek2:
            poloha_prvek2 = randint(0, len(mutace_jedinec)-1)
        else:
            break
    prvek = mutace_jedinec[poloha_prvek1]
    mutace_jedinec[poloha_prvek1] = mutace_jedinec[poloha_prvek2]
    mutace_jedinec[poloha_prvek2] = prvek
    new_selection.extend([mutace_jedinec])
    print("tohle je mutovany jedinec PO MUTACI", mutace_jedinec)
    print("Po funkci mutace", new_selection)
    return new_selection

def krizeni(new_selection):
    list_na_shuffle = []
    nahodne_cislo = randint(0, NUM_OF_PEOPLE - 1)
    zkrizeny_jedinec = new_selection[nahodne_cislo]
    print("DOLE JE FUNKCE KRIZENI")
    print("tohle je random jedinec ke krizeni" , zkrizeny_jedinec)
    random_index = randint(0, len(zkrizeny_jedinec)-3)
    print("random index je", random_index)

    prvni_cislo = zkrizeny_jedinec.pop(random_index)
    druhe_cislo = zkrizeny_jedinec.pop(random_index)
    treti_cislo = zkrizeny_jedinec.pop(random_index)

    list_na_shuffle.append(prvni_cislo)
    list_na_shuffle.append(druhe_cislo)
    list_na_shuffle.append(treti_cislo)

    print("toto je list na shuffle", list_na_shuffle)

    random.shuffle(list_na_shuffle)
    print("toto je list po shufflu", list_na_shuffle)
    print("random jedinec nyní", zkrizeny_jedinec)

    for i in reversed(list_na_shuffle):
        zkrizeny_jedinec.insert(random_index, i)
    print("zkrizeny jedinec po insert", zkrizeny_jedinec)

    return new_selection


def main(LIST_OF_CITIES):
    people_generating()
    value(people, LIST_OF_CITIES)
    quality_sorting(people)
    selection(people, NUM_OF_PEOPLE)
    odstraneni_kvality(people)
    print (people)
    #new_selection = selection_final(people_selection)
    #mutace(new_selection)
    #krizeni(new_selection)
    #print(people)


if __name__ == "__main__":
    main(LIST_OF_CITIES)
