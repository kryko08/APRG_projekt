from random import randint
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

LIST_OF_CITIES = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
NUM_OF_CITIES = len(LIST_OF_CITIES)
NUM_OF_PEOPLE = 3
people = []

def people_generating(NUM_OF_CITIES, NUM_OF_PEOPLE):
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

def value(people, NUM_OF_CITIES, NUM_OF_PEOPLE, LIST_OF_CITIES):
    for m in range(NUM_OF_PEOPLE):
        quality = 0
        for m1 in range(NUM_OF_CITIES - 1):
            quality = quality + LIST_OF_CITIES[people[m][0][m1] - 1][people[m][0][m1 + 1] - 1]
        people[m].insert(0, quality)
    return(people)

def quality_sorting(people):
    sorted_people = sorted(people)
    return sorted_people

def selection(sorted_people, NUM_OF_PEOPLE):
    CONSTANT = NUM_OF_PEOPLE
    people_selection = []
    for element in range(len(sorted_people)):
        multipation = CONSTANT - element
        index = 0
        while index < multipation :
            people_selection.append(sorted_people[element])
            index = index + 1
    return people_selection


def main(NUM_OF_CITIES, NUM_OF_PEOPLE, LIST_OF_CITIES):
    people_generating(NUM_OF_CITIES, NUM_OF_PEOPLE)
    value(people, NUM_OF_CITIES, NUM_OF_PEOPLE, LIST_OF_CITIES)
    sorted_people = quality_sorting(people)
    people_selection = selection(sorted_people, NUM_OF_PEOPLE)
    print(sorted_people)
    print(people_selection)

if __name__ == "__main__":
    main(NUM_OF_CITIES, NUM_OF_PEOPLE, LIST_OF_CITIES)
