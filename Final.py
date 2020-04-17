from random import randint
import random
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

LIST_OF_CITIES = [[0, 1, 2, 3, 4, 5], [1, 0, 6, 7, 8, 9], [2, 6, 0, 10, 11, 12], [3, 7, 10, 0, 13, 14], [4, 8, 11, 13, 0, 15], [5, 9, 12, 14, 15, 0]]
NUM_OF_CITIES = len(LIST_OF_CITIES)
NUM_OF_PEOPLE = 3
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
    return people_selection



def selection_final(people_selection):
    n = 0
    delka = NUM_OF_PEOPLE
    zuzeni_populace = [[], [], []]
    while n < delka:
        random_index = randint(0, len(people_selection) - 1)
        random_clovek = list(people_selection[random_index])
        zuzeni_populace[n] = list(random_clovek[0])
        n += 1
    return zuzeni_populace



def odstraneni_kvality(people_selection):
    for n in people:
        del n[0]
    return people_selection



def mutace(new_selection):
    mutace_jedinec = new_selection.pop(randint(0, NUM_OF_PEOPLE - 1))
    print(mutace_jedinec)
    print (new_selection)
    poloha_prvek1 = randint(0, len(mutace_jedinec)-1)
    poloha_prvek2 = randint(0, len(mutace_jedinec)-1)
    while True:
        if poloha_prvek1 == poloha_prvek2:
            poloha_prvek2 = randint(0, len(mutace_jedinec)-1)
        else:
            break
    prvek = mutace_jedinec[poloha_prvek1]
    print (poloha_prvek1, poloha_prvek2, prvek)
    mutace_jedinec[poloha_prvek1] = mutace_jedinec[poloha_prvek2]
    mutace_jedinec[poloha_prvek2] = prvek
    new_selection.extend([mutace_jedinec])
    return new_selection

def krizeni(new_selection):
    nahodne_cislo = randint(0, NUM_OF_PEOPLE - 1)
    zkrizeny_jedinec = new_selection[nahodne_cislo]
    print(zkrizeny_jedinec)
    # random_element = randint(0, len(zkrizeny_jedinec)-1)
    # rand_cislo = zkrizeny_jedinec[random_element]
    # interval = (rand_cislo, rand_cislo + 2)
    # if rand_cislo == zkrizeny_jedinec[-1] or zkrizeny_jedinec[-2]:
    #     interval = (rand_cislo, rand_cislo - 2)
    # print(interval)
    # random.shuffle(interval)
    # print(interval)

    # random.shuffle(zkrizeny_jedinec)
    # print(zkrizeny_jedinec)
    #new_selection[nahodne_cislo]= zkrizeny_jedinec
    return new_selection


def main(LIST_OF_CITIES):
    people_generating()
    value(people, LIST_OF_CITIES)
    quality_sorting(people)
    people_selection = selection(people, NUM_OF_PEOPLE)
    print(people)
    odstraneni_kvality(people_selection)
    new_selection = selection_final(people_selection)
    print(new_selection)
    mutace(new_selection)
    print(new_selection)
    # krizeni(new_selection)
    # print(new_selection)


if __name__ == "__main__":
    main(LIST_OF_CITIES)
