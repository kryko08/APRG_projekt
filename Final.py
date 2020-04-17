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
    zuzeni_populace = []
    delka = NUM_OF_PEOPLE
    rand_prvek = random.choices(people_selection, k = delka)
    zuzeni_populace.extend(rand_prvek)
    return zuzeni_populace



def odstraneni_kvality(people_selection):
    for n in people:
        del n[0]
    return people_selection



#def mutace(new_selection):
    #mutace_jedinec = new_selection[randint(0, NUM_OF_PEOPLE - 1)][1]
    #print(mutace_jedinec)
    #poloha_prvek1 = randint(0, len(mutace_jedinec))
    #poloha_prvek2 = random.choice([i for i in range(0,len(mutace_jedinec)) if i not in [poloha_prvek1]])
    # mutace_prvek[poloha_prvek1], mutace_prvek[poloha_prvek2] = mutace_prvek[poloha_prvek2], mutace_prvek[poloha_prvek1]
    # new_selection.append([])
    # new_selection[len(new_selection) - 1].append(mutace_jedinec)
    #return new_selection

# def krizeni(new_selection):
    # zkrizeny_jedinec = new_selection.pop(randint(0, NUM_OF_PEOPLE - 1))
    # print(zkrizeny_jedinec)
    # random.shuffle(zkrizeny_jedinec[0])
    # print(zkrizeny_jedinec)
    # new_selection.append(zkrizeny_jedinec)
    # return new_selection

    # random.shuffle(new_selection[randint(0, NUM_OF_PEOPLE - 1)])
    # return new_selection


def main(LIST_OF_CITIES):
    people_generating()
    value(people, LIST_OF_CITIES)
    quality_sorting(people)
    people_selection = selection(people, NUM_OF_PEOPLE)
    print(people)
    print(people_selection)
    new_selection = selection_final(people_selection)
    odstraneni_kvality(people_selection)
    print(new_selection)
    #mutace(new_selection)
    #print(new_selection)
    # krizeni(new_selection)
    # print(new_selection)


if __name__ == "__main__":
    main(LIST_OF_CITIES)
