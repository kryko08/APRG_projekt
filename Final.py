from random import randint

mesta = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
POCET_MIEST = len(mesta)
ludia=[]
for n in range (5):
    cisla = []
    clovek = ''
    for n1 in range(1, POCET_MIEST + 1):
        cisla.append(n1)
    print(cisla)

    for n2 in range (1, POCET_MIEST + 1):
        n3=randint(0,POCET_MIEST-n2)
        clovek=clovek+str(cisla.pop(n3))
    ludia.append(clovek)
print(ludia)