# Map. Filter. Imenovani, pozicioni i podrazumevani parametri

## Map funkcija

map() funkcija uzima kao argumente drugu funkciju i sekvencu iterabilnih i vraćaju kao izlaz funkciju izvršenu nad svakim članom liste. Pretpostavimo da postoji kolekcija podataka torka, lista, set i sl.

Podaci : $a_1$, $a_2$, $a_3$, ..., $a_n$\
Definicija funkcije: f(x)\
Funkcja se izvršava nad svakim članom liste:
$$f(a_1), f(a_2), f(a_3), ..., f(a_n)$$

```python
sintaksa : map(funkcija, iterabilna)
```

* iterabilna : list, tuple, set, ...

Ukoliko postoji niz vrednosti smešten u listu i želimo da vršimo izračunavanje nad svakim članom liste. Za to ćemo koristiti map funkciju.
Izračunati površine krugova čiji su poluprečnici dati listom vrednosti. Dobijene vrednosti površina smestiti u listu i štampati.

```python
poluprecnici = [2, 5, 7.1, 0.3, 10]


# prvi nacin - direktno izracunavanje 

def povrsina(r):
    '''Povrsina kruga radijusa r.'''
    pi = 3.14
    return r*r*pi

povrsine =  []

for r in poluprecnici:
    p = povrsina(r)
    povrsine.append(p)

print(povrsine)      
```

dobijamo rezultat:

```bash
[12.56, 78.5, 158.2874, 0.2826, 314.0] 
```

Drugi način je da koristimo map funkciju i dobijemo rešenje u samo jednoj linij koda:

```python
# Metod 2 : koristeci 'map' funkcija
# koriscenjem map funkcije moguce je da prethodni zadatak uradimo u jednoj liniji

povrsine = map(povrsina, poluprecnici)

print(povrsine) 
```

štampa se:

```bash
<map object at 0x00B4AD70>
```

Kao što se vidi kao rezultat dobijamo iterator map objekat. Ovaj objekat je moguće konvertovati u listu navodjenjem tipa ispred funkcije.

```python
povrsine = list(map(povrsina, poluprecnici))
print(povrsine)
```

i dobijamo:

```bash
[12.56, 78.5, 158.2874, 0.2826, 314.0]
```

Razmotrimo sada primer kada kolekcija sadrži više složenih elemenata poput torki ili setova.

Data je lista torki koje sadrže naziv grada kao niske i celobrojnu vrednost temperature u farenhajtima. Napisati program koji uzima ovu listu i vraća listu sa imenima gradova i temperaturama u celzijusima.Formula za konverziju temperatura je:
$C = 5/9(F-32)$.

```python
temperature = [("Berlin", 60), ("Kairo", 90), ("Buenos aires", 70), ("Los Anđeles", 79), ("Budimpešta", 44), ("London", 32), ("Beograd", 29)]

# prvi nacin - for petlja po elementima

temperature_c = []

for temperatura in temperature:
    temperature_c.append((temperatura[0], 5/9*(temperatura[1]-32)))

print(temperature_c)
```

Moguće je da definišemo funkciju koja vrši konverziju temperaturama koju možemo koristiti kroz iteracije:

```python
def konverzija(par):
    return (par[0], 5/9*(par[1]-32))

temperature_c = []

for temperatura in temperature:
    temperature_c.append(konverzija(temperatura))

print(temperature_c)
```

Najbolja praksa je da se kod jednostavnih funkcija one definišu kao lambda - jednolinijske funkcije. Ove funkcije su posebno efikasne kod sortiranja, map i filter funkcija.

```python
# def konverzija(par):
#    return (par[0], 5/9*(par[1]-32))

konverzija = lambda par: (par[0], 5/9*(par[1]-32))

temperature_c = []

for temperatura in temperature:
    temperature_c.append(konverzija(temperatura))

print(temperature_c)
```

Sada sve gore navedeno možemo zameniti map funkcijom i dobiti rešenje u jednoj liniji koda:

```python
temperature_c = list(map(konverzija, temperature))

print(temperature_c)
```

dobijamo:

```bash
[('Berlin', 15.555555555555557), ('Kairo', 32.22222222222222), ('Buenos aires', 21.11111111111111), ('Los Anđeles', 26.11111111111111), ('Budimpešta', 6.666666666666667), ('London', 0.0), ('Beograd', -1.6666666666666667)]
```

## Filter funkcija

filter() funkcija omogućava filtriranje (selekciju) elemenata iz
kolekcija. Ova funkcija uzima drugu funkciju u sekvenci iterabilnih kao parametre. Filter funkcija vraća sekvencu za koju funkcija vraća vrednost True.

Podaci : $a_1$, $a_2$, $a_3$, ..., $a_n$.\
Definicija funkcije: $f(x)$.\
Funkcija se izvršava nad svakim članom liste:
$$f(a_1), f(a_2), f(a_3), ..., f(a_n)$$

Najjednostavniji način korišćenja filter funkcija je filtriranje konkretnih brojevnih vrednosti na osnovu nekog jednostavnog uslova (>, <, =, >=, <=). Uzmimo primer liste vrednosti iz koje želimo da izdvojimo vrednosti veće od proseka svih vrednosti iz liste:

```python
podaci = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

prosek = sum(podaci)/len(podaci)

print(prosek)

vrednosti = []
for vrednost in podaci:
    if vrednosti > prosek:
        vrednosti.append(vrednost)

print(vrednosti)
```

Rezultat izvršavanja koda je:

```bash
2.183333333333333
[2.7, 4.1, 4.3]
```

Definišimo sada funkciju koja određuje koji su članovi veći od proseka:

```python
podaci = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

prosek = sum(podaci)/len(podaci)

print(prosek)

def veci(vrednost, prosek):
    return vrednost > prosek
vrednosti = []
for vrednost in podaci:
    if veci(vrednost, prosek):
        vrednosti.append(vrednost)

print(vrednosti)
```

Za kraj definišemo lambda funkciju i pozovimo filter funkciju koja će kreirati listu vrednosti:

```python
podaci = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

prosek = sum(podaci)/len(podaci)

print(prosek)

# def veci(vrednost, prosek):
#     return vrednost > prosek
# vrednosti = []
# for vrednost in podaci:
#     if veci(vrednost, prosek):
#         vrednosti.append(vrednost)

veci = lambda vrednost: vrednost > prosek

vrednosti = list(filter(veci, podaci))

print(vrednosti)
```

čime na jednostavniji način dobijamo isti rezultat. Na isti način jednostavnom izmenom možemo dobiti vrednosti manje od proseka:

```python
vrednosti = list(filter(lambda x: x < prosek, podaci))
print(vrednosti)
```

Filter funkciju je pored brojevnih tipova moguće koristiti i sad niskama:

```python
reci = ["", 'tabla', "", "mis", "racunar", "", "prozor"]

funkcija = lambda rec: rec != ""

filtrirano = list(filter(funkcija, reci))

print(filtrirano)
```

Razmotrimo sada primer kada kolekcije sadrže složenije strukture poput torki. Data je lista torki proizvoda sa nazivom i cenom. Korišćenjem filter funkcije filtrijamo proizvode čija je cena niža od 200 dinara. Prvo ćemo koristiti klasičan pristup for petlje i iteriranja:

```python
proizvodi = [("Proizvod 1", 100), ("Proizvod 2", 115), ("Proizvod 3", 220), ("Proizvod 4", 440), ("Proizvod 5", 66)]

filtrirano = []
for proizvod in proizvodi:
    if proizvod[1] < 200:
        filtrirano.append(proizvod)

print(filtrirano)
```

čime dobijamo:

```bash
[('Proizvod 1', 100), ('Proizvod 2', 115), ('Proizvod 5', 66)]
```

Isti rezultat na elegantniji način možemo dobiti korišćenjem filter i lambda funkcije:

```python
filtrirano = list(filter(lambda proizvod: proizvod[1]<200, proizvodi))
print(filtrirano)
```

Takođe, na jednostavan način možemo i kreirati listu cena proizvoda kako bismo pokazali razliku filter i map funkcije:

```python
cene = list(map(lambda proizvod: proizvod[1], proizvodi))
print(cene)
```

Iako su lambda funkcije efikasne i jednostavne za korišćenje sa map i filter funkcijama njih nije moguće uvek koristiti. Pogledajmo sada jedan jednostavan primer u kojem je neophodno kreirati složeniju funkciju radi mapiranja liste:

```python
bodovi = [77, 97, 64, 85, 49, 55, 41, 39, 92, 70]

def ocena(bodovi):
    if bodovi >= 90:
        return 10
    elif bodovi >= 80:
        return 9
    elif bodovi >= 70:
        return 8
    elif bodovi >= 70:
        return 7
    elif bodovi >= 60:
        return 6
    else:
        return 5
    
ocene = list(map(ocena, bodovi))
print(bodovi)
print(ocene)

def nisu_polozili(bodovi):
    return bodovi < 50

pali = list(filter(nisu_polozili, bodovi))
print(bodovi)
print(pali)
```

dobijamo:

```bash
[77, 97, 64, 85, 49, 55, 41, 39, 92, 70]
[8, 10, 6, 9, 5, 5, 5, 5, 10, 8]
[77, 97, 64, 85, 49, 55, 41, 39, 92, 70]
[49, 41, 39]
```

## Podrazumevani, pozicioni i imenovani parametri funkcija

Pogledajmo na početku jednu osnovnu definiciju krajnje jednostavne funkcije koja štampa vrednost prosleđenog parametra: 

```python
def funkcija(x):
    print(x)

funkcija(2) 
funkcija(10)
funkcija(100)
```

čime dobijamo:

```bash
2
10
100
```

U fukcijama je moguće definisati takozvani podrazumevani parametar (argument) čija će vrednost biti iskorišćena ukoliko funkciji ne bude prosleđena vrednost parametra:

```python
def funkcija(x=10):
    print(x)

funkcija(2)
funkcija()
funkcija(100)
```

Kao što vidimo u drugom pozivu funkcije ne navodimo argumente usled čega će funkcija koristiti podrazumevanu vrednost x. Rezultat koji dobijamo je istovetan prvobitnoj verziji:

```bash
2
10
100
```

Pogledajmo još jedan ranije korišćen primer sa više argumenata:

```python
def pozdrav(pozdrav = 'Gde si', ime='Petre'):
    print(f'{pozdrav}, {ime}')

pozdrav('Zdravo', 'Ana')
pozdrav('Cao', 'Milose')
pozdrav()
```

Funkcija uzima dva argumenta i kreira jednostavnu nisku kao pozdrav. U definiciji funkcije dodeljujemo podrazumevane vrednosti argumentima. Pri pozivu bez argumenata vidimo da se koriste podrazumevane vrednosti u telu funkcije:

```bash
Zdravo, Ana
Cao, Milose
Gde si, Petre
```

Ipak ovde treba biti obazriv jer se argumenti prosleđuju redom navođenja pa tako može doći do sledeće situacije:

```python
pozdrav('Jovana')
```

što daje:

```bash
Zdravo, Ana
Cao, Milose
Gde si, Petre
Jovana, Petre
```

Vidimo da se vrednosti argumenata prosleđuju po redosledu. Ukoliko ih ima manje od broja u definiciji neki od njih ostaju neizmenjeni kao u ovom slučaju. To je moguće izbeći kombinovanjem podrazumevanih i pozicionih parametara:

```python
def pozdrav(pozdrav, ime='X'):
    print(f'{pozdrav}, {ime}')
```

U ovom slučaju prvi arugment se prosleđuje po poziciji prvom argumentu u definiciji dok drugi može biti prosleđen ili ostati podrazumevan. Takođe nije moguće da podrazumevani parametri budu ispred onih koji nisu defnisani, odnosno pozicionih parametara:

```python
def pozdrav(pozdrav='Cao', ime):    # greska jer podrazumevani parametri moraju biti iza pozicionih
    print(f'{pozdrav}, {ime}')
```

Kako se u definiciji koriste nazivi promenljivih moguće je pri pozivu koristiti njihove nazive radi prosleđivanje vrednosti. U tom slučaju nazivamo ih imenovanim argumentima:

```python
def izracunaj(a, b):
    return a + b

print(2, 3)
print(izracunaj(b=2, a=6))
```

Rezultat je:

```bash
5
8
```

Pri prvom pozivu funkcije vrednosti argumenata smo prosledili po poziciji u definiciji dok u drugom pozivu koristimo imenovanu dodelu vrednosti. Oba načina su ispravna.
Sve navedeno je jako korisno ko rada sa naprednim funkcijama, rada sa fajlovima i sortiranja velike količine podataka. Pokazaćemo to, za početak, na nekoliko jednostavnih primera. 

Prvi primer je lista celih brojeva koji su nasumično raspoređeni. Zadatak je da sortiramo listu u opadajućem redosledu. Za ovo je moguće napisati poseban program koji sortira listu. Mi ćemo u ovom slučaju problem da rešimo korišćenjem ugrađene funkcije sorted koja radi sa listama.

```python
brojevi = [3, 6, 1, -10, 8, 9, -2, 100, 5, -3, 11]

print(sorted(brojevi))
```

dobijamo:

```bash
[-10, -3, -2, 1, 3, 5, 6, 8, 9, 11, 100]
```

Rezultat koji smo dobili nije lista opadajućih vrednosti. To znači da funkcija sorted podrazumevano radi sortiranje u rastućem redosledu. Ukoliko pogledamo definiciju funkcije sorted videćemo da postoji podrazumevani argument reverse (obrnuto) kojem je dodeljena vrednost False.

```python
brojevi = [3, 6, 1, -10, 8, 9, -2, 100, 5, -3, 11]

print(sorted(brojevi))    # [-10, -3, -2, 1, 3, 5, 6, 8, 9, 11, 100]

print(sorted(brojevi, reverse=False)) 
```

Ukoliko ovaj argument izmenimo dobićemo sortiranje u opadajućem redosledu:

```python
brojevi = [3, 6, 1, -10, 8, 9, -2, 100, 5, -3, 11]

print(sorted(brojevi))    # [-10, -3, -2, 1, 3, 5, 6, 8, 9, 11, 100]

print(sorted(brojevi, reverse=True)) 
```

```bash
[-10, -3, -2, 1, 3, 5, 6, 8, 9, 11, 100]
[100, 11, 9, 8, 6, 5, 3, 1, -2, -3, -10]
```

Pored podrazumevanog argument reverse, sorted funkciji je moguće putem argumenta key proslediti funkciju ili argument po kojem će se vršiti sortiranje:

```python
strs = ['ccc', 'aaaa', 'd', 'bb']

print(sorted(strs, key=lambda rec: len(rec), reverse=False))
```

Ovim funkciji sorted saopštavamo da želimo da u obrnutom redosledu sortiramo listu reči a da kao kriterijum za sortiranje koristimo dužinu svake reči:

```bash
['d', 'bb', 'ccc', 'aaaa']
```

i obrnuto:

```python
print(sorted(strs, key=lambda rec: len(rec), reverse=True)) 
```

```bash
['aaaa', 'ccc', 'bb', 'd']
```

Ukratko možemo objasniti da se kao među vrednosti u funkciji kreiraju dužine svake od reči a zatim se po kriterijumu dužine reči ova lista sortira.

![Način sortiranja niza preko key argumenta](sortiranje.png)
