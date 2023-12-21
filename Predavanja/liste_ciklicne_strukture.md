# Liste i ciklične strukture

## Liste

### Osnovno o listama

Kada je reč o listama kao strukturi podataka možemo reći sledeće:

* liste kao niske, celi ili realni brojevi su tip podataka u pajtonu
* liste su najzastupljeniji složeni tip podataka u pajtonu
* liste odgovaraju nizovima u drugim programskim jezicima poput Java ili C - samo sto su liste poseban tip podataka i ne čuvaju samo jedan tip
* načini definisanja liste:

    ```python
    a = [1, 2, 3, 4]
    b = ["Zdravo","Masinsko inzenjerstvo","Racunarski alati"]
    c = ["Petar", 2, 6.78, True, "Urbano inzenjerstvo"]
    lista = []
    lista = [[1, 2], 5, True, [2, 4, 7]]
    ```

* članovi liste, kao i sama lista su promenljivi

### Rad sa listama

* štampanje liste

  ```python
  a = [3, 101, -4, 99, 33]
  print(a) => [3, 101, -4, 99, 33]
  ```

* pristupanje pojedinačnim članovima liste

  ```python
  prvi_clan = a[0]   
  poslednji_clan = a[-1]
  ```

* izmena članova liste

  ```python
  print(a[1])
  a[1] = 1000
  print(a[1])
  ```

* povezivanje i umnožavanje listi
  
  ```python
  brojevi1 = [1, 4, 6]
  brojevi2 = [3, 8, 9]
  print(brojevi1)
  print(brojevi2)
  print(brojevi1 + brojevi2)   
  print(brojevi1 * 3)
  ```

* izmena mesta članovima liste

  ```python
  lista = ["Huawei", "Microsoft", "Apple"]
  print("lista pre promene")
  print(lista)
  privremena = lista[0]
  lista[0] = lista[-1]
  lista[-1] = privremena
  print("lista nakon zamene")
  print(lista)
  ```

* izmena mesta članovima liste – u pajtonu
  
  ```python
  lista[0], lista[-1] = lista[-1], lista[0]
  print(lista)
  ```

### Metode za rad sa listama

| Primer   | Opis                 |
|-------|-------------------------|
| a.append(x) | dodaje član na kraj liste |
| a.pop(x) | briše član na kraju liste |
| a.index(x)  | vraća indeks člana |
| a.extend(3, 'rec')  | proširuje listu |
| a.remove('Alati')  | uklanja član liste |
| a.sort()  | uređuje listu u rastuću |
| a.insert(2, 199)  | ubacuje član na mesto |

### Funkcije za rad sa listama

| Primer   | Opis                 |
|-------|-------------------------|
| len(lista) | dužina liste |
| max(lista) | najveći član liste |
| min(lista)  | najmanji član liste |
| sorted(lista)  | sortiranje liste |
| sum(lista)  | sumiranje liste |

Najvažnije funkcije za rad sa listama brojeva su:

* izračunavanje dužine liste

    ```python
    dužina = len (brojevi)
    ```

* izračunavanje najvećeg člana liste
  
    ```python
    maksimalni_clan = max(brojevi)
    ```

* nalaženje najmanjeg člana liste

    ```python
    minimalni_clan = min(brojevi)
    ```

* nalaženje sume članova liste
  
    ```python
    suma_liste = sum(brojevi)
    ```

* sortiranje liste u rastućem redosledu

    ```python
    poredjani_brojevi = sorted(brojevi)
    ```

### Metode i funkcije

Iako ćemo o metodama i funkcijama govoriti kasnije ovde skrećemo pažnju na stvari:

* metode su ugrađene funkcije koje su vezane za tip promenljive
* kako su liste izmenjive, metode vrše njihovu izmenu na licu mesta nakon poziva (lista.append(x), lista.sort())
* funkcije mogu biti korisničke (piše ih korisnik) ili ugrađene i vezane za tip
* funkcije ne menjaju liste nakon poziva (sorted(lista), len(lista))

### Službena reč in

Službena reč in u pajtonu se koristi na više načina:

* vraća vrednost True/False u zavisnosti da li se ispitani član nalazi u nekom skupu (listi)
* u for petljama kod definisanja opsega u kom se brojač menja

```python
predmeti = ["Racunarski alati", "Mehanika 1", "Masinski materijali", "Matematika 1"]

print('Engleski jezik' in predmeti)   => False   
print('Racunarski alati' in predmeti) => True
print('Mehanika 1' not in predmeti)   => False
```

### Raspakovanje liste

```python
predmeti = ["Matematika 1", "Racunarski alati", "Mehanika 1]

utorak, sreda, cetvrtak = ["Matematika 1", "Racunarski alati", "Mehanika 1]

utorak, sreda, cetvrtak = predmeti

print("---Predmeti----")
print(utorak)
print(sreda)
print(cetvrtak)
print('--------------')
```

### Višedimenzionalne liste

```python
# visedimenzioni nizovi - 2D liste – liste listi
matrica = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(matrica)
# pristup pojedinim clanovima matrice - redovi matrice
print(matrica[0])    => [1, 2, 3]
print(matrica[1])    => [4, 5, 6]
print(matrica[2])    => [7, 8, 9]
# pristupanje dijagonalnim clanovima matrice A(1,1), A(2,2), A(3,3)
print(matrica[0][0]) => 1
print(matrica[1][1]) => 5
print(matrica[2][2]) => 9
```

## Ciklične strukture

### Tipovi cikličnih struktura (petlji)

* for petlje – omogućavaju da se jedna ili blok komandi (telo petlje) izvrši ciklično tačno određeni broj puta

    ```python
    for brojac in opseg:
        telo petlje
    ```

* while petlje – omogućavaju da se jedna ili blok komandi (telo petlje) izvršava sve dok su početni uslovi zadovoljeni

    ```python
    while uslov:
        telo petlje
    ```

### For petlja

Primeri korišćenja for petlji:

```python
for brojac in opseg:
    telo petlje
```

```python
for brojac in range(pocetni indeks, krajnji indeks):
    telo petlje
```

```python
for brojac in range(pocetni indeks, krajnji indeks, korak):
    telo petlje
```

```python
for brojac in range(krajnji indeks):
    telo petlje
```

Šematsko objašnjenje for petlje prikazano je na slici ispod.

![For petlja](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/3f682617-a159-4e13-82ee-01ad7bba4b39)

### Formulisanje for petlje

```python
for brojac in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(brojac)
```

```python
for brojac in range(0, 10):
     print(brojac)
```

```python
for brojac in range(0, 10, 2):
    print(brojac)
```

```python
for brojac in range(10):
    print(brojac)
```

### Iteracija for petlje po članovima liste

```python
for clan in lista:
    print(clan)
```

```python
reci = ["Masinski materijali", "Mehanika 1", "Engleski jezik", "Racunarski alati"]
print(reci[-1])
print(reci[-1][-1])
for rec in reci:
    for slovo in rec:
        print(slovo)
for rec in reci:
    print("\n")
    for slovo in rec:
        print(slovo)
```

### While petlja

```python
while uslov:
    telo petlje
```

```python
brojac = 0    
while brojac < 10:
    print(brojac)           
    brojac = brojac + 1     
```

![While_petlja](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/96cfe586-f504-46f7-9dee-10c087187811)

**Kod while petlji treba biti oprezan – mogu biti beskonačne!!!**

## Primeri

### Primer 1

Napisati program koji omogućava korisniku da učita listu n celih brojeva.

```python
n = int(input("Unesi duzinu niza: "))
lista = []
for i in range(n):
    element = int(input(f"Unesi {i} clan niza: "))
    lista.append(element)
for i in range(n):
    #print(lista[i])
    print(f"lista[{i}] = {lista[i]}")
for element in lista:
    print(element)
```

### Primer 2

Napisati program koji omogućava korisniku da učita listu kvadratnu matricu.

```python
n = int(input("Unesi dimenzije matrice: "))
matrica = []
for i in range(n):
    red = []
    for j in range(n):
        clan = int(input("Unesi clan matrice: "))
        red.append(clan)
    matrica.append(red)
for red in matrica:
    for kolona in red:
        print(kolona)
for red in matrica:
    print(red)
```

### Primer 3

Napisati program koji se određuje broj i zbir cifara dekadnog zapisa prirodnog broja.

```python
n = int(input())
broj_cifara = 0
zbir_cifara = 0
racunaj = True
while racunaj: 
    cifra = n % 10 
    broj_cifara = broj_cifara + 1 
    zbir_cifara = zbir_cifara + cifra 
    n = n // 10 
    if n == 0: 
        racunaj = False 
        
print(broj_cifara, zbir_cifara)
```

### Primer 4

Napisati program koji omogućava izvršavanje osnovnih operacija na prosleđenim brojevima.

```python
prvi_broj = float(input('Unesi prvi broj: '))
drugi_broj = float(input('Drugi broj: '))
operacija = input('Unesi racunsku operaciju (+, -, *, /): ')
racunaj = True
if operacija == '+':
   rezultat = prvi_broj + drugi_broj
elif operacija == '-':
   rezultat = prvi_broj - drugi_broj
elif operacija == '*':
   rezultat = prvi_broj * drugi_broj
elif operacija == '/':
   rezultat = prvi_broj / drugi_broj
else:
  racunaj = False
if racunaj: 
  print(f"Rezultat operacije {operacija} na brojevima {prvi_broj} i {drugi_broj} je: {rezultat:.3f}")
else:
  print("Niste uneli jednu od operacija +, -, *, /")
```

```python
prvi_broj = float(input('Unesi prvi broj: '))
drugi_broj = float(input('Drugi broj: '))
operacija = input('Unesi racunsku operaciju (+, -, *, /): ')
racunaj = False
if operacija in ['+', '-', '*', '/']:
    racunaj = True
if operacija == '+':
   rezultat = prvi_broj + drugi_broj
elif operacija == '-':
   rezultat = prvi_broj - drugi_broj
elif operacija == '*':
   rezultat = prvi_broj * drugi_broj
elif operacija == '/':
   rezultat = prvi_broj / drugi_broj
if racunaj: 
  print(f"Rezultat operacije {operacija} na brojevima {prvi_broj} i {drugi_broj} je: {rezultat:.3f}")
else:
  print("Niste uneli jednu od operacija +, -, *, /")
```

```python
prvi_broj = float(input('Unesi prvi broj: '))
drugi_broj = float(input('Drugi broj: '))
operacija = input('Unesi racunsku operaciju (+, -, *, /): ')
while operacija not in ['+', '-', '*', '/']:
    operacija = input('Unesite jednu od operacija (+, -, *, /): ')
if operacija == '+':
   rezultat = prvi_broj + drugi_broj
if operacija == '-':
   rezultat = prvi_broj - drugi_broj
if operacija == '*':
   rezultat = prvi_broj * drugi_broj
if operacija == '/':
   rezultat = prvi_broj / drugi_broj
 
print(f"Rezultat operacije {operacija} na brojevima {prvi_broj} i {drugi_broj} je: {rezultat:.3f}")
```

```python
prvi_broj = float(input('Unesi prvi broj: '))
operacija = input('Unesi racunsku operaciju (+, -, *, /): ')
while operacija not in ['+', '-', '*', '/']:
    operacija = input('Unesite jednu od operacija (+, -, *, /): ')
drugi_broj = float(input('Unesi drugi broj: '))
while (operacija == '/' and drugi_broj == 0):
    drugi_broj = float(input('Deljenje nulom nije dozvoljeno, unesi drugi broj: '))
if operacija == '+':
   rezultat = prvi_broj + drugi_broj
if operacija == '-':
   rezultat = prvi_broj - drugi_broj
if operacija == '*':
   rezultat = prvi_broj * drugi_broj
if operacija == '/':
   rezultat = prvi_broj / drugi_broj
 
print(f"Rezultat operacije {operacija} na brojevima {prvi_broj} i {drugi_broj} je: {rezultat:.3f}")
```
