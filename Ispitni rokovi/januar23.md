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
Napisati program koji otvara fajl [listing.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/Januar%202023/listing.txt) koji sadrži spisak brojeva telefona u formatu:  

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

Napisati program koji otvara fajl [raspored.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/Januar%202023/raspored.txt) koji sadrži dnevni raspored filmova u bioskopu u formatu:

    naziv filma,vreme početka, dužina trajanja
    Avatar 2, 17:45, 218

U izlazni fajl štampati spisak filmova koji se završavaju pre 22:00.

Primer:

    raspored.txt

    Avatar 2, 17:45, 218
    Kum, 18:00, 175
    Hari Poter i kamen mudrosti, 20:00, 152
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
Napisati program koji otvara fajl [dostavnica.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/Januar%202023/dostavnica.txt) sa spiskom dostava jedne firme u toku jednog dana u formatu:

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

# Grupa 5a
## Prvi zadatak
Funkcija preuzima kvadratnu celobrojnu matricu.  
Od negativnih članova glavne dijagonale formira novi niz.  
Glavnom programu funkcija vraca broj članova i sumu novog niza.  
_Napomena: Pri racunanju duzine i sume novog niza ne koristiti sum i len._

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(matrica):
	suma = 0
	broj_clanova = 0
	novi_niz = []
    for i in range(len(matrica)):
        for j in range(len(matrica)):
            if i == j and matrica[i][j] < 0:
                novi_niz.append(matrica[i][j])
    for i in range(len(novi_niz)):
        broj_clanova += 1
        suma += novi_niz[i] 
    return suma, broj_clanova
# glavni program
print(funkcija([[6, 4, 1], [-5, -9, 0], [8, -2, -3]]))
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl koeficijenti.txt.  
Svaka linija fajla predstavlja jedan koeficijent u kvadratnoj jednacini.  
Koeficijente smestiti u listu koeficijenti.  

Program u izlazni fajl resenje.txt stampa dve linije:  
Koeficijenti a = {}, b = {} i c = {}  
Resenja x1 = {} i x2 = {}.   

Primer:

	koeficijenti.txt
	2
	4
	-3

	resenje.txt
	Koeficijenti a = 2, b = 4, c = -3
	Resenja x1 = 0.58113 , x2 = -2.5811 

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
koeficijenti = []
with open('ulaz5a.txt', 'r') as fajl:
    for linija in fajl:
        koeficijenti.append(int(linija))

a, b, c = koeficijenti

x1 = (-b+((b**2 - 4*a*c)**0.5))/(2*a)
x2 = (-b-((b**2 - 4*a*c)**0.5))/(2*a)

with open('izlaz5a.txt', 'w') as fajl:
    fajl.write(f"Koeficijenti a = {a}, b = {b} i c = {c}\n")
    fajl.write(f"Resenja x1 = {x1} i x2 = {x2}.") 
```
</details>

# Grupa 5b
## Prvi zadatak
Funkcija ucita celobrojni niz, i sve clanove koji su negativni  
zameni srednjom vrednoscu clanova niza. Srednju vrednost racunati bez koriscenja ugradjenjih funkcija sum i len.  
Funkcija vraca glavnom programu par (srednja_vrednost, niz)   

    Primer: niz = [1, -5, 6, 3, -1, 7, -1]
            suma = 10  
            brojac = 7 (broj clanova)  
            srednja_vrednost = 1.4285...

            => (1.4285..., [1, 1.4285, 6, 3, 1.4285, 7, 1.4285])
<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(niz):
    srednja_vrednost = 0
    suma = 0
    brojac = 0

    for i in range(len(niz)):
        suma += niz[i]
        brojac += 1

    srednja_vrednost = suma/brojac

    for i in range(len(niz)):
        if niz[i] < 0:
            niz[i] = srednja_vrednost

    return srednja_vrednost, niz

#glavni program

print(funkcija([1, -5, 6, 3, -1, 7, -1]))

```
</details>


## Drugi zadatak
Napisati progam koji otvara fajl glasovi.txt.  
Fajl sadrzi spisak kandidata za predsednika Studentskog parlamenta  
FINK u formatu:  

	ime kandidata,smer koji studira,glasovi sa MI,glasovi sa UI i IZZS, glasovi RTSI

U listu kandidati smestiti recnik za svakog kandidata  
 kandidat = {'ime':ime, 'smer':smer, 'glasovi':suma glasova sa svih smerova}  

Program kreira izlazni fajl rezultati.txt u svaka linija ima format:  

	redni broj (i+1), ime kandidata, smer, broj glasova

Kandidati u izlaznom fajlu su sortirani po broju osvojenih glasova.  

U poslednjoj liniji stampa se ime novog predsednika parlamenta:  

	Novi predsednik Studentskog parlamenta je {ime}. 

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
kandidati = []
with open('ulaz5b.txt', 'r') as fajl:
    for linija in fajl:
        ime, smer, glasovi_mi, glasovi_ui, glasovi_rtsi = linija.rstrip().split(',')
        glasovi = int(glasovi_mi) + int(glasovi_ui) + int(glasovi_rtsi)
        kandidat = {'ime':ime, 'smer':smer, 'glasovi':glasovi}

        kandidati.append(kandidat)

i = 0
with open('izlaz5b.txt', 'w') as fajl:
    for kandidat in sorted(kandidati, key=lambda kandidat:kandidat['glasovi'], reverse=True): 
        i += 1
        fajl.write(f'{i}, {kandidat["ime"]}, {kandidat["glasovi"]}\n')
    fajl.write(f'\n')
    fajl.write(f'Novi predsednik Studentskog parlamenta je {kandidati[0]["ime"]}.')
```
</details>

# Grupa 6a
## Prvi zadatak
Funkcija uzima niz celih brojeva i jedan ceo broj.
Funkcija poredi clanove niz sa prosledjenim brojem. 
Ukoliko je clan niza jednak broju indeks clana + 1 se 
dodaje na promenljivu brojilac, a ako clan nije
jednak broju njegov indeks + 1 se dodaje na promenljivu
imenilac. Funkcija vraca glavnom programu kolicnik.

Primer:

    niz = [-5, 4, 5, 4, 2]
    broj = 4

    4 se nalazi na indeksima 1 i 3 => brojilac = (1+1) + (3+1) = 6
    4 se ne nalazi na indeksima 0, 2, 4 => imenilac = (0+1) + (2+1) + (4+1) = 9

    rezultat => 6/9 = 0.666666

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(niz, broj):
    rezultat = 0
    brojilac = 0
    imenilac = 0

    for i in range(len(niz)):
        if niz[i] == broj:
            brojilac += i + 1
        else:
            imenilac += i + 1
    rezultat = brojilac / imenilac

    return rezultat

# glavni program
print(funkcija([-5, 4, 5, 4, 2], 4))
print(funkcija([-2, 4, 9, 3, 2, 3, 4, 6, 3], 3))
print(funkcija([0, 6, 1, 0, 8, 0, 4, 0, 2], 0))
print(funkcija([0, 1, 0, 1, 0, 0, 1, 1, 4], 1))
print(funkcija([5, 4, 5, 4, 7, 5, 0], 5))
print(funkcija([2, 8, 5, 4, 8, 6, 0, 8], 8))

```
</details>

## Drugi zadatak
Napisati program koji otvara fajl rezultati.txt  
u kome svaka linija sadrzi ime studenta i poene  
na prvom i drugom kolokvijumu u formatu:  

	ime studenta,poeni prvi kolokvijum,poeni drugi kolokvijum

Program čita fajl i kreira novi fajl u kome se  
štampaju imena studenata i suma poena ukoliko  
je student ostvario više od 30 poena na kolokvijumima.  
Format izlaznog fajla spisak.txt:  

	ime studenta,suma poena

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
studenti = []
with open('ulaz6a.txt', 'r') as fajl:
    for linija in fajl:
        ime, poeni1, poeni2 = linija.rstrip().split(',')
        poeni = int(poeni1) + int(poeni2)
        if poeni > 30:
            student = {'ime':ime, 'poeni':int(poeni1)+int(poeni2)}
            studenti.append(student)
        
with open('izlaz6b.txt', 'w') as fajl:
    for student in studenti:
        fajl.write(f"{student['ime']} {student['poeni']}\n")
```
</details>

## Grupa 6b
# Prvi zadatak
Funkcija uzima kvadratnu matricu (n x n).  
Glavnom programu vraća sumu ivičnih članova.  
Ivični ćlanovi su ćlanovi prvog reda, prve kolone,  
poslednjeg reda i poslednje kolone.  
Izbeci sumiranje dvostrukih (clanova u uglovima matrice).

 Primer:

        [ 3, 6,  1
    A =   7, 3,  9      => suma = 3 + 6 + 1 + 7 + 9 -1 + 5 + 11 = 41
         -1,  5, 11]

       [ 1, 1, 1, 1,
         1, 0, 0, 1,
    A =  1, 0, 0, 1,     => suma = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 12 
         1, 1, 1, 1]

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(matrica):
    suma = 0 

    for i in range(len(matrica)):
        if i == 0:
            suma += sum(matrica[i])
        elif i == len(matrica)-1:
            suma += sum(matrica[i])
        else:
            suma += matrica[i][0] + matrica[i][-1]
        

    return suma  

# glavni program
print(funkcija([[3, 6, 1], [7, 3, 9], [-1, 5, 11]]))
print(funkcija([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]))

```
</details>

## Drugi zadatak
Napisati program koji otvara fajl temperature.csv.  
Svaka linija fajla sadrzi podatke o temperaturama u nedelji u formatu:  

    dan;temperatura  
 
 Kreirati listu temperature koja sadrzi uredjene parove (dan, temperatura, osecaj).  
Promenljiva osecaj ima vrednost:  
 -'hladno' ako je temperatura <= 10  
 -'toplo' ako je tmeperatura > 10  

Program kreira izlazni fajl rezultat.txt gde je svaka linija formatirana:  

    dan,temperatura,osecaj 

<details markdown='block'>
<summary>Rešenje korišćenjem uređenih parova </summary>
	
```python

dani = []
with open('ulaz3a.txt', 'r') as fajl:
    for linija in fajl:
        dan, temperatura = linija.rstrip().split(';')
        if int(temperatura) <= 10:
            osecaj = 'hladno'
        else:
            osecaj = 'toplo'
        dani.append((dan, int(temperatura), osecaj))

with open('izlaz3a.txt', 'w') as fajl:
    for i in range(len(dani)):
        fajl.write(f"{dani[i][0]} {dani[i][1]} {dani[i][2]}\n")
```
</details>

<details markdown='block'>
<summary>Rešenje korišćenjem rečnika </summary>

```python 
dani = []
with open('ulaz3a.txt', 'r') as fajl:
    for linija in fajl:
        dan, temperatura = linija.rstrip().split(';')
        if int(temperatura) <= 10:
            osecaj = 'hladno'
        else:
            osecaj = 'toplo'
        dani.append({'dan':dan, 'temperatura':int(temperatura), 'osecaj':osecaj})

with open('izlaz3a.txt', 'w') as fajl:
    for dan in dani:
        fajl.write(f"{dan['dan']} {dan['temperatura']} {dan['osecaj']}\n")
```
</details>
