import sys


akcja = sys.argv[1]

lista = ["saldo", "sprzedaz", "zakup","stop"]
akcje = ["saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad" ]
historia = []
dane = []
magazyn = dict()


def stan_konta():
    stan_salda=0
    for i in range(len(historia)):  # stan salda
        b = historia[i]
        if b[0] == akcje[0]:
            stan_salda += b[1]
        if b[0] == akcje[1]:
            stan_salda += b[2] * b[3]
        if b[0] == akcje[2]:
            stan_salda -= b[2] * b[3]
    return stan_salda

# nie do końca wiem jak napisać tę funkcję (jakie argumenty podać na wejściu
# i czy jest dobrze zwracam słownik z niej)
def stan_magazynu(magazyn):

    for i in range(len(historia)):  # magazyn
        b = historia[i]
        if b[0] == akcje[2]:
            if b[1] in magazyn:
                magazyn[b[1]] += b[3]
            else:
                magazyn = {b[1]: b[3]}
        if b[0] == akcje[1]:
            if b[1] in magazyn:
                magazyn[b[1]] -= b[3]
    return (magazyn)


def drukuj():

    for idx in range(len(historia)):
        b = historia[idx]
        for i in range(len(b)):
            print(b[i])
    print("stop")

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
mag = stan_magazynu(magazyn)
z = stan_konta()
if akcja == akcje[0]:  #saldo
    x = sys.argv[2]
    y = sys.argv[3]
    saldo = (akcja, int(x), y)
    historia.append(saldo)
    drukuj()
elif akcja == akcje[1]:  #sprzedaż
    id_produktu = sys.argv[2]
    cena = int(sys.argv[3])
    l_sprzedanych = int(sys.argv[4])
    if cena < 0 or l_sprzedanych < 0:
        print("Nieprawidłowa cena lub ilośc produktu (ujemne)")
    elif id_produktu in magazyn and l_sprzedanych <= magazyn[id_produktu]:
        sprzedaz = (akcja, id_produktu, cena, l_sprzedanych)
        historia.append(sprzedaz)
        stan_konta()
        stan_magazynu(mag)
        drukuj()
    else:
        print('Nie ma na tyle produktu do sprzedaży')
elif akcja == akcje[2]:         #zakup
    id_produktu = sys.argv[2]
    cena = int(sys.argv[3])
    l_kupionych = int(sys.argv[4])
    if cena < 0 or l_kupionych < 0:
        print("Nieprawidłowa cena lub liczba sztuk (ujemna)")
    elif z < cena*l_kupionych:
        print("Za mało pieniędzy na koncie,zakup niemozliwy")
    else:
        zakup = (akcja, id_produktu, cena, l_kupionych)
        historia.append(zakup)
        stan_magazynu(mag)
        stan_konta()
        drukuj()
elif akcja == akcje[3]: #konto
    print(stan_konta())
elif akcja == akcje[4]:  # magazyn
    for k, v in mag.items():
        print("{}: {}".format(k, v))
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
