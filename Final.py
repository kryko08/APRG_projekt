from random import randint
import random
import matplotlib.pyplot as plt
import csv

#with open ("pokus.txt", "r") as txt_file:
#mesta = txt_file.read()www

LIST_OF_CITIES = [[0, 1, 2, 3, 4, 5], [1, 0, 6, 7, 8, 9], [2, 6, 0, 10, 11, 12], [3, 7, 10, 0, 13, 14], [4, 8, 11, 13, 0, 15], [5, 9, 12, 14, 15, 0]]
NUM_OF_CITIES = len(LIST_OF_CITIES)
NUM_OF_PEOPLE = 20
NUM_OF_ITERATIONS = 300
people = []
averages = []
best_value = []
iterations = []


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



def value_remove(people):
    n = 0
    for nn in range (0, NUM_OF_PEOPLE):
        del people[n][0]
        n = n + NUM_OF_PEOPLE - nn
    return people



def selection_final(people):
    population_cut = []
    n = 0
    for x in range(NUM_OF_PEOPLE):
        population_cut.append([])
    while n < NUM_OF_PEOPLE:
        random_index = randint(0, len(people) - 1)
        random_person = list(people[random_index])
        population_cut[n] = list(random_person[0])
        n += 1
    people.clear()
    people.extend(population_cut)
    return people



def mutation(people):
    mutated_person = people.pop(randint(0, NUM_OF_PEOPLE - 1))
    print("tohle je zmutovany jedinec PRED MUTACI", mutated_person)
    element_position1 = randint(0, len(mutated_person)-1)
    element_position2 = randint(0, len(mutated_person)-1)
    while True:
        if element_position1 == element_position2:
            element_position2 = randint(0, len(mutated_person)-1)
        else:
            break
    element = mutated_person[element_position1]
    mutated_person[element_position1] = mutated_person[element_position2]
    mutated_person[element_position2] = element
    people.extend([mutated_person])
    print("tohle je mutovany jedinec PO MUTACI", mutated_person)
    return people



def hybridization(people):
    shuffle_list = []
    random_number = randint(0, NUM_OF_PEOPLE - 1)
    hybrid = people[random_number]
    print("tohle je random jedinec ke krizeni" , hybrid)
    random_index = randint(0, len(hybrid)-3)
    first_number = hybrid.pop(random_index)
    second_number = hybrid.pop(random_index)
    third_number = hybrid.pop(random_index)
    shuffle_list.append(first_number)
    shuffle_list.append(second_number)
    shuffle_list.append(third_number)
    random.shuffle(shuffle_list)
    for i in reversed(shuffle_list):
        hybrid.insert(random_index, i)
    print("zkrizeny jedinec po krizeni", hybrid)
    for i in range(0, len(people)):
        name = []
        name.append(people.pop(0))
        people.append(name)
    return people



def avg_value(people):
    average = 0
    for i in range(0, len(people)):
        average = average + people[i][0]
    average = average / NUM_OF_PEOPLE
    averages.append(average)
    return average



def graphs():
    plt.plot(iterations, averages)
    plt.ylabel('Avg. value')
    plt.xlabel('Iterations')
    plt.show()
    plt.plot(iterations, best_value)
    plt.ylabel('Best value')
    plt.xlabel('Iterations')
    plt.show()


def main(LIST_OF_CITIES):
    people_generating()
    iteration = 0
    while iteration <= NUM_OF_ITERATIONS:
        value(people, LIST_OF_CITIES)
        print("Toto je seznam lidi po %s iteraci"%iteration, people)
        print("Toto je prumerna kvalita:", avg_value(people))
        quality_sorting(people)
        selection(people, NUM_OF_PEOPLE)
        best_value.append(people[0][0])
        value_remove(people)
        selection_final(people)
        mutation(people)
        hybridization(people)
        iterations.append(iteration)
        iteration += 1
    value(people, LIST_OF_CITIES)
    print('toto su finalny ludia: ', people)
    graphs()

#if __name__ == "__main__":
#   main(LIST_OF_CITIES)