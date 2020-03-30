from random import randint
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

LIST_OF_CITIES = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
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


def main(LIST_OF_CITIES):
    people_generating()
    value(people, LIST_OF_CITIES)
    quality_sorting(people)
    people_selection = selection(people, NUM_OF_PEOPLE)
    print(people)
    print(people_selection)

if __name__ == "__main__":
    main(LIST_OF_CITIES)
