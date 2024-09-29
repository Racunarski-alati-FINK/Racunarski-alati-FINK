# Python II kolokvijum 2023.

## Grupa 1
## Prvi zadatak
Napisati funkciju koja vraća zbir cifara najviše četvorocifrenog broja

<details markdown='block'>
<summary>Rešenje </summary>

```python
def zbir_cifara(broj):
    if len(str(broj)) <= 4:
        jedinice = broj % 10
        desetice = (broj // 10) % 10
        stotine = (broj // 100) % 10
        hiljade = (broj // 1000) % 10
        zbir_cifara = jedinice + desetice + stotine + hiljade
    else: print("Broj ima više cifara od 4!")
    return zbir_cifara

# poziv glavnog programa
print(zbir_cifara(1234))
```
</details>

## Drugi zadatak
Napisati funkciju koja će za uneti niz A dimenzije N da formira niz B koji predstavlja „odraz u ogledalu“ niza A.

<details markdown='block'>
<summary>Rešenje </summary>

```python
def funkcija(A):
    B=[] 
    for i in range(0,len(A)):
        B.append(0)
    for i in range(0,len(A)):
        B[i]=A[len(A)-1-i]
    return(B)

# poziv glavnog programa
A = [1,2,3,4,5,6]
niz = funkcija(A)
print(f"Uneti niz: {A}, njegov odraz u ogledalu {niz}")
```
</details>


## Treći zadatak
Napisati program koji otvara fajl [agencija.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Februar/agencija.txt) koji sadrži spisak destinacija u formatu:

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
Napisati funkciju koja broj sekundi pretvara u dane, sate, minute i sekunde.

<details markdown='block'>
<summary>Rešenje</summary>
	
``` python
def prevedi_u_sekunde(vreme):
    dani = vreme // (24*3600)
    sati = vreme // 3600 % 24
    minuti = vreme // 60 % 60
    sekunde = vreme % 60
    print(f"{vreme} sekundi je jednako {dani} dana, {sati} sati, {minuti} minuta i {sekunde} sekundi.")

#glavni program:
prevedi_u_sekunde(12345678)
```
</details>

## Drugi zadatak
Napisati funkciju koja preuzeti niz iz glavnog programa A (n) postavlja za glavnu dijagonalu matrice B (n x n) pri čemu su ostali članovi matrice nule. Glavni program ispisuje niz A i matricu B.

	primer:
	A = [1, 2, 3, 4]
	------------
	Matrica B:
	[1, 0, 0, 0]
	[0, 2, 0, 0]
	[0, 0, 3, 0]
	[0, 0, 0, 4]

<details markdown='block'>
<summary>Rešenje</summary>
	
``` python
def funkcija(A):
    B=[]
    for i in range (0,len(A)):
        red=[]
        for j in range(0,len(A)):
            red.append(0)
        B.append(red)
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i==j:
                B[i][j]=A[i]
    return(B)
#glavni program

print(funkcija([1,2,3,4]))
```
</details>

## Treći zadatak
Napisati program koji otvara fajl [spisak.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Jul/spisak.txt) u kome svaka linija sadrži naziv proizvoda, količinu i cenu u formatu:

    namirnica, kolicina, cena

Program čita fajl i kreira novi fajl u kome se štampaju imena proizvoda i novac potrošen na tu namirnicu (količina*cena po komadu).
Format izlaznog fajla kupovina.txt:

    namirnica novac 
                                    
poslednja linija fajla je:    ukupno = suma potrošenog novca

<details markdown='block'>
<summary>Rešenje</summary>
  
```python
 def kupovina(ulaz):
     korpa = []
     suma = 0
     with open(ulaz, 'r') as fajl:
         for linija in fajl:
             namirnica, kolicina, cena = linija.rstrip().split(',')
             korpa.append((namirnica, int(kolicina)*int(cena)))
            
     with open('kupovina.txt', 'w') as fajl:
         for proizvod in korpa:
             suma += proizvod[1]
             fajl.write(f'{proizvod[0]} {proizvod[1]}\n')
         fajl.write(f'Ukupno = {suma}')
#glavni program:
kupovina('spisak.txt')
```
</details>

# Grupa 3
## Prvi zadatak
Funkcija uzima skup koeficijenata (Niz A, dimenzije n) i vrednost promenljive x i računa polinom: p(x) = a₀ + a₁x² + a₂x³ + a₃x⁴ + …

	koeficijenti: [1, 2, 3] 
  	x = 2
   	p(x) = 1 + 2 × 2² + 3 × 2³ = 1 + 8 + 24 = 33
<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(koeficijenti,x):
	stepen = 2
	polinom = koeficijenti[0]
	for koeficijent in koeficijenti:
		polinom = polinom + koeficijent * x ** stepen
		stepen = stepen + 1
	return polinom

#glavni program
print(funkcija([3, 5, 77, 1, 2, 8, 3],2)) # rešenje je 522
print(funkcija([2, 2, 2, 3, 4, 5],3)) # rešenje je 1615
print(funkcija([1, 2, 3],2))  # rešenje je 33
```
</details>
## Drugi zadatak
Napisati funkciju koja će za niz A dimenzije N da formira dva zasebna niza B i C i da izračuna razliku njihovih suma koja se ispisuje u glavnom programu. Niz B sadrži sve parne članove, dok niz C sadrži sve neparne članove niza A. Funkcija takođe ispisuje nizove B i C.

	primer:
 	A = [1,5,2,7,4]   →   B = [2, 4], C = [1, 5, 7], 
	sumaB = 2 + 4 = 6 
 	sumaC = 1 + 5 + 7 = 13, 
	razlika = sumaB – sumaC = 6 – 13 = -7
<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(A):
    B=[]
    C=[]
    sumaB=0
    sumaC=0
    N = len(A)  # dužina niza A
    for i in range(0,N):
        if A[i]%2==0:	#ako je broj paran (ostatak pri deljenju sa 2 je jednak nuli
            B.append(A[i])
            sumaB=sumaB+A[i]
        else:
            C.append(A[i])
            sumaC=sumaC+A[i]
    print(f"Niz B: {B}, niz C: {C}")
    razlika=sumaB-sumaC
    return razlika
#glavni program:
print(funkcija([1,5,2,7,4]))
```
</details>


## Treći zadatak 
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

# Grupa 4
## Prvi zadatak
Funkcija uzima skup koeficijenata (Niz A, dimenzije n) i vrednost promenljive x i računa polinom: p(x) = a₀ + 2a₁x³ + 4a₂x⁵ + 6a₃x⁷ + …

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A, x):
    polinom = A[0]  # Prvi koeficijent a₀
    for i in range(1, len(A)):
        result += (2 * i) * A[i] * x**(2 * i + 1)  # Računa svaki sledeći član
    return polinom
 

print(funkcija([2, 6, -7, 0, 1, 5], 4))
print(funkcija([5, 1, 8, -2, 7, -3, 10], 6))
```
</details>

## Drugi zadatak
Napisati funkciju koja preuzeti niz iz glavnog programa A (n) postavlja za sporednu dijagonalu matrice B (nxn), pri čemu su ostali članovi matrice nule. Glavni program ispisuje niz A i matricu B.

	primer:
	A = [1, 2, 3, 4, 5]

		[0, 0, 0, 0, 1]
		[0, 0, 0, 2, 0]
	B = [0, 0, 3, 0, 0]
		[0, 4, 0, 0, 0]
		[5, 0, 0, 0, 0]

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(A):
	B=[]
	N = len(A) 	#dužina niza A
	for i in range (0,N):
		red=[]
		for j in range(0,N):
			red.append(0)
		B.append(red)
	for i in range(0,N):
		for j in range(0,N):
			if i+j==N-1:
				B[i][j]=A[i]
    return(B)
 
# glavni program:
matrica = funkcija([1, 2, 3, 4, 5])
for red in matrica:
	print(red)
```
</details>

## Treći zadatak
Funkcija uzima fajl [studenti.txt]([https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Januar/raspored.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2023/studenti.txt) i ukupan broj studenata.

ime studenta;smer;poeni

ZADATAK: Kreirati listu studenata koji su polozili (preko 51 poen), Izracunati procenat studenata koji su polozili, Izracunati procenat studenata koji su izasli na ispit (50 studenata ukupno).
ZAPIS U NOVI FAJL: Lista studenata koji su polozili ispit – red po red u formatu: ime poeni, Procenat studenata koji su polozili, Procenat studenata koji su izasli na ispit.


<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(ulaz, ukupno):
    polozili = []
    br = 0
    izasli = 0
    with open (ulaz, 'r') as fajl:
        for linija in fajl:
            print(linija)
            ime, smer, poeni = linija.rstrip().lstrip().split(";")
            poeni = int(poeni)
            izasli+=1
            if poeni > 51:
                br +=1
                polozili.append((ime, poeni))
        procenat_polozili = br/ukupno * 100
        procenat_izasli = izasli/ukupno * 100

    with open("polozili.txt", 'w') as fajl:
        for student in polozili:
            fajl.write(f"{student[0]}, {student[1]}, polozilo: {procenat_polozili}%, izašlo: {procenat_izasli}% \n")

# glavni program:
funkcija("studenti.txt", 50)

```
</details>

# Grupa 5

## Prvi zadatak
Napisati funkciju koja uzima broj \(n\) koji predstavlja broj članova niza i računa vrednost niza prema formuli:

p = 1 + 4/2 + 7/3 + 10/4 + 13/5 + …

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(n):
    p = 1
    for i in range(2, n+1):
        p += i / (3*i - 2)
    return p

```
</details>
## Drugi zadatak
Napisati funkciju koja uzima dva niza A(n) i B(m) gde niz A predstavlja uneti niz brojeva, dok niz B predstavlja uneti niz redosleda članova i formira novi niz C od članova niza A, a po indeksima iz niza B.

	A = [4, 6, 1, 7]
 	B = [0, 3, 2, 2, 3, 1, 0]
  	C = [A[0], A[3], A[2], A[2], A[3], A[1], A[0]]
  	C = [4, 7, 1, 1, 7, 6, 4]


<details markdown='block'>
<summary>Rešenje</summary>

```python
def formiraj_niz(A, B):
    C = [A[i] for i in B]
    return C

# glavni program:
A = [4, 6, 1, 7]
B = [0, 3, 2, 2, 3, 1, 0]
C = formiraj_niz(A, B)
print(C)
```
</details>

## Treći zadatak
Napisati progam koji otvara fajl [glasovi_5b.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/glasovi_5b.txt).  
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
with open('glasovi_5b.txt', 'r') as fajl:
    for linija in fajl:
        ime, smer, glasovi_mi, glasovi_ui, glasovi_rtsi = linija.rstrip().split(',')
        glasovi = int(glasovi_mi) + int(glasovi_ui) + int(glasovi_rtsi)
        kandidat = {'ime': ime, 'smer': smer, 'glasovi': glasovi}
        kandidati.append(kandidat)

# Sortiranje kandidata po broju glasova opadajuće
kandidati = sorted(kandidati, key=lambda kandidat: kandidat['glasovi'], reverse=True)

# Upis rezultata u izlazni fajl
with open('izlaz_5b.txt', 'w') as fajl:
    i = 0
    for kandidat in kandidati:
        i += 1
        fajl.write(f'{i}, {kandidat["ime"]}, {kandidat["smer"]}, {kandidat["glasovi"]}\n') 
    fajl.write(f'\nNovi predsednik Studentskog parlamenta je {kandidati[0]["ime"]}.\n')
```
</details>

# Grupa 6
## Prvi zadatak
Napisati funkciju koja štampa histogram iz date liste A pomoću zadatog simbola 

	Primer:
	histogram([2,3,6,5], '*'):
	2: **
 	3: ***
 	6: ******
 	5: *****   

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def histogram(lista, simbol):
    for i in lista:
        print(f"{i}:", simbol*i)
        
# glavni program:        
histogram([2,3,6,5], '*')
histogram([2,3,6,5,4], '#')

```
</details>

## Drugi zadatak
Napisati funkciju koja crta „X“ unutar kvadratne matrice (nxn) pomocu slova X. Članovi u okolini „X“ su nule, dok je dimenzija n argument funkcije.

	    [X, 0, X]
	A = [0, X, 0]
	    [X, 0, X]

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(n):
    A=[]
    for i in range(0,n):
        red=[]
        for j in range(0,n):
            red.append(0)
        A.append(red)
    for i in range(0,n):
        for j in range(0,n):
            if i==j or i+j==n-1:
                A[i][j]='X'
            else:
                A[i][j]=0
    return A
#glavni program:
A = funkcija(3)
print("Matrica:")
for red in A:
    print(red)

```
</details>

## Тrеći zadatak
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

# Grupa 7
## Prvi zadatak
Napisati funkciju koja računa površinu geometrijskih oblika (krug, kvadrat, jednakostračni trougao). Argumenti funkcije su oblik i stranica, odnosno poluprečnik.
	
 	primer:
	dimenzija = 5, oblik = “krug” => P = 5 * 5 * 3.14 
	dimenzija = 5, oblik = “kvadrat” => P = 5 * 5
	dimenzija = 5, oblik = “jednakostranicni trougao” => P = 5 * 5 / 2

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def povrsina_oblika(oblik, stranica):
    povrsina = "Nije unet odgovarajuć oblik: krug, kvadrat ili trougao!"
    if oblik == "krug":
        povrsina = stranica **2 * 3.14
    elif oblik == "kvadrat":
        povrsina = stranica ** 2
    elif oblik == "trougao":
        povrsina = (stranica**2) * 3 **(1/2)/4
    return povrsina

#glavni program:
print(povrsina_oblika("krug", 5))
print(povrsina_oblika("kvadrat", 5))
print(povrsina_oblika("trougao", 5))
print(povrsina_oblika("pravougaonik", 5))
```
</details>

## Drugi zadatak
Napisati funkciju koja pronalazi najmanje članove po redovima kvadratne matrice A (nxn) i ispisuje ih u obliku niza B.
	
 	primer:
		[1, 0, 3]
	A = [1, 2, 3]  => B = [0, 1, 1]
    	[1, 2, 5]

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(A):
    B=[]
    for i in range(0,len(A)):
        minbr=A[i][0]
        for j in range(0,len(A)):
            if A[i][j]<minbr:
                minbr=A[i][j]
        B.append(minbr)
    return(B)

#glavni program:
print(funkcija([[1, 0, 3], [1, 2, 3], [1, 2, 5]]))
```
</details>

## Treći zadatak
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

# Grupa 8
## Prvi zadatak
Napisati funkciju koja uzima skup koeficijenata (Niz A, dimenzije n) i vrednost promenljive x i računa polinom: 

p(x) = a₀ + 3a₁x² + 5a₂x⁴ + 7a₃x⁶ + …

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(A, x):
    polinom = A[0]  # Prvi koeficijent a₀
    for i in range(1, len(A)):
        polinom += (2*i + 1) * A[i] * x**(2*i)
    return polinom

# glavni program:
A = [1, 2, 3] 
x = 2  
print(funkcija(A, x))
```
</details>

## Drugi zadatak
Napisati funkciju koja pronalazi najveće članove po redovima kvadratne matrice A (nxn) i ispisuje ih u obliku niza B.
	
 	primer:
		[1, 0, 3]
	A = [1, 2, 3]  => B = [3, 3, 5]
    	[1, 2, 5]

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(A):
    B=[]
    for i in range(0,len(A)):
        maxbr=A[i][0]
        for j in range(0,len(A)):
            if A[i][j]>maxbr:
                maxbr=A[i][j]
        B.append(maxbr)
    return(B)

#glavni program:
print(funkcija([[1, 0, 3], [1, 2, 3], [1, 2, 5]]))
```
</details>

## Treći zadatak
Napisati program koji otvara fajl [dostavnica.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/tree/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/April) sa spiskom dostava jedne firme u toku jednog dana u formatu:

    tip vozila, registracija,predjeni kilometri,broj dostava

U izlazni fajl štampati spisak vozila sortiranih po profitu ostvarenom tog dana. Predjeni kilometar košta 34 dinara
a svaka dostava vredi 250.

<details markdown='block'>
<summary>Rešenje</summary>
  
```python
def dostava(ulaz):
    vozila  = []
    cena_po_km = 34
    cena_dostave = 250
    with open(ulaz) as fajl:
        for linija in fajl:
            tip_vozila, registracija, predjeni_km, br_dostava = linija.rstrip().split(',')
            profit = int(br_dostava)*cena_dostave - int(predjeni_km)*cena_po_km
            vozila.append((tip_vozila, registracija, profit))

#sortiranje preko petlje (jedno od sortiranja je dovoljno)
        for i in range(len(vozila)-1):
            for j in range(i+1, len(vozila)):
                if vozila[i][2] < vozila[j][2]:
                    vozila[i], vozila[j] = vozila[j], vozila[i]
# sortiranje preko sorted funkcije (jedno od sortiranja je dovoljno)
        vozila = sorted(vozila, key=lambda vozilo: vozilo[2], reverse=True)
# sortiranje preko sort metode (jedno od sortiranja je dovoljno)
        vozila.sort(key=lambda  vozilo: vozilo[2], reverse=True)
# ispisivanje u fajl
    with open('rezultat.txt', 'w') as fajl:
    for vozilo in vozila:
        fajl.write(f'{vozilo[0]} {vozilo[1]} {vozilo[2]}\n')
# glavni program
dostava('dostavnica.txt')
```
</details>
