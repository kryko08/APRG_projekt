from random import randint
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

ZOZNAM_MIEST = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
POCET_MIEST = len(ZOZNAM_MIEST)
POCET_LUDI = 3
ludia=[]

def generovanie_ludi(POCET_MIEST, POCET_LUDI):
    for n in range(POCET_LUDI):
        cisla = []
        clovek = []
        mesta = []
        for n1 in range(1, POCET_MIEST + 1):
            cisla.append(n1)

        for n2 in range(1, POCET_MIEST + 1):
            n3 = randint(0, POCET_MIEST - n2)
            mesta.append(cisla.pop(n3))
        clovek.append(mesta)
        ludia.append(clovek)
    return (ludia)

def hodnota(ludia, POCET_MIEST, POCET_LUDI, ZOZNAM_MIEST):
    for m in range(POCET_LUDI):
        kvalita = 0
        for m1 in range(POCET_MIEST-1):
            kvalita = kvalita + ZOZNAM_MIEST[ludia[m][0][m1]-1][ludia[m][0][m1+1]-1]
        ludia[m].insert(0, kvalita)
    return(ludia)

def serazeni_kvality(ludia):
    sorted_ludia = sorted(ludia)
    return sorted_ludia

def selekce(sorted_ludia, POCET_LUDI):
    konstanta = POCET_LUDI
    selekce_lidi = []
    for prvek in range(len(sorted_ludia)):
        nasobeni = konstanta - prvek
        index = 0
        while index < nasobeni :
            selekce_lidi.append(sorted_ludia[prvek])
            index = index + 1
    return selekce_lidi


def main(POCET_MIEST, POCET_LUDI, ZOZNAM_MIEST):
    generovanie_ludi(POCET_MIEST,POCET_LUDI)
    hodnota(ludia, POCET_MIEST, POCET_LUDI, ZOZNAM_MIEST)
    sorted_ludia = serazeni_kvality(ludia)
    selekce_lidi = selekce(sorted_ludia, POCET_LUDI)
    print(sorted_ludia)
    print(selekce_lidi)

if __name__ == "__main__":
    main(POCET_MIEST,POCET_LUDI, ZOZNAM_MIEST)
