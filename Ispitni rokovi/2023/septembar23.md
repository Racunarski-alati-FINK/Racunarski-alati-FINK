# Python Septembarski ispitni rok 2023.

## Grupa 1
## Prvi zadatak
Napisati funkciju, koja preuzima celobrojni niz proizvoljne dužine i računa srednju vrednost članova većih od vrednosti zadate u glavnom programu. Funkcija glavnom programu vraća izračunatu srednju vrednost.
    primer: 
	         
  	A = [2, -4, 3, 5, 7]
	X = 5
	srednja_vrednost = 7.0

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A,X):
    broj = 0
    suma = 0
    for i in range(len(A)):
        if A[i] > X:
            suma += A[i]
            broj += 1
    return suma / broj

# glavni program:
print(f"Srednja vrednsot članova većih od X je {funkcija([2, -4, 3, 5, 7],5)}")
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [agencija.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Septembar/agencija.txt) koji sadrži spisak destinacija u formatu:

	Destinacija, Broj putnika, Cena
	Budimpešta, 50, 130
U izlazni fajl štampati destinacije sortirane u rastućem redosledu po ukupnoj zaradi po aranžmanu (broj putnika * cena)

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
spisak = []
with open ('agencija.txt', 'r') as fajl:
    for linija in fajl:
        destinacija, br_putnika, cena  = linija.lstrip().rstrip().split(',')
        ukupno_cena = int(br_putnika) * float(cena)
        aranzmani = {'destinacija':destinacija, 'ukupno cena':ukupno_cena}
        spisak.append(aranzmani)
    
with open('rezultat_5a.txt', 'w') as fajl:
    for item in sorted(spisak, key = lambda aranzmani:aranzmani['ukupno cena']):
        fajl.write(f"{item['destinacija']}, {item['ukupno cena']}\n")
```
</details>

# Grupa 2
## Prvi zadatak
Napisati funkciju, koja preuzima celobrojni niz proizvoljne dužine i računa proizvod svih članova većih od srednje vrednosti niza. Funkcija glavnom programu vraća izračunati proizvod.
primer: 
    
    A = [2, -4, 3, 5, 7]
    proizvod = 105   

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A):
    broj = 0
    suma = 0
    for i in range(len(A)):
        suma += A[i]
        broj += 1
    srednja_vrednost = suma/broj  # ako nije naglašeno može i sum(A)/len(A)
    proizvod = 1
    for i in range(len(A)):
        if A[i] > srednja_vrednost:
           proizvod *= A[i]

    return proizvod

# glavni program:
print(f"Proizvod članova većih od srednje vrednosti je {funkcija([2, -4, 3, 5, 7])}")
```
</details>

## Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak) grupe 1.