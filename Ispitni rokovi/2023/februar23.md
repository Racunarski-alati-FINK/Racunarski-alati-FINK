# Python Februarski ispitni rok 2023.

## Grupa 1a
## Prvi zadatak
Napisati funkciju koja uzima niz celih brojeva A i ceo broj X, a zatim računa srednju vrednost članova manjih od X i najmanju vrednost u nizu. 
Funkcija glavnom programu vraća razliku srednje vrednosti članova manjih od X i najmanje vrednosti niza

primer: 

	A = [1, 2, -3, 4, -5]
    razlika = 3.75


<details markdown='block'>
<summary>Rešenje </summary>

```python
def funkcija(A,X):
    suma = 0
    br = 0
    for i in range(len(A)):
        if A[i] < X:
            suma += A[i]
            br += 1
    srednja_vrednost = suma/br
    min = A[0]
    for i in range(1,len(A)):
        if A[i] < min:
            min = A[i]
    return srednja_vrednost - min


# poziv glavnog programa
print(funkcija([1, 2, -3, 4, -5],4)
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [bioskop.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Februar/bioskop.txt) koji sadrži spisak filmova formatu:

    naziv filma,vreme početka, trajanjae (min)
    Avatar, 14:52, 130
U izlazni fajl štampati nazive filmova sortirane u rastućem redosledu po vremenu završetka.

<details markdown='block'>
<summary>Rešenje </summary>
	
```python
spisak = []
with open ('bioskop.txt','r') as fajl:
    for linija in fajl:
        naziv_filma, vreme_pocetka, trajanje = linija.lstrip().rstrip().split(',')   
        sati, minuti = vreme_pocetka.split(':')
        ukupno_vreme = int(sati) * 60 + int(minuti) + int(trajanje)
        film = {'naziv_filma':naziv_filma, 'vreme_zavrsetka':ukupno_vreme}
        spisak.append(film)
```
</details>

## Grupa 1b
## Prvi zadatak
Napisati funkciju koja uzima niz realnih brojeva A i ceo broj X, a zatim računa zbir svih članova većih od X i proizvod članova manjih od X. Funkcija glavnom programu vraća razliku sračunatih vrednosti za sumu i proizvod
primer: 

  	A = [1, 2, -3, 4, -5]
	razlika = -30

<details markdown='block'>
<summary>Rešenje </summary>

```python
def funkcija(A,X):
    suma = 0
    proizvod = 1
    for i in range(len(A)):
        if A[i] > X:
            suma += A[i]
        elif A[i] < X:
            proizvod *= A[i]
    return suma - proizvod

# poziv glavnog programa
print(funkcija([1,2,-3,4,-5],4))
```
</details>

## Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak) grupe 1a.

## Grupa 2a
## Prvi zadatak
Napisati funkciju koja uzima dva niza celih brojeva A i B i 
formira treći niz C tako što na i-tom mestu 
postavlja manji od dva člana A[i] i B[i].
Funkcija glavnom programu vraća niz C sortiran u rastućem redosledu.
_Napomena: Ne koristiti metod i funkciju za sortiranje_
primer: 

  	A = [1, 2, -3, 4, -5]
        B = [-1, -2, 3, -4, 5]
	C = [-5, -4, -3, -2, -1]

<details markdown='block'>
<summary>Rešenje korišćenjem funkcije min() </summary>

```python
def funkcija(A,B):
    C = []
    for i in range(len(A)):
        C.append(min(A[i],B[i]))

    for i in range(0, len(C)-1):        # petlje za sortiranje
        for j in range(i+1,len(C)):
            if C[i] > C[j]:
                pomocna = C[i]
                C[i] = C[j]
                C[j] = pomocna
    return C
# glavni program:
print(funkcija([1, 2, -3, 4, -5], [-1, -2, 3, -4, -5]))
```
</details>

<details markdown='block'>
<summary>Rešenje bez funkcije min() </summary>

```python
def funkcija(A,B):
    C = []
    for i in range(len(A)):
        if A[i] < B[i]:
            C.append(A[i])
        else:
            C.append(B[i])

    for i in range(0, len(C)-1):        # petlje za sortiranje
        for j in range(i+1,len(C)):
            if C[i] > C[j]:
                pomocna = C[i]
                C[i] = C[j]
                C[j] = pomocna
    return C
        
# glavni program:
print(funkcija([1, 2, -3, 4, -5], [-1, -2, 3, -4, -5]))
```
</details>

## Drugi zadatak 
Napisati program koji otvara fajl [nabavka.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Februar/nabavka.txt) koji sadrži spisak robe u formatu:

	Naziv artikla, Cena po komadu, Broj komada
	secer, 100, 7
 
U izlazni fajl štampati sortirane nazive artikala u rastućem poretku po ukupnoj ceni nabavke. 

<details markdown='block'>
<summary>Rešenje </summary>

```python
spisak = []
with open ('nabavka.txt', 'r') as fajl:
    for linija in fajl:
        artikal, cena_po_komadu, br_komada = linija.lstrip().rstrip().split(',')
        ukupna_vrednost = float(cena_po_komadu) * float(br_komada)
        artikli = {'artikal':artikal,'ukupna_vrednost':ukupna_vrednost}
        spisak.append(artikli)

with open('rezultat_2a.txt', 'w') as fajl:
    for item in sorted(spisak, key = lambda artikli:artikli['ukupna_vrednost']):
        fajl.write(f"{item['artikal']}, {item['ukupna_vrednost']}\n")
# ukupna vrednost nije bila obavezna da se štampa
```
</details>

## Grupa 2b
## Prvi zadatak
Napisati funkciju koja uzima dva niza celih brojeva A i B i 
formira treći niz C tako što na i-tom mestu 
postavlja manji od dva člana A[i] i B[i].
Funkcija glavnom programu vraća niz C sortiran u opadajućem redosledu.
_Napomena: Ne koristiti metod i funkciju za sortiranje_
primer: 

  	A = [1, 2, -10, 4, -5]
        B = [-1, -2, 3, -4, 5]
	C = [-1, -2, -4, -5, -10]

<details markdown='block'>
<summary>Rešenje korišćenjem funkcije min() </summary>

```python
def funkcija(A,B):
    C = []
    for i in range(len(A)):
        C.append(min(A[i],B[i]))

    for i in range(0, len(C)-1):        # petlje za sortiranje
        for j in range(i+1,len(C)):
            if C[i] < C[j]:
                pomocna = C[i]
                C[i] = C[j]
                C[j] = pomocna
    return C
# glavni program:
print(funkcija([1, 2, -10, 4, -5], [-1, -2, 3, -4, -5]))
```
</details>

<details markdown='block'>
<summary>Rešenje bez funkcije min() </summary>

```python
def funkcija(A,B):
    C = []
    for i in range(len(A)):
        if A[i] < B[i]:
            C.append(A[i])
        else:
            C.append(B[i])

    for i in range(0, len(C)-1):        # petlje za sortiranje
        for j in range(i+1,len(C)):
            if C[i] < C[j]:
                pomocna = C[i]
                C[i] = C[j]
                C[j] = pomocna
    return C
        
# glavni program:
print(funkcija([1, 2, -10, 4, -5], [-1, -2, 3, -4, -5]))
```
</details>

## Drugi zadatak 
Videti [drugi zadatak](#drugi-zadatak-2) grupe 2a.

## Grupa 3a
## Prvi zadatak
Napisati funkciju koja uzima niz celih brojeva A, pronalazi najmanji parni element niza i najveći element sa neparnim indeksom. Funkcija glavnom programu vraća razliku najvećeg i najmanjeg elementa.
    	primer: 
	 	
   		A = [1, 2, -3, -4, -5]
		razlika = 6

<details markdown='block'>
<summary>Rešenje (nesavršeno) </summary>

```python
def funkcija(A):
	minimum = A[0]  # pretpostavka da je prvi član minimalan - greška ako ne postoji manji a parni član, ako je prvi npr neparan
					# može se pretpostaviti da je neki mnogo veliki broj minimalan npr min = 100e100
    maximum = A[0]	# pretpostavka da je prvi član maksimalan
    for i in range(len(A)):
        if A[i] % 2 == 0 and A[i] < minimum:
            minimum = A[i]
  
        if  i % 2 != 0 and A[i] > maximum:
            maximum = A[i]
    print(minimum)
    print(maximum)
    rezultat = maximum - minimum
    return rezultat
# glavni program:
print(funkcija([1, 2, -3, -4, -5]))
```
</details>

<details markdown='block'>
<summary>Tačnije rešenje</summary>

```python
	minimum = None					# pretpostavka da su minimum i maximum None
    maximum = None
    for i in range(len(A)):
        if A[i] % 2 == 0 and (minimum is None or A[i] < minimum):
            minimum = A[i]
  
        if  i % 2 != 0 and (maximum is None or A[i] > maximum):
            maximum = A[i]
    print(minimum)
    print(maximum)
    rezultat = maximum - minimum
    return rezultat
        
# glavni program:
print(funkcija([1, 2, -3, -4, -5]))
```
</details>

## Drugi zadatak 
Napisati program koji otvara fajl [test.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Februar/test.txt) koji sadrži spisak studenata u formatu:

	Ime i prezime, broj tačnih odgovora, broj netačnih odgovora
	Petar Petrović, 23, 7
 
U izlazni fajl štampati spisak studenata koji su položili test u opadajućem poretku po sumi bodova 
(test je položen ako je br_tačnih – br netačnih >= 15

<details markdown='block'>
<summary>Tačnije rešenje</summary>

```python

polozili = []
nisu_polozili = []

with open ('test.txt', 'r') as fajl:
    for linija in fajl:
        ime_prezime, br_tacnih, br_netacnih  = linija.lstrip().rstrip().split(',')
        rezultat = int(br_tacnih) - int(br_netacnih)
        if rezultat >= 15:
            studenti_polozili = {'ime i prezime':ime_prezime, 'rezultat':rezultat}
            polozili.append(studenti_polozili)
        else:
            studenti_nisu_polozili = {'ime i prezime':ime_prezime, 'rezultat':rezultat}
            nisu_polozili.append(studenti_nisu_polozili)
    
with open('rezultat_3a_polozili.txt', 'w') as fajl:
    for student in sorted(polozili, key = lambda studenti_polozili:studenti_polozili['rezultat']):
        fajl.write(f"{student['ime i prezime']}, {student['rezultat']}\n")

with open('rezultat_3a_nisu_polozili.txt', 'w') as fajl:
    for student in sorted(nisu_polozili, key = lambda studenti_polozili:studenti_polozili['rezultat']):
        fajl.write(f"{student['ime i prezime']}, {student['rezultat']}\n")
```
</details>

## Grupa 3b
## Prvi zadatak
Napisati funkciju koja uzima niz celih brojeva A, pronalazi najmanji neparni element niza i najveći element sa parnim indeksom. Funkcija glavnom programu vraća razliku najvećeg i najmanjeg elementa.

    	primer: 
	 	
   		A = [1, 2, -3, -4, 5]
		razlika = 8

<details markdown='block'>
<summary>Rešenje (nesavršeno) </summary>

```python
def funkcija(A):
	minimum = A[0]  # pretpostavka da je prvi član minimalan - greška ako ne postoji manji a neparni član, ako je prvi npr paran
					# može se pretpostaviti da je neki mnogo veliki broj minimalan npr min = 100e100
    maximum = A[0]	# pretpostavka da je prvi član maksimalan
    for i in range(len(A)):
        if A[i] % 2 != 0 and A[i] < minimum:
            minimum = A[i]
  
        if  i % 2 == 0 and A[i] > maximum:
            maximum = A[i]
    print(minimum)
    print(maximum)
    rezultat = maximum - minimum
    return rezultat
# glavni program:
print(funkcija([1, 2, -3, -4, 5]))
```
</details>

<details markdown='block'>
<summary>Tačnije rešenje</summary>

```python
def funkcija(A):
	minimum = None					# pretpostavka da su minimum i maximum None
    maximum = None
    for i in range(len(A)):
        if A[i] % 2 != 0 and (minimum is None or A[i] < minimum):
            minimum = A[i]
  
        if  i % 2 == 0 and (maximum is None or A[i] > maximum):
            maximum = A[i]
    print(minimum)
    print(maximum)
    rezultat = maximum - minimum
    return rezultat
        
# glavni program:
print(funkcija([1, 2, -3, -4, 5]))
```
</details>

## Drugi zadatak 
Videti [drugi zadatak](#drugi-zadatak-4) grupe 3a.

# Grupa 4a

## Prvi zadatak
Napisati funkciju koja uzima niz realnih brojeva A i sve negativne parne članove niza pretvara u pozitivne i štampa novodobijeni niz. Funkcija glavnom programu vraća broj pretvorenih članova.
    primer: 
	         
	  	A = [1, -2, 3, 4, -5]
		novo_A = [1, 2, 3, 4,-5]
		broj = 1

<details markdown='block'>
<summary>Rešenje</summary>

```python
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

# glavni program:
print(f"Broj izmenjenih članova je {funkcija([1, -2, 3, 4, -5])}")
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [fakture.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Februar/fakture.txt) koji sadrži spisak klijenata u formatu:

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


