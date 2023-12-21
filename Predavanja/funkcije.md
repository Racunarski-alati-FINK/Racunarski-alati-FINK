# Funkcije

## Definicija funkcija

* funkcije predstavljaju grupu instrukcija (komandi) pod odgovarajućim imenom
* funkcije mogu biti bez argumenata, sa jednim ili vise argumenata
* funkcije mogu vraćati programu jednu ili više vrednosti
* funkcije se izvršavaju tek po pozivu imenom i spiskom argumenata iz glavnog programa
* prednost funkcija je što mogu biti pozvane beskonačno puta
* glavna prednost je što nema ponavljanja koda

## Definisanje funkcije

* funkcija bez argumenata:

    ```python
    def ime_funckije():
        telo funkcije
    ```

* funkcija koja uzima argumente:

    ```python
    def ime_funckije(argumenti):
        telo funkcije
    ```

## Primeri funkcija

```python
def pozdrav():
    print('Zdravo')

def pozdrav():
    print('******')
    print('Zdravo')
    print('******')

pozdrav()   # Zdravo 
```

**Telo funkcije se izvršava tek nakon poziva imenom i zagradama.**

## Funkcije sa jednim argumentom

Definisanje funkcije sa jednim argumentom:

```python
def pozdrav_ime(ime):
    print('******')
    print(f'Zdravo {ime}')
    print('******')
```

Poziv funkcije:

```python
pozdrav_ime('Janko')
```

Definisanje funkcije sa više argumenata:

```python
def pozdrav_i_ime(pozdrav, ime):
    print('*'*(1+ len(pozdrav) + len(ime)))
    print(f'{pozdrav} {ime}')
    print('*'*(1+ len(pozdrav) + len(ime)))
```

Poziv funkcije sa više argumenata:

```python
pozdrav_i_ime('Cao', 'Jelisaveta')       # Cao Jelisaveta
pozdrav_i_ime('Zdravo', 'Aleksandar')    # Zdravo Aleksandar
pozdrav_i_ime('Dobar dan', 'Grigorije')  # Dobar dan Grigorije
```

## Funkcije koje vraćaju vrednosti

Definisanje funkcije koja vraća vrednost glavnom programu:

```python
def dupla_vrednost(x):
    return 2 * x
```

Pozivanje funkcija koje vraćaju vrednosti:

```python
print(dupla_vrednost(2))   
print(dupla_vrednost(10))
print(dupla_vrednost(-2.3456)) 
print(dupla_vrednost('Zdravo svima'))
```

## Primeri funkcija koje vraćaju vrednosti

```python
def matematicka_funkcija(x, y):
    return 2*x - y

print(matematicka_funkcija(-2, 6))
print(matematicka_funkcija(2, 2))
print(matematicka_funkcija(0, 0))
print(matematicka_funkcija(9, -2))
```

```python
def povrsina_trougla(a, h):
    """Ova funkcija racuna povrsinu trougla."""
    povrsina = 0.5 * a * h
    return povrsina         # moze  i samo : return 0.5 * a * h

print(povrsina_trougla(3, 6))
print(help(povrsina_trougla))
```

## Lambda funkcije

* funkcije koje se pišu u jednoj liniji
* kao i obične, lambda funkcije mogu imati jedan ili više argumenata
* lambda funkcije nemaju ime
* koriste se za sortiranje i filtriranje u drugim tipovima podataka
  
Lambda funkcija sa jednim argumentom:

```python
h = lambda x: 3 * x + 1
print(h(3))
```

Lambda funkcija sa više argumenata:

```python
g = lambda x, y : 2*x - y
print(g(2,2))
```

Lambda funkcija sa stringovima:

```python
puno_ime = lambda ime, prezime : ime + " " + prezime
print(puno_ime('Goran', 'Mihajlovic'))
```

## Zadaci

### Zadatak 1

Napisati funkciju koja broji parne brojeve u datoj listi brojeva.

```python
def broj_parne(lista_brojeva):
    broj_parnih = 0
    for broj in lista_brojeva:
        if broj % 2 == 0:
            broj_parnih += 1    # isto sto i broj_parnih = broj_parnih + 1
    return broj_parnih

print(broj_parne([2, 1, 2, 4, 6]))
print(broj_parne([1, 3, 5]))
print(broj_parne([2, 2, 0]))
```

### Zadatak 2

Napisati funkciju koja za datu listu brojeva i ceo broj vraća Tačno (True) ako se dati broj nalazi na prvom ili poslednjem mestu liste.

```python
def prvi_zadnji(lista, broj):
    if broj == lista[0] or broj == lista[-1]:
        return True
    else:
        return False

print(prvi_zadnji([1, 2, 6], 6)) 
print(prvi_zadnji([8, 1, 2, 6], 8))
print(prvi_zadnji([0, 3, 4, 2], 4))
```

### Zadatak 3

Napisati funkciju koja uzima nisku i vraca novu nisku u kojoj su svi karakteri ispisani dva puta.

```python
def dupla_niska(niska):
    nova_niska = ""
    for slovo in niska:
        nova_niska += slovo*2
    return nova_niska
print(dupla_niska("Ana"))
print(dupla_niska("Zdravo"))
print(dupla_niska("Racunarski alati"))
```

### Zadatak 4

Napisati funkciju koja uzima listu celih brojeva i nalazi maksimalni član.

```python
def nadji_najveci(lista):
    najveci = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > najveci:
            najveci = lista[i]
    return najveci

print(nadji_najveci([1, 5, 7, 9, 10, 11, -4, 0, 2, 6, 8, 9, -7, 3])) 
print(nadji_najveci([3, 5, 1, -100, 8, -2, 6, 9, 0, 1, 0, 3, 5, 3, 6, 2, 2, 3, 1]))
```

### Zadatak 5

Napisati funkciju koja uzima listu celih brojeva i nalazi minimalni član.

```python
def nadji_najmanji(lista):
    najmanji = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < najmanji:
            najmanji = lista[i]
    return najmanji
print(nadji_najmanji([1, 5, 7, 9, 10, 11, -4, 0, 2, 6, 8, 9, -7, 3])) 
print(nadji_najmanji([3, 5, 1, -100, 8, -2, 6, 9, 0, 1, 0, 3, 5, 3, 6, 2, 2, 3, 1]))
```

### Zadatak 6

Napisati funkciju koja sortira listu brojeva u rastućem redosledu (od najmanjeg do najveceg člana).

```python
def sortiraj_rastuci(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
print(sortiraj_rastuci([1, 5, 7, 9, 10, 11, -4, 0, 2, 6, 8, 9, -7, 3]))
print(sortiraj_rastuci([3, 5, 1, -100, 8, -2, 6, 9, 0, 1, 0, 3, 5, 3, 6, 2, 2, 3, 1]))
```

### Zadatak 7

Napisati funkciju koja sortira listu brojeva u opadajućem redosledu (od najvećeg do najmanjeg člana).

```python
def sortiraj_opadajuci(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
print(sortiraj_opadajuci([1, 5, 7, 9, 10, 11, -4, 0, 2, 6, 8, 9, -7, 3]))
print(sortiraj_opadajuci([3, 5, 1, -100, 8, -2, 6, 9, 0, 1, 0, 3, 5, 3, 6, 2, 2, 3,1]))
```
