# Python Avgustovski ispitni rok 2023.

## Grupa 1
## Prvi zadatak
Napisati funkciju koja uzima niz realnih brojeva A i sve negativne parne članove niza pretvara u pozitivne i štampa novodobijeni niz. Funkcija glavnom programu vraća broj pretvorenih članova.
    primer: 
	         
  	A = [1, -2, 3, 4, -5]
	novo_A = [1, 2, 3, 4,-5]
	broj = 1

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A):
    broj = 0
    print(f"Polazni niz je: {A}")
    for i in range(len(A)):
        if A[i] < 0 and A[i] % 2 == 0:
            A[i] = -1 * A[i]
            broj += 1
    print(f"Krajnji niz je: {A}")
    return broj

# glavni program:
print(f"Broj izmenjenih članova je {funkcija([1, -2, 3, 4, -5])}")
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [fakture.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Avgust/fakture.txt) koji sadrži spisak klijenata u formatu:

	klijent, broj porudžbina, promet
	Kompanija1, 17, 50000
 
U izlazni fajl štampati spisak klijenata koji su ostvarili pravo na rabat od 10% (rabat je ostvaren ako su imali više od deset porudžbina) sa novodobijenim prometom sortirano po prometu u opadajućem poretku.

<details markdown='block'>
<summary>Rešenje</summary>

```python
spisak = []
with open ('fakture.txt', 'r') as fajl:
    for linija in fajl:
        klijent, broj_porudzbina, promet = linija.rstrip().lstrip().split(',')
        if int(broj_porudzbina) > 10:
            promet = float(promet) * 0.9
            klijenti = {'klijent':klijent, 'promet':promet}
            spisak.append(klijenti)
    print(spisak)

with open('rezultat_4a.txt', 'w') as fajl:
    for item in sorted(spisak, key = lambda klijenti:klijenti['promet']):
        fajl.write(f"{item['klijent']}, {item['promet']}\n")
```
</details>

# Grupa 2
## Prvi zadatak
Napisati funkciju koja uzima niz realnih brojeva A i sve pozitivne neparne članove niza pretvara u negativne i štampa novodobijeni niz. Funkcija glavnom programu vraća broj pretvorenih članova.
    primer: 
	         
    A = [1, -2, 3, 4, -5]
	novo_A = [-1, -2, -3, 4,-5]
	broj = 2


<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A):
    broj = 0
    print(f"Polazni niz je: {A}")
    for i in range(len(A)):
        if A[i] > 0 and A[i] % 2 != 0:
            A[i] = -1 * A[i]
            broj += 1
    print(f"Krajnji niz je: {A}")
    return broj

# glavni program:
print(f"Broj izmenjenih članova je {funkcija([1, -2, 3, 4, -5])}")
```
</details>

## Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak) grupe 1.
