# Python Januarski ispitni rok 2023.

## Grupa 1a
## Prvi zadatak
Napisati funkciju koja uzima dva niza celih brojeva A i B I računa treći niz C kao zbir članova nizova A i B, po formuli C(i) = A(i) + B(i). Funkcija glavnom programu vraća srednju vrednost niza C

primer: 

	A = [1, 2, 3, 4, 5]
	B = [-1, -2, -3, -4, 5]
	srednja_vrednost = 2


<details markdown='block'>
<summary>Rešenje </summary>

```python
def funkcija(A,B):
	C = []
	for i in range(len(A)):
        C.append(A[i]+B[i])

    suma = 0

    for i in range(len(C)):
        suma += C[i]
    srednja_vrednost = suma/len(C)
    # a može i srednja_vrednost = sum(C)/len(C)
	
    return srednja_vrednost

# poziv glavnog programa
print(funkcija([1, 2, 3, 4, 5], [-1, -2, -3, -4, 5]))
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [listing.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Januar/listing.txt) koji sadrži spisak brojeva telefona u formatu:  

    broj telefona, broj sms poruka, trajanje poziva
    0601112223, 252, (7:32)

U izlazni fajl štampati broj sa kojim je razmenjeno najviše poruka, i ukupne troškove za sve razgovore i sms poruke. Cena sms poruke je 15 dinara a cena poziva 4 din/sekunda

Primer:
    
    listing.txt

    0601112223, 252, (7:32)
    0611112223, 300, (8:00)
    0621112223, 180, (10:15)

    rezultat.txt

    Broj sa kojim je razmenjeno najviše poruka (300) je 0611112223, a ukupni troškovi za sve razgovore i sms poruke su 17168 din.

<details markdown='block'>
<summary>Rešenje</summary>

	
```python
maks_poruka_broj = 0
ukupni_troskovi = 0

with open('listing.txt') as fajl:
    for linija in fajl:
        broj_telefona, broj_sms, trajanje = linija.lstrip().rstrip().split(',')
        minuti, sekunde = trajanje.lstrip().lstrip('(').rstrip(')').split(':')
        broj_sms = int(broj_sms)
        ukupno_vreme = int(minuti) * 60 + int(sekunde)
        trosak = ukupno_vreme * 4 + int(broj_sms) * 15
        ukupni_troskovi += trosak

        if int(broj_sms) > maks_poruka_broj:
            maks_poruka_broj = broj_sms
            broj_sa_najvise_poruka = broj_telefona
        
with open('rezultat.txt', 'w') as fajl:
        fajl.write(f"Broj sa kojim je razmenjeno najviše poruka ({maks_poruka_broj}) je {broj_telefona}, a ukupni troškovi za sve razgovore i sms poruke su {ukupni_troskovi} din.")
```
</details>

# Grupa 1b
## Prvi zadatak
Napisati funkciju koja uzima dva niza celih brojeva A i B I računa treći niz C kao proizvod članova nizova A i B, po formuli C(i) = A(i) * B(i). Funkcija glavnom programu vraća niz C sortiran u rastućem redosledu.
_Napomena: Nije dozvoljeno korišćenje metoda ili funkcija za sortiranje._

Primer: 
        
    A = [1, 2, 3, 4, 5]
	B = [-1, -2, -3, -4, 5]
	C = [-16, -9, -4, -1, 25]

<details markdown='block'>
<summary>Rešenje</summary>

	
```python
def funkcija(A,B):
    C = []
    for i in range(len(A)):
        C.append(A[i]*B[i])

    for i in range(len(C)-1):
        for j in range(i+1, len(C)):
            if C[i] > C[j]:
                pomocna = C[i]
                C[i] = C[j]
                C[j] = pomocna
    return C

# glavni program
print(funkcija([1, 2, 3, 4, 5], [-1, -2, -3, -4, 5]))

```
</details>

## Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak) grupe 1a.

# Grupa 2a
## Prvi zadatak
Napisati funkciju koja od glavnog programa preuzima celobrojni niz proizvoljne dužine, sumira parne članove i množi negativne članove. Funkcija glavnom program vraća uređeni par (suma, proizvod)
    
primer: 

    A = [1, 2, -3, 4, -5]
	suma = 6
 	proizvod = 15

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(A):
    suma = 0
    proizvod = 1
    for i in range(len(A)):
        if A[i] % 2 == 0:
            suma += A[i]
        if A[i] < 0:
            proizvod *= A[i]
	return (suma,proizvod)
# glavni program

print(funkcija([1, 2, -3, 4, -5])

```
</details>

## Drugi zadatak 

Napisati program koji otvara fajl [raspored.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Januar/raspored.txt) koji sadrži dnevni raspored filmova u bioskopu u formatu:

    naziv filma,vreme početka, dužina trajanja
    Avatar 2,17:45,218

U izlazni fajl štampati spisak filmova koji se završavaju posle 22:00.

Primer:

    raspored.txt

    Avatar 2,17:45,218
    Kum,18:00,175
    Hari Poter i kamen mudrosti,20:00,152
    rezultat.txt
    Hari Poter i kamen mudrosti


<details markdown='block'>
<summary>Rešenje</summary>
	
```python

spisak = []

with open('filmovi.txt') as fajl:
    for linija in fajl:
        film, pocetak, trajanje = linija.lstrip().rstrip().split(',')
        sati, minuti = pocetak.lstrip().split(':')
        sati, minuti, trajanje = int(sati), int(minuti), int(trajanje)
        vreme_pocetka = sati * 60 + minuti
        vreme_zavrsetka = vreme_pocetka + trajanje
        
        if vreme_zavrsetka > 22*60:
            spisak.append(film)
        
with open('rezultat_2a.txt', 'w') as fajl:
        for i in range(len(spisak)):
            fajl.write(spisak[i] + "\n")

```
</details>

# Grupa 2b
## Prvi zadatak
Napisati funkciju koja od glavnog programa preuzima celobrojni niz proizvoljne dužine, i računa razliku proizvoda i sume svih članova čija je vrednost manja od srednje vrednosti niza. Funkcija glavnom programu vraća izračunatu razliku.   

primer: 
	
 	A = [1, 2, 3, 4, 5]
    srednja_vrednost = 3
    suma = 3
    proizvod = 2
    razlika = proizvod - suma
  

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A):
	suma = 0
    for i in range(len(A)):
        suma += A[i]
	srednja_vrednost = suma / len(A)   # ili srednja_vrednost = sum(A)/len(A)

	suma = 0
	proizvod = 1

	for i in range(len(A)):
		if A[i] < srednja_vrednost:
			suma += A[i]
			proizvod *= A[i]
    return srednja_vrednost

# glavni program
print(funkcija([1, 2, 3, 4, 5]))
```
</details>

# Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak-2) grupe 2a.

# Grupa 2c
## Prvi zadatak
Napisati funkciju koja od glavnog programa preuzima celobrojni niz proizvoljne dužine i računa razliku proizvoda i sume članova čija je vrednost manja od vrednosti zadate u glavnom programu. 
Funkcija glavnom programu vraća izračunatu razliku.  

primer: 

	A = [1, 2, 3, 4, 5]
	suma = 12
	proizvod = 60
	razlika = proizvod - suma


<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A,X):
	proizvod = 1
	suma = 0
	for i in range(len(A)):
		if A[i] > X:
			suma += A[i]
			proizvod *= A[i]
	razlika = proizvod - suma
	return razlika
    
#pozivanje glavnog programa
print(funkcija([1, 2, 3, 4, 5],2))
```
</details>

# Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak-2) grupe 2a.

# Grupa 3a
## Prvi zadatak
Napisati funkciju koja uzima niz realnih brojeva A i prepakuje niz tako da redosled članova niza bude suprotan redosledu prilikom učitavanja 
niza u glavnom programu (prvi član postaje poslednji, drugi član postaje pretposlednji itd.). Funkcija glavnom programu vraća novoformirani niz
primer: 

	A = [1, 2, -3, 4, -5]
	A_novi = [-5, 4, -3, 2, 1]

<details markdown='block'>
<summary>Rešenje korišćenjem isecanja</summary>
	
```python
def funkcija(A):
	A_novi = A[::-1]
	return A_novi
#pozivanje glavnog progam
print(funkcija([1, 2, -3, 4, -5]))
```
</details>

<details markdown='block'>
<summary>Rešenje korišćenjem for petlje</summary>
	
```python
def funkcija(A):
    A_novi = []
    for i in range(len(A)):
        A_novi.append(A[len(A)-i-1])
    return A_novi
#pozivanje glavnog progam
print(funkcija([1, 2, -3, 4, -5]))
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [dostavnica.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Januar/dostavnica.txt) sa spiskom dostava jedne firme u toku jednog dana u formatu:

	tip vozila, registracija, predjeni kilometri, broj dostava
	Reno twingo, KG111HH, 342, 12

U izlazni fajl štampati spisak vozila sortiranih po profitu ostvarenom tog dana. Predjeni kilometar košta 34 dinara a svaka dostava vredi 250 dinara.

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
spisak = []

with open('dostavnica.txt') as fajl:
    for linija in fajl:
        tip_vozila, registracija, predjeni_km, br_dostava = linija.lstrip().rstrip().split(',')
        profit = int(br_dostava) * 250 - int(predjeni_km)*34
        vozilo = {'tip_vozila':tip_vozila, 'registracija':registracija, 'profit':profit}
        spisak.append(vozilo)
        
with open('rezultat_3a.txt', 'w') as fajl:
        for vozilo in sorted(spisak, key = lambda vozilo:vozilo['profit'], reverse=True):
             fajl.write(f"{vozilo['tip_vozila']}, {vozilo['registracija']}, {vozilo['profit']}\n")
```
</details>

# Grupa 3b
## Prvi zadatak
Napisati funkciju koja uzima niz realnih brojeva i transformiše niz zamenom mesta parovima uzastopnih vrednosti ako važi uslov da je x[i] < x[i+1]. Funkcija glavnom program vraća izmenjeni niz.    
primer:     

	X = [1, 2, -3, 4, -5, 6]
	X_novo = [2, 1, 4, -3, 6, -5]

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(X):
    for i in range(0,len(X),2):
        if X[i] < X[i+1]:
            pomocna = X[i]
            X[i] = X[i+1]
            X[i+1] = pomocna
    return X
#glavni program
print(funkcija([1, 2, -3, 4, -5, 6]))
```
</details>

# Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak-4) grupe 3a.

# Grupa 3c
## Prvi zadatak
Napisati funkciju koja preuzima celobrojni niz i neparnim brojevima 
dodeljuje vrednost 0. Funkcija glavnom program vraća procenat članova koji su jednaki 0.

primer

  	X = [1, 2, -3, 4, 5] 
 	X_novo = [0, 2, 0, 4, 0]  => 60 %

<details markdown='block'>
<summary>Rešenje</summary>
	
```python

def funkcija(X):
        br = 0
    for i in range(0,len(X)):
        if X[i] %2 != 0:
            X[i] = 0
            br += 1
    procenat = 100 * br/len(X)
    print("Novi niz je ", X)
    return str(procenat) + ' %' # vraća "procenat" kao string i dodaje znak %
	
#glavni program
print(funkcija([1, 2, -3, 4, 5]))
```
</details>

## Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak-4) grupe 3a.

# Grupa 3d
## Prvi zadatak
Napisati funkciju koja preuzima celobrojni niz i pozitivnim brojevima 
dodeljuje vrednost 0. Funkcija glavnom program vraća procenat članova koji su jednaki 0.

primer:

	X = [1, 2, -3, 4, -5] 
 	X_novo = [0, 0, -3, 4, -5]  => 60 %

<details markdown='block'>
<summary>Rešenje</summary>
	
```python

def funkcija(X):
        br = 0
    for i in range(0,len(X)):
        if X[i] > 0:
            X[i] = 0
            br += 1
    procenat = 100 * br/len(X)
    print("Novi niz je ", X)
    return str(procenat) + ' %' # vraća "procenat" kao string i dodaje znak %
	
#glavni program
print(funkcija([1, 2, -3, 4, -5]))
```
</details>

## Drugi zadatak
Videti [drugi zadatak](#drugi-zadatak-4) grupe 3a.

