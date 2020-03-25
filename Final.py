from random import randint
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

ZOZNAM_MIEST = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
POCET_MIEST = len(ZOZNAM_MIEST)
POCET_LUDI = 10
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
        ludia[m].append(kvalita)
    return(ludia)

def main(POCET_MIEST, POCET_LUDI, ZOZNAM_MIEST):
    generovanie_ludi(POCET_MIEST,POCET_LUDI)
    hodnota(ludia, POCET_MIEST, POCET_LUDI, ZOZNAM_MIEST)
    print(ludia)

if __name__ == "__main__":
    main(POCET_MIEST,POCET_LUDI, ZOZNAM_MIEST)
