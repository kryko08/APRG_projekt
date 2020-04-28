from random import randint
import random
import matplotlib.pyplot as plt
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

LIST_OF_CITIES = [[0, 1, 2, 3, 4, 5], [1, 0, 6, 7, 8, 9], [2, 6, 0, 10, 11, 12], [3, 7, 10, 0, 13, 14], [4, 8, 11, 13, 0, 15], [5, 9, 12, 14, 15, 0]]
NUM_OF_CITIES = len(LIST_OF_CITIES)
NUM_OF_PEOPLE = 5
POCET_ITERACI = 20
people = []
priemery = []
iteracie = []


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
    return (people)



def value(people, LIST_OF_CITIES):
    for m in range(NUM_OF_PEOPLE):
        quality = 0
        for m1 in range(NUM_OF_CITIES - 1):
            quality = quality + LIST_OF_CITIES[people[m][0][m1] - 1][people[m][0][m1 + 1] - 1]
        people[m].insert(0, quality)
    return(people)



def quality_sorting(people):
    sorted_people = sorted(people)
    people.clear()
    people.extend(sorted_people)
    return people



def selection(people, NUM_OF_PEOPLE):
    people_selection = []
    for element in range(len(people)):
        multipation = NUM_OF_PEOPLE - element
        index = 0
        while index < multipation :
            people_selection.append(people[element])
            index = index + 1
    people.clear()
    people.extend(people_selection)
    return people



def odstraneni_kvality(people):
    n = 0
    for nn in range (0, NUM_OF_PEOPLE):
        del people[n][0]
        n = n + NUM_OF_PEOPLE - nn
    return people



def selection_final(people):
    zuzeni_populace = []
    n = 0
    for x in range(NUM_OF_PEOPLE) :
        zuzeni_populace.append([])
    while n < NUM_OF_PEOPLE:
        random_index = randint(0, len(people) - 1)
        random_clovek = list(people[random_index])
        zuzeni_populace[n] = list(random_clovek[0])
        n += 1
    people.clear()
    people.extend(zuzeni_populace)
    return people



def mutace(people):
    mutace_jedinec = people.pop(randint(0, NUM_OF_PEOPLE - 1))
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
    people.extend([mutace_jedinec])
    print("tohle je mutovany jedinec PO MUTACI", mutace_jedinec)
    return people



def krizeni(people):
    list_na_shuffle = []
    nahodne_cislo = randint(0, NUM_OF_PEOPLE - 1)
    zkrizeny_jedinec = people[nahodne_cislo]
    print("tohle je random jedinec ke krizeni" , zkrizeny_jedinec)
    random_index = randint(0, len(zkrizeny_jedinec)-3)
    prvni_cislo = zkrizeny_jedinec.pop(random_index)
    druhe_cislo = zkrizeny_jedinec.pop(random_index)
    treti_cislo = zkrizeny_jedinec.pop(random_index)
    list_na_shuffle.append(prvni_cislo)
    list_na_shuffle.append(druhe_cislo)
    list_na_shuffle.append(treti_cislo)
    random.shuffle(list_na_shuffle)
    for i in reversed(list_na_shuffle):
        zkrizeny_jedinec.insert(random_index, i)
    print("zkrizeny jedinec po krizeni", zkrizeny_jedinec)
    for i in range(0, len(people)):
        nazev = []
        nazev.append(people.pop(0))
        people.append(nazev)
    return people



def prumerna_kvalita(people):
    prumer = 0
    for i in range(0, len(people)):
        prumer = prumer + people[i][0]
    prumer = prumer / NUM_OF_PEOPLE
    priemery.append(prumer)
    return prumer



def main(LIST_OF_CITIES):
    people_generating()
    iterace = 0
    while iterace <= POCET_ITERACI:
        value(people, LIST_OF_CITIES)
        print("Toto je seznam lidi po %s iteraci"%iterace, people)
        print("Toto je prumerna kvalita:", prumerna_kvalita(people))
        quality_sorting(people)
        selection(people, NUM_OF_PEOPLE)
        odstraneni_kvality(people)
        selection_final(people)
        mutace(people)
        krizeni(people)
        iteracie.append(iterace)
        iterace += 1
    value(people, LIST_OF_CITIES)
    print('toto su finalny ludia: ', people)
    plt.plot(iteracie, priemery)
    plt.ylabel('Priemerna hodnota iterace')
    plt.xlabel('iterace')
    plt.show()



if __name__ == "__main__":
    main(LIST_OF_CITIES)