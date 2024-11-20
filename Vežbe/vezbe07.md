# Vežbanje
## Prvi primer
Napisati program koji iz unete rečenice uklanja kasnije definisani karakter

```python
recenica = input("Unesi rečenicu ")
niska = ""
karakter = input("Unesi željeni karakter ")
for slovo in recenica:
    if slovo != karakter:
        niska = niska + slovo
        print(niska)
```

Ili ako se opredelimo da istu stvar uradimo korišćenjem metode [replace()](
https://www.w3schools.com/python/ref_string_replace.asp)

```python
recenica = input("Unesi rečenicu ")
niska = ""
karakter = input("Unesi željeni karakter ")
niska.replace(karakter, "")							# metoda replace menja prvi parametar drugim: replace("a","b") menja svako slovo "a" slovom "b"
```

## Drugi primer
Napisati program koji proverava da li u zadatoj niski ima vise malih ili velikih slova.
```python
niska = input("Unesi reč: ")
mala = 0
velika = 0
for slovo in niska:
    if slovo >= "a" and slovo <= "z":					# proveravamo da li se slovo nalazi između "a" i "z" (ASCII opseg)
        mala = mala + 1
    elif slovo >="A" and slovo <= "Z":					# proveravamo da li se slovo nalazi između "A" i "Z" (ASCII opseg)
        velika = velika + 1
if mala > velika:
    print(f"Niska {niska} ima više malih nego velikih slova")
elif mala < velika:
    print(f"Niska {niska} ima više velikih nego malih slova")
else:
    print(f"Niska {niska} ima podjednak broj malih i velikih slova")
```

Možemo da koristimo i ugrađene metode [islower()](https://www.w3schools.com/python/ref_string_islower.asp) i [isupper](https://www.w3schools.com/python/ref_string_isupper.asp).

```python
niska = input("Unesi reč: ")
mala = 0
velika = 0
for slovo in niska:
    if slovo.islower():					
        mala = mala + 1
    elif slovo.isupper()					
        velika = velika + 1
if mala > velika:
    print(f"Niska {niska} ima više malih nego velikih slova")
elif mala < velika:
    print(f"Niska {niska} ima više velikih nego malih slova")
else:
    print(f"Niska {niska} ima podjednak broj malih i velikih slova")
```

## Treći primer
Napisati program koji proverava da li u zadatoj niski pronalazi poziciju poslednjeg pojavljivanja željenog znaka.
```python
niska = input("Unesi reč: ")
brojac = 0									# usvajamo početnu vrednost promenljive "brojač"
indeks = 0									# usvajamo početnu vrednost promenljive "indeks"
znak = input("Unesi željeni znak: ")
for slovo in niska:
    if slovo == znak:						# ako je promenljiva "slovo" jednaka promenljivoj "znak"
        indeks = brojac						# izjednačiti indeks i brojač
    brojac = brojac + 1						# uvećava se brojač za 1
print(f"Poslednje pojavljivanje znaka '{znak}' ima indeks {indeks}")
```

## Četvrti primer
Napisati program koji unosi niz brojeva od N elemenata, a zatim ispisuje član sa najvećom vrednošću i njegov indeks.

```python
n = int(input("Unesi broj članova niza  n = "))
niz = []
for i in range(0,n):
    clan = float(input(f"Unesi x[{i}] = "))
    niz.append(clan)
print(niz)
maksimum = max(niz)									# funkcija za nalaženje maksimuma
indeks = niz.index(maksimum)						# metoda za vraćanje indeksa člana "maksimum"
print(f"Najveća vrednost niza je {maksimum}, a njen indeks je {indeks}.")
```
A ako ne želimo da koristimo metodu [index()](https://www.w3schools.com/python/ref_list_index.asp), ni funkciju max()

```python
maksimum = niz[0]           						# pretpostavljamo da je prvi element niza, niz[0], najveći
indeks = 0
for i in range(n):
    if niz[i] > maksimum:  							# poredi da li je član veći od pretpostavljenog max
        maksimum = niz[i]   						# ako jeste on postaje novi maksimum
        indeks = i
print(f"Najveća vrednost niza je {maksimum}, a njen indeks je {indeks}.")
```
Na isti način dolazimo do najmanjeg člana niza, i njegovog indeksa:
```python
minimum = min(niz)
indeks = niz.index(minimum)					# primenom metode
print(f"Najmanja vrednost niza je {minimum}, a njen indeks je {indeks}.")

# bez metoda i funkcija:
minimum = niz[0]          							# pretpostavljamo da je prvi član niza, niz[0] najmanji
indeks = 0
for i in range(n):
    if niz[i] < minimum:  							# poredi da li je član manji od pretpostavljenog min
        minimum = niz[i]   							# ako jeste on postaje novi maksimum
        indeks = i
print(f"Najmanja vrednost niza je {minimum}, a njen indeks je {indeks}.")"""
```

## Peti primer
Napisati program koji unosi niz brojeva od n elemenata, a zatim uredjuje niz u rastući.

Unošenje niza vršimo na isti način kao i do sada:

```python
n = int(input("Unesi broj članova niza  n = "))
niz = []
for i in range(0,n):
    clan = float(input(f"Unesi x[{i}] = "))
    niz.append(clan)
print(niz)
```
Sortiranje možemo da izvršimo korišćenjem ugrađenje funkcije sorted():
```python
print(f"Niz sortiran u rastućem poretku: {sorted(niz)}")
```
A ako želimo sami da napišemo algoritam za sortiranje [selection sort](https://www.youtube.com/watch?v=QsNeEm1a-rU):

```python
for i in range(0,n):														# dve petlje, poredimo element i-tog indeksa sa elementima desno od i
    for j in range(i+1,n):
        if niz[i] > niz[j]:
            niz[i], niz[j] = niz[j], niz[i]      							# zamena mesta članovima, niz[i] uzima vrednost niz[j] i obrnuto
print(f"Niz sortiran u rastućem poretku: {niz}")
```
Zamena mesta članovima može da se izvrši i uvođenjem pomoćne, privremene, promenljive:

```python
for i in range(0,n):												
    for j in range(i+1,n):
        if niz[i] > niz[j]:
            privremena = niz[i]
			niz[i] = niz[j]
			niz[j] = privremena      							
print(f"Niz sortiran u rastućem poretku: {niz}")
```

Analogno prethodnim koracima, niz soritramo u opadajućem poretku na sledeći način:

ugrađenom funkcijom:

```python
print(f"Niz sortiran u opadajućem poretku: {sorted(niz, reverse = True)}") 

```
ili algoritmom:

```python
for i in range(0,n):										# dve petlje, poredimo element i-tog indeksa sa elementima desno od i
    for j in range(i+1,n):
        if niz[i] < niz[j]:
            niz[i], niz[j] = niz[j], niz[i]      			# zamena mesta članovima, niz[i] uzima vrednost niz[j] i obrnuto
print(f"Niz sortiran u rastućem poretku: {niz}")
```
Uvođenjem pomoćne, privremene, promenljive:

```python
for i in range(0,n):												
    for j in range(i+1,n):
        if niz[i] < niz[j]:
            privremena = niz[i]
			niz[i] = niz[j]
			niz[j] = privremena      							
print(f"Niz sortiran u rastućem poretku: {niz}")
```
