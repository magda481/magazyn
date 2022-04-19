import sys


akcja = sys.argv[1]
lista = ["saldo", "sprzedaz", "zakup","stop"]
akcje = ["saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad" ]
historia = []
dane = []
stan_salda = 0
magazyn = dict()

while True:
    linia = input()
    dane.append(linia)
    if linia == "stop":
        break
for idx in range(len(dane)):
    if dane[idx] == lista[0]:
        if dane[idx + 3] not in lista:
            print('Błędna akcja, program przerywa pracę!')
            break
        saldo = (dane[idx], int(dane[idx + 1]), (dane[idx + 2]))
        historia.append(saldo)
    elif dane[idx] == lista[1]:
        if dane[idx + 4] not in lista:
            print('Błędna akcja, program przerywa pracę!')
            break
        sprzedaz = (dane[idx], (dane[idx + 1]), int(dane[idx + 2]),
                    int(dane[idx + 3]))
        historia.append(sprzedaz)
    elif dane[idx] == lista[2]:
        if dane[idx + 4] not in lista:
            print('Błędna akcja, program przerywa pracę!')
            break
        zakup = (dane[idx], dane[idx + 1], int(dane[idx + 2]),
                 int(dane[idx + 3]))
        historia.append(zakup)


for idx in range(len(historia)): #magazyn
    b = historia[idx]
    if b[0] == akcje[2]:
        if b[1] in magazyn:
            magazyn[b[1]] += b[3]
        else:
            magazyn = {b[1]: b[3]}
    if b[0] == akcje[1]:
        if b[1] in magazyn:
            magazyn[b[1]] -= b[3]
for idx in range(len(historia)): #stan salda
    b = historia[idx]
    if b[0] == akcje[0]:
        stan_salda += b[1]
    if b[0] == akcje[1]:
        stan_salda += b[2]*b[3]
    if b[0] == akcje[2]:
        stan_salda -= b[2] * b[3]

if akcja == akcje[0]:  #saldo
    x = sys.argv[2]
    y = sys.argv[3]
    saldo = (akcja, int(x), y)
    historia.append(saldo)
    for idx in range(len(historia)):
        b = historia[idx]
        for i in range(len(b)):
            print(b[i])
    print("stop")

elif akcja == akcje[1]:  #sprzedaż
    id_produktu = sys.argv[2]
    cena = int(sys.argv[3])
    l_sprzedanych = int(sys.argv[4])
    if cena < 0 or l_sprzedanych < 0:
        print("Nieprawidłowa cena lub ilośc produktu (ujemne)")
    elif id_produktu in magazyn and l_sprzedanych <= magazyn[id_produktu]:
        sprzedaz = (akcja, id_produktu, cena, l_sprzedanych)
        historia.append(sprzedaz)
        for idx in range(len(historia)):  # stan salda
            b = historia[idx]
            if b[0] == akcje[0]:
                stan_salda += b[1]
            if b[0] == akcje[1]:
                stan_salda += b[2]*b[3]
            if b[0] == akcje[2]:
                stan_salda -= b[2] * b[3]
        for idx in range(len(historia)):
            b = historia[idx]
            if b[0] == akcje[2]:
                if b[1] in magazyn:
                    magazyn[b[1]] += b[3]
                else:
                    magazyn = {b[1]: b[3]}
            if b[0] == akcje[1]:
                if b[1] in magazyn:
                    magazyn[b[1]] -= b[3]
        for idx in range(len(historia)):
            b = historia[idx]
            for i in range(len(b)):
                print(b[i])
        print("stop")
    else:
        print('Nie ma na tyle produktu do sprzedaży')

elif akcja == akcje[2]:         #zakup
    id_produktu = sys.argv[2]
    cena = int(sys.argv[3])
    l_kupionych = int(sys.argv[4])
    if cena < 0 or l_kupionych < 0:
        print("Nieprawidłowa cena lub liczba sztuk (ujemna)")
    elif stan_salda < cena*l_kupionych:
        print("Za mało pieniędzy na koncie,zakup niemozliwy")
    else:
        zakup = (akcja, id_produktu, cena, l_kupionych)
        historia.append(zakup)
        for idx in range(len(historia)):
            b = historia[idx]
            if b[0] == akcje[2]:
                if b[1] in magazyn:
                    magazyn[b[1]] += b[3]
                else:
                    magazyn = {b[1]: b[3]}
            if b[0] == akcje[1]:
                if b[1] in magazyn:
                    magazyn[b[1]] -= b[3]
        for idx in range(len(historia)):  # stan salda
            b = historia[idx]
            if b[0] == akcje[0]:
                stan_salda += b[1]
            if b[0] == akcje[1]:
                stan_salda += b[2] * b[3]
            if b[0] == akcje[2]:
                stan_salda -= b[2] * b[3]
        for idx in range(len(historia)):
            b = historia[idx]
            for i in range(len(b)):
                print(b[i])
        print("stop")

elif akcja == akcje[3]: #konto
    print(stan_salda)

elif akcja == akcje[4]:  # magazyn
    for k, v in magazyn.items():
        print("{}: {}".format(k, v))
# podejrzewam że też możnaby zrobić funkcję żeby się dało drukować zarówno całośc
# jak i część historii ale nie bardzo mam pomysł
elif akcja == akcje[5]:
    lsp = int(sys.argv[2])
    psp = int(sys.argv[3])+1
    for idx in range(lsp, psp):
        b = historia[idx]
        for i in range(len(b)):
            print(b[i])
    print("stop")
elif akcja not in akcje:
    print("Niedozwolona akcja!")
