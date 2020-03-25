from random import randint
#with open ("pokus.txt", "r") as txt_file:
#    mesta = txt_file.read()

ZOZNAM_MIEST = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
POCET_MIEST = len(ZOZNAM_MIEST)
ludia=[]

def generovanie_ludi(POCET_MIEST):
    for n in range(20):
        cisla = []
        clovek = []
        mesta = []
        for n1 in range(1, POCET_MIEST + 1):
            cisla.append(n1)
        print(cisla)

        for n2 in range(1, POCET_MIEST + 1):
            n3 = randint(0, POCET_MIEST - n2)
            mesta.append(cisla.pop(n3))
        clovek.append(mesta)
        ludia.append(clovek)
    return ludia

def main(POCET_MIEST):
    generovanie_ludi(POCET_MIEST)
    print(ludia)

if __name__ == "__main__":
main(POCET_MIEST)
