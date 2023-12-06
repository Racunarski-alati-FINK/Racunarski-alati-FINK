# Python Septembarski ispitni rok 2023.

## Grupa 1
## Prvi zadatak
Napisati funkciju, koja kao argument uzima matricu, pravi niz članova iznad glavne dijagonale i niz članova ispod glavne dijagonale. Funkcija glavnom programu vraća proizvod suma kreiranih nizova.
    primer: 

    [[5 4 3 6]
     [4 3 2 5]
     [6 5 4 3]
     [2 5 4 3]]

    [4, 3, 6, 2, 5, 3] - članovi iznad glavne dijagonale
    [4, 6, 5, 2, 5, 4] - članovi ispod glavne dijagonale
    proizvod_sume = 598
    

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A):
    suma_iznad = 0
    suma_ispod = 0
    for i in range(len(A)):
        for j in range(len(A[0])):          
            if i > j:
                suma_iznad += A[i][j]
            if i < j:
                suma_ispod += A[i][j]

    return suma_iznad * suma_ispod

#glavni program:

print(funkcija([[5,4,3,6],[4,3,2,5],[6,5,4,3],[2,5,4,3]])) 
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [agencija.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Oktobar/agencija.txt) koji sadrži spisak destinacija u formatu:

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
Napisati funkciju, koja kao argument uzima matricu, pravi niz članova iznad glavne dijagonale i niz članova od glavne dijagonale. Funkcija glavnom programu vraća proizvod suma kreiranih nizova
primer: 
    
    [[5 4 3 6]
     [4 3 2 5]
     [6 5 4 3]
     [2 5 4 3]]

    [4, 3, 6, 2, 5, 3] - članovi iznad glavne dijagonale
    [5, 3, 4, 3] - članovi glavne dijagonale
    proizvod_sume = 390   

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A):
    suma_iznad = 0
    suma_glavne = 0
    for i in range(len(A)):
        for j in range(len(A[0])):          
            if i > j:
                suma_iznad += A[i][j]
            if i == j:
                suma_glavne += A[i][j]

    return suma_iznad * suma_glavne

#glavni program:

print(funkcija([[5,4,3,6],[4,3,2,5],[6,5,4,3],[2,5,4,3]])) 

```
</details>

## Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak) grupe 1.