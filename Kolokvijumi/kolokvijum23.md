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
Napisati program koji otvara fajl  [rezultati_1a.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/rezultati_1a.txt) u kome svaka linija sadrži ime studenta, poene na prvom i drugom kolokvijumu u formatu:

        ime,poeni1,poeni2
	
Program čita fajl i kreira fajlove položili.txt i nisu_polozili.txt u kojima se u abecednom redu ispisuju imena studenata. Student je položio ako je suma poena > 51. 
Format:  

        ime studenta  

<details markdown='block'>
<summary>Rešenje korišćenjem uređenenih parova </summary>
	
```python
polozili = []
nisu_polozili = []
with open('rezultati_1a.txt') as fajl:
	for linija in fajl:
	    ime, poeni1, poeni2 = linija.rstrip().split(',')
         poeni = int(poeni1) + int(poeni2)
         if poeni > 51:
             polozili.append((ime, poeni))
         else:
             nisu_polozili.append((ime, poeni))


with open('polozili.txt', 'w') as fajl:
 	for student in sorted(polozili):
        fajl.write(f"{student[0]}\n")

with open('nisu_polozili.txt', 'w') as fajl:
	for student in sorted(nisu_polozili):
    	fajl.write(f"{student[0]}\n")
```
</details>

<details markdown='block'>
<summary>Rešenje korišćenjem rečnika </summary>
	
``` python
polozili = []
nisu_polozili = []
with open('rezultati_1a.txt') as fajl:
	for linija in fajl:
    	ime, poeni1, poeni2 = linija.rstrip().split(',')
        poeni = int(poeni1) + int(poeni2)
        student = {'ime':ime, 'poeni':poeni}
        if poeni > 51:
            polozili.append(student)
        else:
            nisu_polozili.append(student)

with open('polozili_recnici.txt', 'w') as fajl:
	for student in sorted(polozili, key=lambda student: student['ime'], reverse=False):
		fajl.write(f"{student['ime']}\n")

with open('nisu_polozili_recnici.txt', 'w') as fajl:
	for student in sorted(nisu_polozili, key=lambda student: student['ime'], reverse=False):
		fajl.write(f"{student['ime']}\n")
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
Napisati program koji otvara fajl [reci_1b.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/reci_1b.txt) u kome svaka linija predstavlja jednu reč.
Svaku reč smestiti u listu reci. Program takođe dobija skup reči, i treba da u izlazni
fajl rezultat.txt zapiše sve reči koje se nalaze u obe liste i broj takvih reči. 

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
skup = ['robot', 'macka', 'masinstvo', 'kolokvijum']
reci = []
with open('reci_1b.txt', 'r') as fajl:
    for linija in fajl:
        reci.append(linija.rstrip())

zajednicke_reci = []
for rec in reci:
    if rec in skup:
        zajednicke_reci.append(rec)

with open('reci.txt', 'w') as fajl:
    for rec in zajednicke_reci:
        fajl.write(f"{rec}\n")
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
Napisati program koji otvara fajl [prodavnica_2a.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/prodavnica_2a.txt)
u kome svaka linija sadrži podatke o artiklima u
prodavnici u formatu:  
  
artikal, nabavna cena, prodajna cena, broj prodatih komada  
  
zarada = (prodajna cena - nabavna cena) * broj prodatih komada  

i kreira novi fajl izveštaj.txt u kome se štampaju nazivi artikala i ostvarena zarada po artiklu
u jednom danu, u formatu:  

	artikal, zarada  
 
A kao poslednju liniju fajla vraća ukupnu zaradu za taj dan.  

<details markdown='block'>
<summary>Rešenje korišćenjem uređenih parova</summary>
	
```python
artikli = []
with open('prodavnica_2a.txt', 'r') as fajl:
    for linija in fajl:
        naziv, nabavna_cena, prodajna_cena, broj_prodatih = linija.rstrip().split(',')
        zarada = (int(prodajna_cena) - int(nabavna_cena)) * int(broj_prodatih)
        artikli.append((naziv, zarada))

with open('artikli.txt', 'w') as fajl:
    for i in range(len(artikli)):
        fajl.write(f"{artikli[i][0]} {artikli[i][1]}\n")
```
</details>

<details markdown='block'>
<summary>Rešenje korišćenjem rečmika</summary>
	
```python
artikli = []
with open('prodavnica_2a.txt', 'r') as fajl:
    for linija in fajl:
        naziv, nabavna_cena, prodajna_cena, broj_prodatih = linija.rstrip().split(',')
        zarada = (int(prodajna_cena) - int(nabavna_cena)) * int(broj_prodatih)
        artikal = {'naziv':naziv, 'zarada':zarada}
        artikli.append(artikal)

with open('artikli.txt', 'w') as fajl:
    for artikal in artikli:
        fajl.write(f"{artikal['naziv']} {artikal['zarada']}\n")
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
# Drugi zadatak
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

# Treći zadatak
Napisati program koji otvara fajl [tacke_2b.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/tacke_2b.txt).    
Svaka linija fajla predstavlja koordinate u formatu:    
xkoord,ykoord  
Napraviti listu tacke i u nju smestiti recnike,  
koji sadrze podatke iz ucitanog fajla, pri cemu recnik treba da bude u formatu:  
tacka = {'x':xkoord, 'y':ykoord}  
Sortirati tacke ykoord u rastucem poretku,
i tako sortirane tacke stampati u izlazni fajl rezultat.txt.
Poslednji red izlaznog fajla rezultat.txt) treba da sadrzi srednju vrednost svih xkoord.

Primer:

	tacke.txt  
	0,1  
	2,10  
	10,-3  
 
	rezultat.txt  
	10,-3  
	0,1  
	2,10  
	Srednja vrednost svih x koordinata je: 4  

<details markdown='block'>
<summary>Rešenje</summary>

```python
tacke = []
with open('tacke_2b.txt', 'r') as fajl:
    for linija in fajl:
        xkoord, ykoord = linija.rstrip().split(',')
        tacka = {'x':float(xkoord), 'y':float(ykoord)}
        tacke.append(tacka)

x_ukupno = 0
y_ukupno = 0
with open('izlaz2b.txt', 'w') as fajl:
    for tacka in sorted(tacke, key=lambda tacka:tacka['y'], reverse=False):
        fajl.write(f"{tacka['x']} {tacka['y']}\n")
        x_ukupno += tacka['x']
    fajl.write(f"Srednja vrednost svih x koordinata je {x_ukupno/len(tacke)}")

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

# Treći zadatak
Napisati program koji otvara fajl [temperature_3a.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/temperature_3a.txt).  
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
with open('temperature_3a.txt', 'r') as fajl:
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
with open('temperature_3a.txt', 'r') as fajl:
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
Napisati program koji otvara fajl [tacke_3b.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/tacke_3b.txt).  
Svaka linija fajla predstavlja koordinate u formatu:  
xkoord,ykoord  
Napraviti listu tacke i u nju smestiti recnike,  
koji sadrze podatke iz ucitanog fajla, pri cemu recnik treba  
da bude u formatu:  
tacka = {'x':xkoord, 'y':ykoord}  
Sortirati tacke ykoord u rastucem poretku,  
i tako sortirane tacke stampati u izlazni fajl rezultat.txt.  
Poslednji red izlaznog fajla rezultat.txt) treba da sadrzi srednju vrednost svih xkoord.  

Primer:

	tacke.txt  
	0,1  
	2,10  
	10,-3  

	rezultat.txt  
	10,-3  
	0,1  
	2,10  
	Srednja vrednost svih x koordinata je: 4  

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
tacke = []
with open('tacke_3b.txt', 'r') as fajl:
	for linija in fajl:
		xkoord, ykoord = linija.rstrip().split(',')
        tacka = {'x':float(xkoord), 'y':float(ykoord)}
        tacke.append(tacka)
x_ukupno = 0
y_ukupno = 0
with open('izlaz2b.txt', 'w') as fajl:
    for tacka in sorted(tacke, key=lambda tacka:tacka['y'], reverse=False):
        fajl.write(f"{tacka['x']} {tacka['y']}\n")
        x_ukupno += tacka['x']
    fajl.write(f"Srednja vrednost svih x koordinata je {x_ukupno/len(tacke)}")
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

# Treći zadatak
Napisati program koji otvara fajl [rezultati_4a.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/rezultati_4a.txt).   
Svaka linija fajla sadrzi ime studenta i poene na ispitu u formatu:

 	ime studenta;poeni  
 Program treba da pročita podatke o studentima,  
 na osnovu broja poena dodeli argument položio (>=51)  
 ili nije položio (<51) studentu i štampa izlaznu datoteku  
 spisak.txt u formatu:   
  ime studenta - polozio ime studenta - nije polozio  

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
studenti = []
with open('rezultati_4a.txt') as fajl:
    for linija in fajl:
        ime, poeni = linija.rstrip().split(';')
        if int(poeni) >= 51:
            status = 'polozio'
        else:
            status = 'nije polozio'
        studenti.append((ime, status))

print(studenti)

with open('rezultati_torke.txt', 'w') as fajl:
    for i in range(len(studenti)):
        fajl.write(f"{studenti[i][0]} - {studenti[i][1]}\n")
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
Napisati program koji otvara program [kupovina_4b.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/kupovina_4b.txt).  
Svaka linija fajla sadrzi podatke od namirnici i kolicini za kupovinu:  

    namirnica,kolicina,cena po komadu

Program stampa fajl racun.txt u kome je ispisan svaki proizvod   
i potrosen novac po proizvodu (kolicina*cena)
u formatu:  

    namirnica,novac

Poslednja linija fajla je:  

    Ukupno,suma novca 
    
<details markdown='block'>
<summary>Rešenje korišćenjem uređenih parova</summary>
	
```python
proizvodi = []
with open('kupovina_4b.txt', 'r') as fajl:
    for linija in fajl:
        namirnica, kolicina, cena = linija.rstrip().split(',')
        novac = int(kolicina)*int(cena)
        proizvodi.append((namirnica, novac))

with open('kupovina_4b.txt', 'w') as fajl:
    for i in range(len(proizvodi)):
        fajl.write(f"{proizvodi[i][0]} {proizvodi[i][1]}\n")
```
</details>
<details markdown='block'>
<summary>Rešenje korišćenjem rečnika</summary>
	
```python
proizvodi = []
with open('ulaz4b.txt', 'r') as fajl:
    for linija in fajl:
        namirnica, kolicina, cena = linija.rstrip().split(',')
        proizvod = {'namirnica':namirnica, 'novac':int(kolicina)*int(cena)}
        proizvodi.append(proizvod)

with open('kupovina_recnici.txt', 'w') as fajl:
    for proizvod in proizvodi:
        fajl.write(f"{proizvod['namirnica']} {proizvod['novac']
```
</details>
</details>
