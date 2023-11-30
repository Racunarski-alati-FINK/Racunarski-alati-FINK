# Python II kolokvijum 2022.

## Grupa 1a
## Prvi zadatak
Napisati funkciju koja ce izracunavati razliku izmedju zbira negativnih clanova ispod glavne dijagonale i proizvoda clanova iznad glavne dijagonale kvadratne celobrojne matrice dimenzija n x n.

<details markdown='block'>
<summary>Rešenje </summary>

```python
def funkcija(matrica):
	suma_ispod = 0
	proizvod_iznad = 1
	for i in range(len(matrica)):
    	for j in range(len(matrica)):
        	if i > j:
            	if matrica[i][j] < 0:
                	suma_ispod += matrica[i][j]
             elif i < j:
                     proizvod_iznad *= matrica[i][j]
	return suma_ispod - proizvod_iznad

# poziv glavnog programa
print(funkcija([[2, -4, 3], [3, -2, 1], [-8, 5, 2]]))
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl  [rezultati_1a.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/rezultati_1a.txt) u kome svaka linija sadrži ime studenta, poene na prvom i drugom kolokvijumu u formatu:

        ime,poeni1,poen2
	
Program čita fajl i kreira fajlove položili.txt i nisu_polozili.txt u kojima se u abecednom redu ispisuju imena studenata. Student je položio ako je suma poena > 51. 
Format:  

        ime studenta  

<details markdown='block'>
<summary>Rešenje korišćenjem uređenenih parova </summary>
	
```python
polozili = []
nisu_polozili = []
with open('ulaz1a.txt') as fajl:
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

# Grupa 1b
## Prvi zadatak
Napisati funkciju koja uzima celobrojnu matricu proizvoljnih dimenzija (n x m). Funkcija računa razliku između proizvoda članova matrice koji su deljivi sa 3 i sume članova matrice čiji su indeksi parni brojevi.

<details markdown='block'>
<summary>Rešenje</summary>
	
``` python
def funkcija(matrica):
	proizvod = 1
	suma = 0

	for i in range(len(matrica)):
		for j in range(len(matrica[i])):
			if (matrica[i][j] % 3 == 0):
				proizvod *= matrica[i][j]
			if (i % 2 == 0) and (j % 2 == 0):
				suma += matrica[i][j]
	return proizvod - suma

# pozivanje glavnog programa
print(funkcija([[4, 6, 1], [5, 2, 9], [-3, 3, 1]]))
print(funkcija([[5, 8, 9], [0, 6, 12], [-3, 5, 1], [8, 1, 2]]))
```
</details>

## Drugi zadatak
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

# Grupa 2a
## Prvi zadatak
Funkcija uzima niz i vraca glavnom programu niz novi_niz.  
- ako je broj clanova niza paran novi_niz sadrzi vrednosti:
    [niz[0]+niz[-1], niz[1]+niz[-2], ..]  
- ako je broj clanova neparan novi_niz sadrzi samo niz[n/2+1]  

	Primer: [3, 5, 77, 1, 2, 8, 3] => novi_niz = [1]    
	Primer: [2, 2, 2, 3, 4, 5] => novi_niz = [7, 6, 5]

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(niz):
	novi_niz = []
    print(len(niz)//2)
    if len(niz) % 2 == 0:
		for i in range(len(niz)//2):
			novi_niz.append(niz[i] + niz[-(i+1)])
	else:
    	novi_niz.append(niz[len(niz)//2])
	return novi_niz

glavni program
print(funkcija([3, 5, 77, 1, 2, 8, 3]))
print(funkcija([2, 2, 2, 3, 4, 5]))
```
</details>

## Drugi zadatak 
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

# Grupa 2b
## Prvi zadatak
Funkcija uzima celobrojni niz i ceo broj X. Sortira niz u opadajućem poretku. Zatim unuli sve parne brojeve koji su veći od X, a neparnim manjim od X  dodeli vrednost 1. 

	Primer: niz = [2, 6, -7, 0, 1, 5], x = 4  => [0, 5, 2, 1, 0, 1]  
	Primer: niz = [5, 1, 8, -2, 7, -3, 10], x = 6 => [0, 0, 7, 1, 1, -2, 1]  

<details markdown='block'>
<summary>Rešenje</summary>

```python
def funkcija(niz, x):
    for i in range(0, len(niz)-1):
        for j in range(i+1, len(niz)):
            if niz[i] < niz[j]:
                niz[i], niz[j] = niz[j], niz[i]

    for i in range(len(niz)):
        if niz[i] % 2 == 0 and niz[i] > x:
            niz[i] = 0
        elif niz[i] % 2 != 0 and niz[i] < x:
            niz[i] = 1
 
    return niz


print(funkcija([2, 6, -7, 0, 1, 5], 4))
print(funkcija([5, 1, 8, -2, 7, -3, 10], 6))
```
</details>

# Drugi zadatak
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

# Grupa 3a
## Prvi Zadatak
Funkcija uzima kvadratnu matricu (n x n).
Glavnom programu vraca sumu ivicnih clanova.
Ivicni clanovi su clanovi prvog reda, prve kolone,
poslednjeg reda i poslednje kolone.
Izbeći sumiranje dvostrukih članova (članova u uglovima matrice).

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
        if i == 0 or i == len(matrica)-1:
            for j in range(len(matrica)):
                suma += matrica[i][j]
        else:
            suma += matrica[i][0] + matrica[i][-1]

    return suma

#pozivanje glavnog programa
print(funkcija([[3, 6, 1], [7, 3, 9], [-1, 5, 11]]))
print(funkcija([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]))
```
</details>

# Drugi zadatak
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

# Grupa 3b
## Prvi zadatak
Funkcija uzima celobrojni niz i ceo broj X.  
Sortira niz u opadajućem poretku.  
Zatim unuli sve parne brojeve koji su veći od X,
a neparnim manjim od X  dodeli vrednost 1.

	Primer: niz = [2, 6, -7, 0, 1, 5], x = 4  => [0, 5, 2, 1, 0, 1]  
	Primer: niz = [5, 1, 8, -2, 7, -3, 10], x = 6 => [0, 0, 7, 1, 1, -2, 1]  

<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(niz, x):
    print(niz)
    for i in range(0, len(niz)-1):
        for j in range(i+1, len(niz)):
            if niz[i] < niz[j]:
                niz[i], niz[j] = niz[j], niz[i]
    for i in range(len(niz)):
        if niz[i] % 2 == 0 and niz[i] > x:
            niz[i] = 0
        elif niz[i] % 2 != 0 and niz[i] < x:
	return niz

#pozivanje glavnog progam
print(funkcija([2, 6, -7, 0, 1, 5], 4))
print(funkcija([5, 1, 8, -2, 7, -3, 10], 6))

```
</details>

## Drugi zadatak
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

# Grupa 4a
## Prvi zadatak
Funkcija izračunava razliku između srednjih vrednosti elemenata niza A (n) i niza B (m).
<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(A, B):
	srednja_vred_A = 0
    srednja_vred_B = 0
    
    suma_A = 0
    suma_B = 0

    brojac_A = 0
    brojac_B = 0

    for i in range(len(A)):
        brojac_A += 1
        suma_A += A[i]

    for i in range(len(B)):
        brojac_B += 1
        suma_B += B[i]

    srednja_vred_A = suma_A / brojac_A
    srednja_vred_B = suma_B / brojac_B

    return srednja_vred_A-srednja_vred_B
    
#glavni program
print(funkcija([2, -4, 3, 5, 9, 1], [3, -2, 0, 1]))
```
</details>

# Drugi zadatak
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

# Grupa 4b
## Prvi zadatak
Funkcija uzima celobrojni niz i ceo broj x.
Funkcija racuna i glavnom programu vraća srednju vrednost članova niza koji su veći od broja x i sortira niz u rastući poredak.
_Napomena: ne koristiti metode i funkcije za sortiranje._
<details markdown='block'>
<summary>Rešenje</summary>
	
```python
def funkcija(niz, x):
	srednja_vrednost = 0
    suma = 0
    brojac = 0

    for i in range(len(niz)):
        if niz[i] > x:
            suma += niz[i]
            brojac += 1

    srednja_vrednost = suma/brojac

    
    for i in range(0, len(niz)-1):
        for j in range(i+1, len(niz)):
            if niz[i] > niz[j]:
                niz[i], niz[j] = niz[j], niz[i]

#ovde je moguce koristiti i klasicnu zamenu mesta clanovima
                privremena = niz[i]
                niz[i] = niz[j]
                niz[j] = privremena

    return srednja_vrednost, niz


#glavni program
print(funkcija([5, 4, 9, -11, 13, 19, 2, 6, -7], 4))
```
</details>

## Drugi zadatak
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
Napisati program koji otvara fajl [koeficijenti_5a.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/koeficijenti_5a.txt).  
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
with open('koeficijenti_5a.txt', 'r') as fajl:
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
Napisati program koji otvara fajl [rezultati_6a.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/rezultati_6a.txt)  
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
with open('rezultati_6a.txt', 'r') as fajl:
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
Napisati program koji otvara fajl [temperature_6b.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Kolokvijumi/Ulazni%20txt%20fajlovi/2022/temperature_6b.txt).  
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
