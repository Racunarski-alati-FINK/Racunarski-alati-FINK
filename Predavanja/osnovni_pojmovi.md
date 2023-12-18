# Osnovni pojmovi

## Osnovni pojmovi u računarstvu

Osnovni pojmovi u računarstvu su:

* **podatak** - formalizovana reprezentacija činjenice ili ideje pogodne za komunikaciju, interpretaciju ili obradu
* **informacija** - saznanje koje je prihvatljivo za žive organizme ili mašine. Podaci predstavljaju osnovu svake informacije
* **sistem** - složen objekat koji sačinjava više elemenata čiji sklop predstavlja jednu funkcionalnu celinu
* **informacioni sistem** - sistem u kome su osnovni elementi čuvanje, prenos i obrada informacija
* **informatika** - nauka čiji je predmet istraživanja informacioni sistem u okviru proizvoljnog sistema
* **program** - niz komandi (instrukcija) kojima se upravlja računarom pri rešavanju određenog zadatka informatike

## Programiranje i primena računara

Programiranje podrazumeva tri nivoa u rešavanju problema:

* algoritamski
* programski
* mašinski

Primena računara može biti:

* naučno-tehnička
* poslovna
* upravljanje velikim sistemima
* komunikacija, zabava

## Faze izrade programa

Faze u izradi računarskog programa su:

* postavka problema
* projektovanje programa
* razvoj programa
* ispitivanje performansi programa
* uobličavanje konačne verzije programa

Primer

Za krug poznatog poluprečnika R izračunati obim (O) i površinu kruga (P).\
Poznato: r, $\pi$
Izračunati: O, P

Algoritam:

1. Ulazne veličine: r, $\pi$  
2. Izračunati: O = 2r $\pi$  
3. Izračunati: P = $r^2$ $\pi$  
4. Izlazne veličine: O, P 

Izvršavanje programa:

1. Ulazne veličine: R = 3, Pi = 3.14159
2. Izračunati: O = 2\*3\*3\*3.14159
3. Izračunati: P = r\*r\*Pi
4. Izlazne veličine: O, P

## Kompajlirani i interpretirani jezici

![Dijagram interpretirani i kompajliranih jezika](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/8ce86a37-3d44-4de1-b078-825592315b5d)

## Interpretirani (skript) jezici

![Dijagram interpretiranog jezika](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/45e9b195-5f29-4cbe-adf1-61a5963f668f)

## Prvi program u Python

### Hello world program

```python
print('Hello world')
```

Prvi program u Pythonu:

* sastoji se od jedne naredbe (linije)
* štampa tekst na ekran/konzolu
* nakon pokretanja na ekranu se ispisuje Hello world

### print() funkcija

* ugrađena python funkcija za ispisivanje u konzolu
* ispisuje tekst dat pod navodnicima ili brojeve

```python
print('Zdravo svima!')
print(101)
print(5.74)
```

### input() funkcija

* ugrađena python funkcija za čitanje unosa korisnika
* unete vrednosti učitavaju se kao tekst

```python
print('Zdravo! Kako se zoves?')
ime = input()
print('Zdravo, znaci ti si' + ime)
```

### Promenljive

* u prethodnom primeru u promenljivu ime smeštamo tekst koji kasnije prikazujemo
* koriste se kako bismo zapamtili različite vrednosti - tekst ili brojeve
* dodelu vrednosti promenljivoj vršimo preko opretora dodele (=)
* ukoliko se naziv promenljive sastoji od više reči poželjno je razdvojiti ih (_): ime_studenta, broj_indeksa, naziv_smera

```python
ime_studenta = "Marko Markovic"
broj_indeksa = 99
naziv_studija = "Urbano inzenjerstvo"
prosek = 8.75
```

### Komentari

* komentari su delovi programa koji se ne izvršavaju
* ostavljanje komentara je dobra praksa, pomaže u razumevanju koda
* komentari u python su označeni znakom (#) ili (""" """)

```python
"""
Ovo je prvi program u Python.
U python je moguce ostaviti komentare.
Komentari se mogu pisati i u vise redova.
"""
# prvi komentar
print("Zdravo svete!")  # linijski komentar
# drugi komentar
```

## Tipovi podataka

### O tipovima podataka

* python spada u dinamički tipizirane jezike - promenljive dobijaju tip od vrednosti koju sadrže
* promenljive mogu da prihvate bilo koju vrednost
* promenljive promenom vrednosti mogu da promene i tip
* u python postoji više osnovnih i složenih tipova podataka
* ugrađena funkcija type() vraća tip (klasu) kojoj pripada promenljiva

### Primer promene tipa preko vrednosti

```python
print(type(c))

c = 15.4
print(type(c))

c = "Promenljiva je sada str."
print(type(c))
```

Rezultat:

```bash
<class 'int'>
<class 'float'>
<class 'str'>
```

### Osnovni tipovi podataka u python

| Tip   | Opis                    | Primer      |
|-------|-------------------------|-------------|
| int   | celi brojevi            | 5           |
| float | decimalni brojevi       | 7.86        |
| str   | tekst (niska karaktera) | "Zdravo"    |
| bool  | logička promenljiva     | True, False |

## Brojevi

### Celi brojevi

* bez obzira da li se radi o veoma velikim ili malim brojevima oni su u python predstavljeni kao int:
  
  ```python
  x = 1
  x = 10000000000000000000000000000000000000000001
  ```

* ovo značajno olakšava rad sa brojevima u python jer za razliku od nekih drugih programa nema posebnih tipova intergera za veoma velike brojeve
* uključuju pozitivne i negativne brojeve

### Realni brojevi

* brojevi koji imaju bar jednu ili više decimala
* pozitivni i negativni brojevi:

    ```python
    x = 3.14
    x = 56.9
    x = 101.24
    ```

### Aritmetičke operacije

| Znak  | Naziv                   | Primer      |
|-------|-------------------------|-------------|
| +     | sabiranje            | 3+2           |
| -     | oduzimanje       | 6-1        |
| *     | množenje | 3*5    |
| /     | deljenje     | 3/2 |
| //     | celobrojno deljenje     | 7//2 |
| **     | stepenovanje     | 4**2 |
| %     | ostatak celobrojnog deljenja     | 5%2 |

### Operacije sa celim brojevima

| Program  | Rezultat |
|-------|--------------|
| 2+3     | 5 |
| 8-2     | 6         |
| 6*3   | 18  |
| 8/4     | 2.0 |
| 11//3     | 3 |
| 2**3     | 8 |
| 9%4     | 1 |

### Operacije sa realnim brojevima

| Program  | Rezultat |
|-------|--------------|
| 2.3+1.5     | 3.8 |
|2.3-15     | 0.79999998         |
| 1.7*3.1   | 5.27  |
| 8/4     | 2.0 |
| 3.0**2.0     | 9.0 |
| 4.2**1.6     | 2.625 |

### Složeni operatori dodele

* ranije je pokazano da se operator dodele '=' može koristiti za dodelu vrednosti promenljivoj
* složeni operatori omogućavaju kombinovanje numeričkih operacije i dodele vrednosti

```python
x += 1   # isto kao i x = x + 1
x -= 4   # isto kao i x = x - 4
x *-= 2  # isto kao i x = x * 2
```

| Znak  | Naziv                   | Primer      | Ekvivalnet|
|-------|-------------------------|-------------|-------------|
| +=     | Dodaje vrednost promenljivoj | x += 2  | x = x + 2 |
| -=     | Oduzima vrednost promenljivoj | x -= 3  | x = x - 3 |
| *=     | Množi promenljivu | x *= 2    | x = x*2 |
| /=     | Deli promenljivu | x /= 2    | x = x/2 |
| //=     | Celobrojno deljenje promenljive | x //= 3    | x = x//3 |
| **=     | Stepenuje promenljivu     | x ** = 3 | x = x**3 |
| %=     | Ostatak celobrojnog deljenja     | x %= 2 | x = x % 2 |

## Niske

### O niskama

* niske predstavljaju skevence ili niz karaktera (slova)
* definisane su navođenjem između jednostrukih ili dvostrukih navodnika
* svakom karakteru je moguće pristupiti preko njegovog indeksa
* indeksi u  python počinju od 0
* razmak predstavlja karakter

### Definisanje niske

* navođenjem teksta između jednostrukih ili dvostrukih navodnika:

    ```python
    rec1 = "Masinsko inzenjerstvo"
    rec2 = 'Racunarski alati'
    ```

* kombinovanje navodnika je moguće:
  
  ```python
  rec3 = "Koriscenje 'navodnika' je dozvoljeno"
  rec4 = 'Jednostruki spolja a "dvostruki" unutra'
  ```

* ukoliko se ne može izbeći korišćenje istih navodnika unutar niske, neophodno je ispred dodati specijalni karakter:
  
  ```python
  rec5 = 'Upotreba \'navodnika\' unutar niske'
  rec6 = "Dvostruki navodnici unutar \"navodnika\""
  ```

### Pristupanje karakterima niska

* pristupanje karakteru niske preko indeksa
  
  ```python
  niska[indeks karaktera]
  ```

```python
moja_rec = "Fakultet inzenjerskih nauka"
prvo_slovo = moja_rec[0]
poslednje_slovo = moja_rec[-1]
deseto_slovo = moja_rec[9]
```

```bash
print(prvo_slovo)      # F
print(poslednje_slovo) # a
print(deseto_slovo)    # i
```

### Izdvajanje dela niske

* izdvajanje dela niske preko indeksa
  
  ```python
  niska[pocetni indeks:poslednji indeks]
  ```

```python
rec = "BM1300 Racunarski alati"

print(rec)
print(rec[0:6]), print(rec[:6])
print(rec[7:17])
print(rec[8:23]), print(rec[18:]), print(rec[-6:])
```

### Povezivanje niski

```python
prva_rec = "Dobar"
druga_rec = "dan"
treca_rec = prva_rec + druga_rec

prva_rec = "Dobar"
druga_rec = "dan"
razmak = " "

nova_rec = prva_rec + razmak + druga_rec

nova_rec = "Dobar " + "dan"
```

### funkcija len()

* ugrađena funkcija u python koja vraća broj karaktera (dužinu) niske
* funkcija broji i prazna mesta (razmake)

    ```python
    rec = "Racunarski alati"

    print(len(rec))
    ```

* rezultat izvršavanja ovog programa je 16 (15 karaktera i razmak)

### Formatiranje niske

```python
formatirana_niska = "Racunarski alati {}"
print(formatirana_niska.format("BM1300"))

ime_studenta = "Marko"
broj_indeska = "99"
naziv_studija = "Urbano inzenjerstvo"
print("{} ima broj indeksa {} i upisao/la je {}".format(ime_studenta, broj_indeska, naziv_studija))

print("Smer {2} upisao/la je {0} sa brojem indeksa {1} i ".format(ime_studenta, broj_indeska, naziv_studija))
```

### f-string formatiranje

```python
ime_studenta = "Marko Petrovic"
naziv_predmeta = "Racunarski alati"
ocena = 10
print(f"{ime_studenta} je polozio ispit {naziv_predmeta} sa ocenom {ocena}.")

pi = 3.14159
 
print(f"Broj pi najcesce zaokruzujemo na 2 decimale {pi:.2f}")
```

### Promena ulazne niske u broj

* podrazumevano funkcija input() vraća promenljivu tipa str
* promenu tipa moguće je izvršiti dodavanjem float ili int ispred input funkcije
* promena teksta u celobrojnu:
  
  ```python
  godine = int(input('Koliko imas godina?'))
  ```

* promena teksta u decimalnu:
  
  ```python
  r = float(input('Unesi poluprecnik: '))
  ```

## Primeri

```python
prvi_broj = input("Unesi prvi broj: ")     # unos korisnika
drugi_broj = input("Unesi drugi broj: ")   # unos korisnika
z-bir = prvi_broj + drugi_broj             # zbir 
print(zbir)                                # stampanje rezultata
```

```bash
Unesi prvi broj: 2
Unesi drugi broj: 5.8

25.8  ?
```

Rezultat izvršavanja ovog programa je neočekivan jer python unete vrednosti tretira kao tekstualne:

```python
'2' + '5.8' = '25.8'
```

```python
prvi_broj = float(input("Unesi prvi broj: "))     # unos korisnika
drugi_broj = float(input("Unesi drugi broj: "))    # unos korisnika
z-bir = prvi_broj + drugi_broj             # zbir 
print(zbir)                                # stampanje rezultata
```

```bash
Unesi prvi broj: 2
Unesi drugi broj: 5.8

7.8
```

Sada se unos konvertuje u realne brojeve i dobijamo rezultat:

```python
2 + 5.8 = 7.8
```

```python
r = float(input("Unesi poluprecnik: ")) # unos korisnika
pi = 3.1415926                          # konstanta
obim = 2*r*pi                           # izracunavanje
povrsina = r*r*pi                       # izracunavanje
print(f"Za krug poluprecnika {r} obim iznosi {obim:.3f} a povrsina {povrsina:.2f}.")

```
