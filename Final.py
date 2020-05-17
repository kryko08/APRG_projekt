from random import randint
import random
import matplotlib.pyplot as plt
from Cities import *


LIST_OF_CITIES = LIST_OF_CITIES3
NUM_OF_CITIES = len(LIST_OF_CITIES)
NUM_OF_PEOPLE = 20
NUM_OF_ITERATIONS = 200
people = []
averages = []
best_value = []
iterations = []

#Krajco
def people_generating():
    """
    Funkce generování jedinců

    Funkce vytvoří populaci, ve které bude každý člověk reprezentován
    vnořeným seznamem s čísly, které popisují jakými městy
    v jakém pořadí daný jedinec prošel.

    Returns:
    people

    """

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


#Krajco
def value(people, LIST_OF_CITIES):
    """
    Funkce přiřazení kvality

    Funkce přiřadí každému jedinci jeho kvalitu, což je vzdálenost,
    kterou daný jedinec ušel při svém náhodném průchodu městy.
    Čím je ušlá vzdálenost kratší, tím větší je kvalita jedince.

    Parameters:
    people, LIST_OF_CITIES

    Returns:
    people

    """

    for m in range(NUM_OF_PEOPLE):
        quality = 0
        for m1 in range(NUM_OF_CITIES - 1):
            quality = quality + LIST_OF_CITIES[people[m][0][m1] - 1][people[m][0][m1 + 1] - 1]
        people[m].insert(0, quality)
    return(people)


#Krmela
def quality_sorting(people):
    """
    Fuknce seřazení jedinců

    Fuknce seřadí jedince podle kvality. Nejkvalitnější jedinec, to je jedinec
    s nejkratší ušlou vzdáleností, se zařadí na první místo v seznamu.
    Nejméně kvalitní jedinec na poslední.

    Parameters:
    people

    Returns:
    people

    """

    sorted_people = sorted(people)
    people.clear()
    people.extend(sorted_people)
    return people


#Krmela
def selection(people, NUM_OF_PEOPLE):
    """
    Funkce k roznásobení jedinců

    Funkce každého jedince zkopíruje do nového seznamu právě tolikrát
    podle jeho pozice v seznamu people. Nejkvalitnější jedinec
    bude v novém seznamu zastoupen nejvíckrát, nejméně kvalitní jedinec nejméněkrát

    Parameters:
    people, NUM_OF_PEOPLE

    Returns:
    people

    """

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


#Krmela
def value_remove(people):
    """Funkce slouží k odstranění kvality"""

    n = 0
    for nn in range (0, NUM_OF_PEOPLE):
        del people[n][0]
        n = n + NUM_OF_PEOPLE - nn
    return people


#Kopecny
def selection_final(people):
    """
    Funkce provádí selekci jedinců

    Funkce náhodně vybere se seznamu jedince. Vzhledem k tomu,
    že kvalitnější jedinci jsou zastoupeni vícekrát než ti méně kvalitní,
    je i větší pravděpodobnost, že budou do nové populace vybráni.

    Parameters:
    people

    Returns:
    poeple

    """

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


#Krajco
def mutation(people):
    """
    Funkce mutace

    Funkce pracuje pouze s jedním náhodným jedincem.
    Dojde k náhodnému vybrání dvou čísel (měst) a jejich vzájemnému
    prohození. Mění se tak cesta, kterou zmutovaný jedinec prošel.
    To má následně vliv i na jeho kvalitu.

    Parameters:
    people

    Returns:
    people

    """

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


#Kopecny
def hybridization(people):
    """
    Funkce křížení

    Funkce pracuje s náhodným jedincem. V jeho seznamu
    se vyberou tři sousedící čísla a ty se mezi sebou promíchají.
    Stejně jako mutace má tato funkce vliv na kvalitu jedince.

    Parameters:
    people

    Returns:
    people

    """

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


#Kopecny
def avg_value(people):
    """Funkce určí průměrnou kvalitu populace"""

    average = 0
    for i in range(0, len(people)):
        average = average + people[i][0]
    average = average / NUM_OF_PEOPLE
    averages.append(average)
    return average


#Krajco
def graphs():
    """Funkce k vytvoření grafů"""

    plt.plot(iterations, averages)
    plt.ylabel('Avg. value')
    plt.xlabel('Iterations')
    plt.show()
    plt.plot(iterations, best_value)
    plt.ylabel('Best value')
    plt.xlabel('Iterations')
    plt.show()

def route():
    route_final = people[0][1]
    for x in range (0,NUM_OF_CITIES):
        print (CITY_NAMES[route_final[x]-1], end=', ')


