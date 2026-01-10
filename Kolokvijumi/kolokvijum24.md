# Python II kolokvijum 2024/2025.

## Grupa 1
### Prvi zadatak
Napisati program koji računa vrednost funkcije y = (2X^3)/6 + (3X^5)/9 + (4X^7)/12 + … + (20X^39)/60

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi X = "))
y = 0                                           # početna vrednost funkcije
koeficijent = 2                                 # početna vrednost koeficijenta
eksponent = 3                                   # početna vrednost eksponenta
imenilac = 6                                    # početna vrednost imenioca
for i in range(19):
      y = y + (koeficijent * x **(eksponent))/imenilac  # izračunavanje funkcije
      koeficijent += 1                                  # uvećavanje koeficijenta
      eksponent += 2                                    # uvećavanje eksponenta
      imenilac += 3                                     # uvećavanje imenioca
print(f"Vrednost funkcije y je: {y}, x = {x}")
```
</details>

### Drugi zadatak
Napisati program koji će za uneti niz A dimenzije N da formira niz B koji predstavlja "odraz u ogledalu" niza A.

<details markdown='block'>
<summary>Rešenje </summary>

```python
n = int(input("Unesi broj članova niza n = "))          # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")

B = []                                                  # deklarisanje prazne liste B
'''
B = A[::-1]                                             # slajsovanje niza u nazad
'''
for i in range(n):                                      # ili rešavanje for petljom
      B.append(A[n-1-i])

print(f"Odraz u ogledalu niza {A} je niz {B}.")
```
</details>

### Treći zadatak
Izračunati razliku broja malih i velikih slova u unetoj reči.

<details markdown='block'>
<summary>Rešenje </summary>

```python
broj_malih = 0
broj_velikih = 0
rec = input("Unesi reč ")
for slovo in rec:
    if slovo.isupper():
        broj_velikih += 1
    elif slovo.islower():
        broj_malih += 1
razlika = abs(broj_velikih - broj_malih)            # apsolutna vrednost abs()
print(f"U reči {rec}, razlika broja velikih i malih slova je {razlika}.")
```
</details>

## Druga grupa
### Prvi zadatak
Napisati program koji računa vrednost funkcije y = (6X^3)/2 + (9X^5)/3 + (12X^7)/4 + … + (60X^39)/20 za zadato X.

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi x = "))
y = 0
y = 0                                           # početna vrednost funkcije
koeficijent = 6                                 # početna vrednost koeficijenta
eksponent = 3                                   # početna vrednost eksponenta
imenilac = 2                                    # početna vrednost imenioca
for i in range(19):
    y = y + (koeficijent * x ** eksponent)/imenilac
    koeficijent += 3
    eksponent += 2
    imenilac += 1
print(f"Vrednost funkcije y je: {y} za x = {x}")
```   

</details>


### Drugi zadatak
Napisati program koji će za uneti niz A dimenzije N da formira dva zasebna niza B i C i da izračuna razliku njihovih suma. 
Niz B sadrži sve parne, dok niz C sadrži sve neparne članove niza A.


<details markdown='block'>
<summary>Rešenje </summary>

```python
n = int(input("Unesi broj članova niza n = "))          # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")

B = []                                                  # deklarisanje praznih lista B i C
C = []
sumaB = 0                                               # deklarisanje početnih vrednosti suma
sumaC = 0
for clan in A:
    if clan % 2 == 0:
         B.append(clan)
         sumaB = sumaB + clan
    else:
         C.append(clan)
         sumaC = sumaC + clan
razlika = abs(sumaB - sumaC)                            # apsolutna vrednost razlike abs()
print(f"Suma članova niza B = {B} je {sumaB}, suma članova niza C = {C} je {sumaC}, dok je njihova razlika {razlika}")
```

</details>


### Treći zadatak
Napisati program koji sva velika slova iz unete reči pretvara u mala

<details markdown='block'>
<summary>Rešenje </summary>

```python
rec = input("Unesi reč ")
nova_rec = ""                                           # prazna niska
for slovo in rec:
    if slovo.isupper():
        nova_rec = nova_rec + slovo.lower()
    else:
        nova_rec = nova_rec + slovo
print(nova_rec)
```

</details>

## Treća grupa
### Prvi zadatak
Napisati program koji računa vrednost funkcije y = X^6/2 + X^9/3 + X^12/4 + … + X^30/10 za zadato X. '''

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi X = "))
y = 0                                           # početna vrednost funkcije
eksponent = 6                                   # početna vrednost eksponenta
imenilac = 2                                    # početna vrednost imenioca
for i in range(9):
      y = y + (x**(eksponent))/imenilac  # izračunavanje funkcije
      eksponent += 3                                         # uvećavanje eksponenta
      imenilac += 1                                     # uvećavanje imenioca
print(f"Vrednost funkcije y je: {y}, x = {x}")
```

</details>

### Drugi zadatak
Napisati program koji će za uneti niz A dimenzije N 
da formira niz B koji sadrži sve članove niza A koji su veci od unesenog broja K. 

<details markdown='block'>
<summary>Rešenje </summary>

```python
n = int(input("Unesi broj članova niza n = "))          # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")

B = []                                                  # deklarisanje prazne liste B
K = int(input("Unesi broj K = "))                       # unošenje broja K
for clan in A:                                          # petlja po članovima niza A
      if clan > K:                                      # ako je član veći od K
            B.append(clan)                              # dodaj ga u B
print(f"Novoformirani niz B koji se sastoji od članova niza A = {A}, većih od broja {K} je B = {B}")
```

</details>


### Treći zadatak
Napisati program koji sva velika slova iz unete reči pretvara u mala

<details markdown='block'>
<summary>Rešenje </summary>

```python
rec = input("Unesi reč ")
nova_rec = ""                                           # prazna niska
for slovo in rec:
    if slovo.islower():
        nova_rec = nova_rec + slovo.upper()
    else:
        nova_rec = nova_rec + slovo
print(nova_rec)
```

</details>


## Četvrta grupa
### Prvi zadatak

Napisati program koji računa vrednost funkcije y = X^30/15 + X^28/14 + X^26/13 + … + X^2 za zadato X

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi X = "))
y = 0                                            # početna vrednost funkcije
eksponent = 30                                   # početna vrednost eksponenta
imenilac = 15                                    # početna vrednost imenioca
for i in range(15):
      y = y + (x**(eksponent))/imenilac  # izračunavanje funkcije
      eksponent -= 2                                         # uvećavanje eksponenta
      imenilac -= 1                                         # umanjenje imenioca
print(f"Vrednost funkcije y je: {y}, x = {x}")
```

</details>

### Drugi zadatak
Napisati program koji samostalno formira dva niza A i B i računa razliku njihovih suma (sumaB – sumaA). 
Članovi niza A su svi brojevi od nula do N (granica koju unosi korisnik), a članovi niza B su svi članovi od poslednjeg člana 
niza A do M (granice koju unosi korisnik)

<details markdown='block'>
<summary>Rešenje </summary>

```python
n = int(input("Unesi n = "))
m = int(input("Unesi m = "))
A = []
B = []
sumaA = 0
sumaB = 0
for i in range(n+1):                # od nula do n+1 da bi bio uključen i broj n
      A.append(i)
      sumaA += i
for i in range(n+1,m+1):            # od prvog većeg broja od n do m+1 da bi bio uključen i broj m
      B.append(i)
      sumaB += i
razlika = sumaB - sumaA
print(f"Dobijen je niz A = {A}, čija je suma članova {sumaA}; i niz B = {B}, čija je suma članova {sumaB}, dok je razlika ovih suma: {razlika}.")
```

</details>

### Treći zadatak
Napisati program koji prebrojava koliko puta se slovo „M“ pojavljuje u unetoj reči (i veliko i malo).

<details markdown='block'>
<summary>Rešenje </summary>

```python
rec = input("Unesi reč ")
br = 0
for slovo in rec:
    if slovo in "mM":
        br += 1
print(f"Broj pojavljivanja slova M u reči {rec} je {br}")
```

</details>

## Peta grupa
### Prvi zadatak
Napisati program koji računa vrednost funkcije y = X^2/3 + 2X^3/4 + 3X^4/5 + … + 29X^30/31 za zadato X.'''

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi X = "))
y = 0                                           # početna vrednost funkcije
koeficijent = 1                                 # početna vrednost koeficijenta
eksponent = 2                                   # početna vrednost eksponenta
imenilac = 3                                    # početna vrednost imenioca
for i in range(29):
      y = y + (koeficijent * x **(eksponent))/imenilac  # izračunavanje funkcije
      koeficijent += 1                                  # uvećavanje koeficijenta
      eksponent += 1                                    # uvećavanje eksponenta
      imenilac += 1                                     # uvećavanje imenioca
print(f"Vrednost funkcije y je: {y}, x = {x}")  
```

</details>

### Drugi zadatak
Napisati program koji će za unete nizove A, B i C dimenzije N pronaći najveće članove, a zatim da izračuna njihov zbir.

<details markdown='block'>
<summary>Rešenje </summary>

```python
n = int(input("Unesi dimenzije nizova "))               # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")

B =[]                                                   # deklarisanje prazne liste B
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi B[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      B.append(clan)                                    # smeštanje promenljive "član" na kraj liste "B"
print(f"Uneli ste niz {B}.")

C =[]                                                   # deklarisanje prazne liste C
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi C[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      C.append(clan)                                    # smeštanje promenljive "član" na kraj liste "C"
print(f"Uneli ste niz {C}.")

maxA = A[0]                                             # pretpostavka da je A[0] najveći u nizu A
maxB = B[0]                                             # pretpostavka da je B[0] najveći u nizu B
maxC = C[0]                                             # pretpostavka da je C[0] najveći u nizu C
for clan in A:
      if clan > maxA:
            maxA = clan

for clan in B:
      if clan > maxB:
            maxB = clan

for clan in C:
      if clan > maxC:
            maxC = clan

suma = maxA + maxB + maxC

print(f"Maksimalni član niza A = {A} je {maxA}, niza B = {B} je {maxB}, niza C = {C} je {maxC}, a njihova suma je {suma}")

''' ako bismo radili preko funkcija'''
def unesi_niz(n):
    A =[]                                                   # deklarisanje prazne liste A
    for i in range(n):                                      # petlja odradi n koraka
        clan = int(input(f"Unesi član niza [{i}] = "))      # smeštanje vrednosti u promenljivu "član"
        A.append(clan)                                      # smeštanje promenljive "član" na kraj liste "A"
    print(f"Uneli ste niz {A}.")
    return A
def maksimum(A):
    maxA = A[0]
    for clan in A:
      if clan > maxA:
            maxA = clan
    return maxA
n = int(input("Unesi dimenziju nizova "))
suma = maksimum(unesi_niz(n)) + maksimum(unesi_niz(n)) + maksimum(unesi_niz(n))
print(f"Suma maksimuma unetih nizova je {suma}") 

```

</details>

### Treći zadatak

Napisati program koji prebrojava samoglasnike i suglasnike u unetoj reci i izračunava njihovu razliku. 

<details markdown='block'>
<summary>Rešenje </summary>

```python
rec = input("Unesi reč ")
samoglasnici = 0
suglasnici = 0
for slovo in rec:
    if slovo.isalpha() and slovo.lower() in "aeiou":
        samoglasnici += 1
    elif slovo.isalpha():
        suglasnici +=1
razlika = abs(samoglasnici - suglasnici)
print(f"Reč {rec} se sastoji od {samoglasnici} samoglasnika i {suglasnici} suglasnika, a njihova razlika je {razlika}.")
```

</details>

## Šesta grupa
### Prvi zadatak
Napisati program koji računa vrednost funkcije y = 3X^2 + 4X^3/2 + 5X^4/3 + … + 31X^30/29 za zadato X.

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi X = "))
y = 0                                           # početna vrednost funkcije
koeficijent = 3                                 # početna vrednost koeficijenta
eksponent = 2                                   # početna vrednost eksponenta
imenilac = 1                                    # početna vrednost imenioca
for i in range(29):
      y = y + (koeficijent * x **(eksponent))/imenilac  # izračunavanje funkcije
      koeficijent += 1                                  # uvećavanje koeficijenta
      eksponent += 1                                    # uvećavanje eksponenta
      imenilac += 1                                     # uvećavanje imenioca
print(f"Vrednost funkcije y je: {y}, x = {x}")  

```

</details>

### Drugi zadatak

Napisati program koji će za unete nizove A, B i C dimenzije N pronaći najmanje članove, a zatim da izračuna njihov proizvod.

<details markdown='block'>
<summary>Rešenje </summary>

```python

n = int(input("Unesi dimenzije nizova "))               # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")

B =[]                                                   # deklarisanje prazne liste B
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi B[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      B.append(clan)                                    # smeštanje promenljive "član" na kraj liste "B"
print(f"Uneli ste niz {B}.")

C =[]                                                   # deklarisanje prazne liste C
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi C[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      C.append(clan)                                    # smeštanje promenljive "član" na kraj liste "C"
print(f"Uneli ste niz {C}.")

minA = A[0]                                             # pretpostavka da je A[0] najveći u nizu A
minB = B[0]                                             # pretpostavka da je B[0] najveći u nizu B
minC = C[0]                                             # pretpostavka da je C[0] najveći u nizu C
for clan in A:
      if clan < minA:
            minA = clan

for clan in B:
      if clan < minB:
            minB = clan

for clan in C:
      if clan < minC:
            minC = clan

proizvod = minA * minB * minC

print(f"Minimalni član niza A = {A} je {minA}, niza B = {B} je {minB}, niza C = {C} je {minC}, a njihov proizvod je {proizvod}")

''' ako bismo radili preko funkcija'''
def unesi_niz(n):
    A =[]                                                   # deklarisanje prazne liste A
    for i in range(n):                                      # petlja odradi n koraka
        clan = int(input(f"Unesi član niza [{i}] = "))      # smeštanje vrednosti u promenljivu "član"
        A.append(clan)                                      # smeštanje promenljive "član" na kraj liste "A"
    print(f"Uneli ste niz {A}.")
    return A
def minimum(A):
    minA = A[0]
    for clan in A:
      if clan < minA:
            minA = clan
    return minA
n = int(input("Unesi dimenziju nizova "))
proizvod = minimum(unesi_niz(n)) * minimum(unesi_niz(n)) * minimum(unesi_niz(n))
print(f"Proizvod minimuma unetih nizova je {proizvod}") 

```

</details>


### Treći zadatak

Napisati program koji prebrojava samoglasnike i suglasnike u unetoj reci. Zatim se u zavisnosti od odnosa broja samoglasnika i suglasnika računa y.

<details markdown='block'>
<summary>Rešenje </summary>

```python
rec = input("Unesi reč ")
samoglasnici = 0
suglasnici = 0
for slovo in rec:
    if slovo.isalpha() and slovo.lower() in "aeiou":        # proverava da li je string slovo, prebacuje u malo i proverava 
                                                            # da li se nalazi unutar stringa "aeiou"
        samoglasnici += 1                                   # prebrojava kao samoglasnik
    elif slovo.isalpha():                                   # u suprotnom samo ako je slovo, prebrojava kao suglasnik
        suglasnici +=1

if samoglasnici > suglasnici:
    y = samoglasnici ** 2 + 1
else:
    y = suglasnici ** 3 - 1
print(f"Reč {rec} se sastoji od {samoglasnici} samoglasnika i {suglasnici} suglasnika, pa je rezultat funkcije {y}.")   
```

</details>

## Sedma grupa
### Prvi zadatak

Napisati program koji računa vrednost proizvoda: P(x,n)=(x+1)⋅(x2+2)⋅(x3+3)⋅…⋅(xn+n) za uneto x i n

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi x = "))
n = int(input("Unesi n = "))
proizvod = 1
for i in range(n):
    proizvod = proizvod * (x**i+i)
print(f"Rešenje polinoma za x = {x} i n = {n} je {proizvod}")

```
</details>

### Drugi zadatak
Napisati program koji će za uneti niz A izračunati proizvod minimalnog broja i broja sa maksimalnim parnim indeksom.

<details markdown='block'>
<summary>Rešenje </summary>

```python
n = int(input("Unesi broj članova niza n = "))          # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")
minimalan_clan = A[0]                                        # pretpostavka da je A[0] minimalan clan
maksimalan_indeks = 0                                        # pretpostavka da je 0 maksimalan indeks

for i in range(n):
    if A[i] < minimalan_clan:                                # ako je A[i] manji od pretpostavljenog minimuma
        minimalan_clan = A[i]                                # postaje novi minimum
    if i % 2 == 0 and i > maksimalan_indeks:                 # ako je i parno i veće od pretpostavljenog maksimuma
        maksimalan_indeks = i                                # postaje novi maksimum
proizvod = minimalan_clan * A[maksimalan_indeks]             # A[maksimalan_indes] je element sa maksimalnim parnim indeksom!
print(f"Proizvod minimalnog broja i broja sa maksimalnim parnim indeksom je {proizvod}.")
```
</details>

### Treći zadatak
Napisati program koji za unetu rečenicu sve suglasnike menja definisanim simbolom. I rečenica i simbol se unose sa tastature. 

<details markdown='block'>
<summary>Rešenje </summary>

```python
recenica = input("Unesi recenicu ")
simbol = input("Unesi simbol ")
recenica_nova = ""                                      # prazan string
for slovo in recenica:
    if slovo in "aeiouAEIOU":                           # proveravamo da li se slovo nalazi u skupu aeiouAEIOU
        recenica_nova = recenica_nova + slovo           # ako postoji prepisujemo ga u novu rečenicu
    elif slovo.isalpha:                                 # ako nije u skupu, ali jeste slovo (isključujemo simbole i brojeve), 
                                                        # onda umesto tog slova pišemo simbol
        recenica_nova = recenica_nova + simbol
print(f"Novodobijena recenica je '{recenica_nova}'.")
```
</details>

## Osma grupa
### Prvi zadatak

Napisati program koji računa vrednost funkcije y = x^12 * x^9/2 * x^6/3 * … * 1/5
za uneto x.

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = int(input("Unesi x = "))
y = 1
imenilac = 1
stepen = 12
for i in range(5):
    y = y * (x**stepen)/imenilac
    stepen = stepen - 3
    imenilac = imenilac + 1
print(f"Rešenje polinoma za x = {x} je {y}")
```
</details>

### Drugi zadatak

Napisati program koji će za uneti niz pozitivnih brojeva A izračunati faktorijel maksimalnog broja (faktorijel broja 5: 5! = 5*4*3*2*1). 

<details markdown='block'>
<summary>Rešenje </summary>

```python

n = int(input("Unesi broj članova niza n = "))          # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")
maksimalni_clan = A[0]                                        # pretpostavka da je A[0] maksimalan clan
proizvod = 1
for broj in range(n):
    if broj > maksimalni_clan:
        maksimalni_clan = broj
for broj in range (1, maksimalni_clan + 1):             # od 1 do maksimalni_clan + 1 da bi se uzeo u obzir i maksimalni clan, 
                                                        # a da se ne uzima u obzir 0
    proizvod = proizvod * broj
print(f"Maksimalni clan niza je {maksimalni_clan}, a njegv faktorijel je {proizvod}")

```
</details>

### Treći zadatak
Napisati program koji za unetu rečenicu sve samoglasnike menja definisanim simbolom. I rečenica i simbol se unose sa tastature.

<details markdown='block'>
<summary>Rešenje </summary>

```python
recenica = input("Unesi recenicu ")
simbol = input("Unesi simbol ")
recenica_nova = ""                                      # prazan string
for slovo in recenica:
    if slovo in "aeiouAEIOU":                           # proveravamo da li se slovo nalazi u skupu aeiouAEIOU
        recenica_nova = recenica_nova + simbol          # ako postoji umesto njega pišemo simbol u novu rečenicu
    elif slovo.isalpha:                                 # ako nije u skupu, ali jeste slovo (isključujemo simbole i brojeve), 
                                                        # onda prepisujemo to slovo
        recenica_nova = recenica_nova + slovo
print(f"Novodobijena recenica je '{recenica_nova}'.")
```
</details>

## Deveta grupa
### Prvi zadatak

Napisati program koji računa vrednost funkcije y = (2X^3)/6 + (3X^5)/9 + (4X^7)/12 + … + (20X^39)/60.
Za uneto X.

<details markdown='block'>
<summary>Rešenje </summary>

```python
x = float(input("Unesi vrednost za x: "))
y = 0
brojilac = 2
eksponent = 3
imenilac = 6
for i in range(10):
    y = y + (brojilac * (x ** eksponent)) / imenilac  
    brojilac += 1
    eksponent += 2
    imenilac += 3
print("Vrednost funkcije je y = {y}")
```
</details>

### Drugi zadatak

Napisati program koji će za uneti niz brojeva A prebrojati pozitivne neparne brojeve, dodeliti im vrednost nula i štampati novodobijeni niz i broj izmenjenih članova 

<details markdown='block'>
<summary>Rešenje </summary>

```python

n = int(input("Unesi broj članova niza n = "))          # unošenje broja članova niza
A =[]                                                   # deklarisanje prazne liste A
for i in range(n):                                      # petlja odradi n koraka
      clan = int(input(f"Unesi A[{i}] = "))             # smeštanje vrednosti u promenljivu "član"
      A.append(clan)                                    # smeštanje promenljive "član" na kraj liste "A"
print(f"Uneli ste niz {A}.")
for i in range(n):
    if A[i] > 0 and A[i] % 2 != 0:                      # pozitivan i neparan
        A[i] = 0                                        # pretvori u nulu
        brojac += 1                                     # uvećaj brojač
print("Novodobijeni niz:", A)
print("Broj izmenjenih članova:", brojac)
```
</details>

### Treći zadatak
Napisati program koji za unetu rečenicu prebrojava velika slova i razmake i štampa rezultat funkcije:

\[
f =
\begin{cases}
\text{razmaci}^2, & \text{ako je } slova < razmaci \\
\frac{slova}{razmaci}, & \text{ako je } slova >= razmaci
\end{cases}
\]


<details markdown='block'>
<summary>Rešenje </summary>

```python
recenica = input("Unesi rečenicu: ")
slova = 0
razmaci = 0
for slovo in recenica:
    if slovo > "A" and slovo < "Z"  # ili slovo.isupper():     # veliko slovo
        slova += 1
    elif slovo == " ":      # razmak
        razmaci += 1
print("Broj velikih slova:", slova)
print("Broj razmaka:", razmaci)
if slova < razmaci:
    f = razmaci ** 2
else:
    f = slova / razmaci
print(f"Vrednost funkcije f = {f}")

```
</details>