# Rad sa fajlovima

## Otvaranje fajlova. Funkcija open()

Funkcija koja omogućava otvaranje postojećih fajlova je **open()**:

```python
fajl = open(naziv fajla, mod za rad sa fajlom)
```

* open() - funkcija omogućava otvaranje fajla
* prvi argument funkcije open() je naziv fajla koji se otvara
* mod (način) rada sa fajlom
  
    - w - zapisivanje (eng. write) zapisivanje u fajl
    - a - dodavanje (eng. append) dodavanje na kraj fajla
    - r - čitanje (eng. read), čitanje iz fajla
    - fajl - funkcija open() vraća fajl objekat

## Zapisivanje u fajlove. Funkcija write()

Pri zapisivanju u fajlove koristimo funkciju write. Funkcija write uzima jedan argument i omogućava zapisivanje na kraj fajla:

```python
fajl.write(argument)   # argument je najcesce jedna niska (string)
```

Sada možemo kombinovati unos korisnika i metodu write kako bismo unos zapisali na kraj fajla.

```python
ime = input('Kako se zoves?')
fajl = open('imena_studenata.txt', 'w')
fajl.write(ime)
```

Ukoliko program pokrenemo nekoliko puta i unesemo niske (imena) dobijamo sledeći rezultat:

```bash
Kako se zoves? Marko
Kako se zoves? Ana
Kako se zoves? Milica
```

Ukoliko otvorimo fajl imena_studenata.txt nakon ova tri unosa videćemo sledeći sadržaj:

```bash
Milica
```

Kako se vidi u fajl je snimljeno samo poslednje od unetih imena. Ovo se dešava zato što mod za zapisivanje 'w', koji smo koristili pri otvaranju fajla, otvara potpuno novi fajl svaki put i briše sav prethodni sadržaj. Kako je naš cilj da u fajl zapisujemo vrednosti bez brisanja prethodnih, moramo da koristimo mod zapisivanja na kraj fajla 'a'. Pri otvaranju fajla na ovaj način uneti sadržaj se zapisuje na kraj prethodnog sadržaja:

```python
ime = input('Kako se zoves?')
fajl = open('imena_studenata.txt', 'a')
fajl.write(ime)
```

Nakon što smo promenili način otvaranja pokrenimo program ponovo nekoliko puta:

```bash
Kako se zoves? Marko
Kako se zoves? Ana
Kako se zoves? Milica
```

Po otvaranju fajla možemo videti da su sada sva imena zapisana u fajl na sledeći način:

```bash
MarkoAnaMilica
```

## Formatiranje niski pri zapisivanju u fajlove

Kako smo videli u prethodnom primeru, koršćenje različitih modova pri otvaranju fajlova omogućuje nam različito zapisivanje u fajlova. Pri zapisivanju u fajlove moguće je niske prethodno formatirati i urediti na način koji je nama potreban. Radi formatiranog zapisa niski u fajlove neophodno je:

* pri zapisivanju možemo odrediti tačan položaj podataka, razmake i prelazak u novi red
* linije koje zapisujemo u fajlove su niske i zato koristimo metode za rad sa niskama i specijalne znake za formatiranje pri zapisivanju
* pri zapisivanju najčešće koristimo:
  - \n, \t
  - lstrip(), rstrip(), strip()
  - split()
  - join()

### Specijalni karakteri \n i \t

Dva najčešća specijalna karaktra za pozicioniranje niski u redu fajla jesu:

* \n - specijalni karakter koji prelama nisku prebacujući ostatak u novi red
  
  ```python
  ime = 'Marko\nAna\nMilica'
  print(ime)
  ```
  
  daje:

  ```bash
  Marko
  Ana
  Milica
  ```

* specijalni karakter za višestruki razmak (tab)

    ```python
    imena = 'Marko\tAna\tMilica'
    ```

    daje:

    ```bash
    Marko   Ana   Milica  
    ```

### Metode strip(), lstrip(), rstrip()

Ova grupa metoda za rad sa niskama omogućava nam da uklonimo specijalne znake i razmake i niski:

* strip() - metoda iz niske uklanja specijalne znake i razmake:
    
    ```python
    ime = '   Ana   '
    print(ime)
    ```

    ```bash
        Ana   
    ```

    uz korišćenje metode:

    ```python
    print(ime.strip())
    ```

    ```bash
    Ana
    ```

* lstrip() - metoda iz niske uklanja specijalne znake i razmake:
    
    ```python
    ime = '   Ana   '
    print(ime)
    ```

    ```bash
       Ana   
    ```

    uz korišćenje metode:

    ```python
    print(ime.lstrip())
    ```

    ```bash
    Ana
    ```

* rstrip() - metoda iz niske uklanja specijalne znake i razmake:
    
    ```python
    ime = '   Ana   '
    print(ime)
    ```

    ```bash
       Ana   
    ```

    uz korišćenje metode:

    ```python
    print(ime.rstrip())
    ```

    ```bash
        Ana
    ```

### Metoda split()

Metodu split() možemo koristiti ukoliko želimo da podelimo nisku na mestu prosleđenog znaka. Kao rezultat poziva ove metode dobijamo listu koja sadrži sve niske dobijene deljenjem originalne niske:

```python
niska.split(znak)
```

znak je najčešće iz grupe:

```bash
zarez(,), tačka zarez(;), kosa crta(\)
```

Primer:

```python
student = 'Marko Petrovic,Masinsko inzenjerstvo,50'
ime, smer, bodovi = student.split(',')
print(f'Student {ime} na smeru {smer} je ostvario {bodovi} ESPB bodova.')
```

```bash
Student Marko Petrovic na smeru Masinsko inzenjerstvo je ostvario 50 ESPB bodova.
```

### Formatirano zapisivanje podataka na kraj fajla

```python
ime = input('Kako se ti zoves?')

fajl = open('imena_studenata.txt', 'a')   # otvaranje fajla
fajl.write(f'{ime}\n')  # zapisivanje u fajl
fajl.close()   # zatvaranje fajla na kraju rada
```

Ponavljanjem istog unosa uz dodavanje specijalnog znaka za prelazak u novi red (\n) dobijamo svako od imena ispisano u novom redu fajla:

```bash
Marko
Ana
Milica
```

### Zapisivanje u fajlove korišćenjem ključne reči with

```python
ime = input('Kako se zoves?')

with open('imena_studenata.txt', 'a') as fajl:
    fajl.write(f'{ime}\n')
```

## Čitanje fajlova

### Čitanje fajlova korišćenjem ključne reči with i metode readlines()

Za čitanje fajlova postoji nekoliko ugradjenih metoda u pythonu. Najefikasniji način jeste korišćenje metode readlines() koja čitav sadržaj fajla smešta u promenljivu kao nisku. Pogledajmo primer čitanja datoteke imena_studenata.txt. Za razliku od prethodnih primera fajl otvaramo u modu za čitanje 'r':

```python
with open('imena_studenata.txt', 'r') as fajl:
    linije = fajl.readlines()
print(linije)
```

Vidimo da je na objektu fajla pozvana metoda readlines. Nakon izvršavanja ove linije u promenljivu linije smeštena je lista niski koje predstavljaju svaku od linija fajla:

```bash
['Marko\n', 'Ana\n', 'Milica\n']
```

Kako bismo utvrdili kog su tipa članovi ovog niza možemo pozvati metodu type za svaki član:

```python
for linija in linije:
    print(type(linija))    # svaka linija je niska
```

Nakon što smo potvrdili da se radi o niskama možemo kreirati formatiranu nisku kao poruku:

```python
for linija in linije:
    print(f'Zdravo, {linija}!')
```

Kako na kraju svake niske postoji specijalni znak za prelazak u novi red rezultat koji dobijamo je:

```bash
Zdravo, Marko
!
Zdravo, Milica
!
Zdravo, Ana
!
Zdravo, Jovana
!
```

Nakon svake promenljive niska je prelomljena u ostatak (!) prebačen u novi red. Koristeći metodu rstrip() možemo da uklonimo specijalne karaktere na kraju reči dobijemo željeni format štampe:

```python
for linija in linije:
    print(f'Zdravo, {linija.rstrip()}!')
```

čime konačno dobijamo:

```bash
Zdravo, Marko!
Zdravo, Milica!
Zdravo, Ana!
Zdravo, Jovana!
```

Pogledajmo sada primer fajla koji u svojim linijama čuva više podataka odvojenih specijalnim znakom (,). Sadržaj fajl studenti.txt:

```bash
Marko Nikolic,Masinsko inzenjerstvo,50
Ana Petrovic,Urbano inzenjerstvo,48
Milica Nikolic,Vojno inzenjerstvo,47
Goran Filipovic,Zastita zivotne sredine,42
Janko Cvetic,Masinsko inzenjerstvo,39
```

U ovom slučaju osim čitanja linija možemo podeliti svaku od njih kako bismo dobili odvojene podatke:

```python
with open('studenti.txt', 'r') as fajl:
    linije = fajl.readlines()

print(linije)
```

daje:

```bash
['Marko Nikolic,Masinsko inzenjerstvo,50\n', 'Ana Petrovic,Urbano inzenjerstvo,48\n', 'Milica Nikolic,Vojno 
inzenjerstvo,47\n', 'Goran Filipovic,Zastita zivotne sredine,42\n', 'Janko Cvetic,Masinsko inzenjerstvo,39']
```

Sadržaj fajl sada je smešten u listu niski. Svaka niska ima podatke koji su odvojeni zarezima. Pored toga, uočimo da se svaka od linija završava specijalnim znakom \n. Podelićemo svaku liniju metodom split na mestu zareza. Za početak svakoj liniji uklonimo specijalni znak:

```python
for linija in linije:
    print(linija.rstrip())
```

```bash
Marko Nikolic,Masinsko inzenjerstvo,50
Ana Petrovic,Urbano inzenjerstvo,48
Milica Nikolic,Vojno inzenjerstvo,47
Goran Filipovic,Zastita zivotne sredine,42
Janko Cvetic,Masinsko inzenjerstvo,39
```

A zatim pozivamo i metodu split kako bismo svaku liniju podelili:

```python
for linija in linije:
    print(linija.rstrip().split(','))
```

dobijamo liste niski:

```bash
['Marko Nikolic', 'Masinsko inzenjerstvo', '50']
['Ana Petrovic', 'Urbano inzenjerstvo', '48']
['Milica Nikolic', 'Vojno inzenjerstvo', '47']
['Goran Filipovic', 'Zastita zivotne sredine', '42']
['Janko Cvetic', 'Masinsko inzenjerstvo', '39']
```

Svaka od linija sada je predstavljena kao lista niski o studentu. Svaka on niski u listi o studentu ima svoju poziciju (indeks) kojim ćemo pristupiti vrednosti. Kreiramo sada od svake linije formatiranu informaciju o studnetu:

```python
for linija in linije:
    linija = linija.rstrip().split(',')
    print(f'Student {linija[0]} studira {linija[1]}.')
```

i dobijamo:

```bash
Student Marko Nikolic studira Masinsko inzenjerstvo.
Student Ana Petrovic studira Urbano inzenjerstvo.
Student Milica Nikolic studira Vojno inzenjerstvo.
Student Goran Filipovic studira Zastita zivotne sredine.
Student Janko Cvetic studira Masinsko inzenjerstvo.
```

Na kraju možemo raspakovati listu linija u promenljive koje ćemo dalje koristiti:

```python
with open('studenti.txt', 'r') as fajl:
    linije = fajl.readlines()

for linija in linije:
    ime, smer, bodovi = linija.rstrip().split(',')
    print(f'Student {ime} studira {smer}.')
```
