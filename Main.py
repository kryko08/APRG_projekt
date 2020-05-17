from Final import *



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
    quality_sorting(people)
    print('toto su finalny ludia: ', people)
    graphs()

if __name__ == "__main__":
    main(LIST_OF_CITIES)
