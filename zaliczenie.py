import random
print("_____________________________________________")
wielkosc = (random.randint(10,20))
print("wylosowana wielkosc tablicy:",wielkosc)
print("_____________________________________________")


stosunek = 0
liczba_elementow_true = 0
suma_true = 0
max1 = -100
max2 = -100
suma_p_w = 0
suma_n_k = 0
liczba_komorek = 0

Tablica = [[None] * wielkosc for i in range(wielkosc)]       #wypelniamy tablice o none, range leci od i=0 do wylosowanej wielkosci

for j  in range(wielkosc):
    for k in range(wielkosc):                                #petla dla j - wiersze i k - kolumny.
        if j == k:
            x = (random.randint(1,100))                      #losowanie od 1 do 100 (procenty)
            if x <= 35:
                Tablica[j][k] = 1
            else:
                Tablica[j][k] = -1                          #koniec przekatnej
        else:
            Tablica[j][k] = (random.randint(-100,100))      #reszta ma wartosci wylosowane od -100 do 100
        if Tablica[j][k] > max2 and Tablica[j][k] != max1:  #sprawdzamy czy indeks jest wiekszy niz max2:
            max2 = Tablica[j][k]                            #do max2 przypisujemy wartosc komorki
            if max2 > max1:
                x = max2
                max2 = max1                                 #max1 - pierwsza najwieksza max2 - druga najwieksza, x jest potrzebny do zamiany max2 z max1
                max1 = x
        if j%2 == 0:                                        #j = wiersze parzyste
            suma_p_w += Tablica[j][k]                       #zlicza  sume watosci w komorkach o parzystych indeksach wierszy
        if k%2 != 0:                                        #k = komorki nieparzyste
            suma_n_k += Tablica[j][k]                       #zlicza sume liczb w komorkach o nieparzystych indeksach kolumn
        if Tablica[j][k]<j*k:
            liczba_komorek += 1                             #zlicza liczbe komorek w ktorej indeks jest mniejszy niz iloczyn indeksu wiersza i komorki

stosunek = suma_n_k/suma_p_w                                #stosunek suma_n_k i suma_p_w

print("Tablica:")
print(Tablica)
print("_____________________________________________")

#tablica boolowska

Tablicabool = [[None] * wielkosc for i in range(wielkosc)]     #tworzymy tablice o j,k razy wielkosc a range zlicza nam od 0 do i,  i wpisuje none

for j in range (wielkosc):
    for k in range (wielkosc):
        x = (random.randint(0,1))                             #random 0,1 tworzymy tablice boolowska
        if x  == 1:
            Tablicabool[j][k] = True
            liczba_elementow_true += 1                        #zliczanie ile jest true
            suma_true += Tablica[j][k]                        #zlicza sumy elementow
        else:
            Tablicabool[j][k] = False



print("Ilosc true w tablicy boolowskiej:",liczba_elementow_true)
print("Suma ilosci true w tablicy boolowskiej:",suma_true)
print("_____________________________________________")
print("Maxymalne wartosci tablicy to:",max1,"oraz",max2)
print("_____________________________________________")
print("Stosunek = ",suma_n_k,"/",suma_p_w," = ",stosunek)
print("_____________________________________________")
print("Liczba_komorek",liczba_komorek)
print("_____________________________________________")

