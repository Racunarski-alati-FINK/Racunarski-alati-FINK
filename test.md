# Vežbe

## Funkcije

Funkcije služe da razlože velike programe na manje celine kako bi bili lakši za održavanje i razumevanje. Takođe funkcije nam omogućavaju da izbegnemo pisanje istog koda u različitim delovima našeg programa.

### Osnove funkcija

Funkcije se definišu ključnom rečju **def**. Komanda se završava navođenjem dvotačke (:). Kod koji pripada funkciji mora biti uvučen za jedan tab ispod def komande. Primer jednostavne funkcije možemo videti ispod:

```python
def print_hello():
    print('Hello!')

print_hello()
```

Prve dve linije definišu funkciju. Poslednja linija predstavlja pozivanje definisane funkcije.

## Python moduli

Posebnu snagu programskog jezika pored osnovnih komandi jezika predstavlja i široka kolekcija dodatnog softvera koji se sadržan u različitim modulima, bibliotekama ili paketima. Neki od paketa deo su osnovne verzije programskog jezika dok je neke od specijalizovanih paketa neophodno naknadno instalirati. Pristup paketima ostvaruje se navođenjem ključne reči **import** i naziva paketa. Četiri najpoznatija Python paketa koji nisu deo osnovnog jezika su:

* NumPy je standardni paket za naučno računarstvo u Pythonu. Jedan od najmoćnijih delova ovog pakete jesu nizovi kao struktura podataka. Posebno se istuču alati koji služe za kreiranje i manipulaciju nizovima poput sortiranja i osnovim operacijama član po član. Pored nizova ovaj paket sadrži osnovne matematičke funkcije iz trigonometrije, eksponencijalne i logaritamske kao i niza statističkih funkcija i operacija iz linearne algebre.
* SciPy obezbeđuju širok spektar matematičkih funkcija i numeričkih rutina u Python. SciPy omogućava još naprednije korišćenje NumPy nizova i najčešće se koriste zajedno u okviru programa. Pored niza opcija i struktura koje su zajedničke za ova dva paketa SciPy omogućava kreiranje programa koji mogu komunicirati sa eksternim programima napisanim u Fortranu, C ili C++. SciPy paket čini Python još moćnijim alatom u operacijama poput fitovanja krivih, numeričkog rešavanja diferencijalnih jednačina i optimizacije.
* matplotlib je standardni Python paket za kreiranje 2D i 3D grafikona.
* Pandas je Python paket namenjen analizi podataka nalik excelu. U pogledu alata i načina korišćenja ovaj paket omogućava korisnicima napredno uređivanje i pretragu podataka na način daleko interaktivniji od programa poput Excela

### Python moduli i funkcije

Navedeni paketi nisu deo osnovne verzije Pythona i moraju biti uvezeni kako bismo omogućili pristup njihovim funkcijama i strukturama podataka. Uvozimo paket NumPy:

```python
import numpy

numpy.sin(0.5)

```

daje rezultat:

```bash
0.479425538604203
```

U ovom jednostavnom primeru sin funkcija ima jedan argument 0.5 i kao rezultat vraća sinus prosleđenog argumenta, podrazumevano u radijanima.
Ovde treba primetiti da je bilo neophodno navesti prefik numpy. pre imena konkretne funkcije sin. Na ovaj način saopštavamo Pythonu da je sin funkcija deo uvezenog mogula NumPy.
Pored ovog postoji i drugi modul math koji takođe sadrži sin funkciju. Moguće je uvesti math paket na isti način kako je to učinjeno sa NumPy:

```python
import math
print(math.sin(0.5))
```

daje:

```bash
0.479425538604203
```

Ove dve funkcije nisu identične iako u ovom slučaju daju identičan rezultat. NumPy pored osnovnih može obaviti trigonometrijska izračunavanja sa kompleksnim brojevima:

```python
print(numpy.sin(3+4j))
```

daje:

```bash
(3.853738037919377-27.016813258003932j)
```

Sa druge strane ovo nije moguće učiniti sa osnovnim paketom math:

```python
print(math.sin(3+4j))
```

daje:

```bash
Traceback (most recent call last):
  File "d:\Nastava\Programski jezici\2023_2024\cetvrtak_7_12\vezbe_7_12.py", line 20, in <module>
    print(math.sin(3+4j))
TypeError: can't convert complex to float
```

Pri korišćenju NumPy funkcija više puta pisanje numpy. pre svake funkcije može postati naporno. Python omogućava kreiranje naziva u vidu skraćenice pri uvozu paketa. Podrazumevano u pythonu to činimo na sledeći način:

```python
import numpy as np

print(np.sin(0.5))
```

Prva komanda uvozi i dodeljuje skraćenicu np za numpy paket. Iako je moguće koristiti bilo koju skraćenicu, postoje standardni nazivi skraćenica u Pythonu. U slučaju NumPy to je np. Preporuka je koristiti upravo ove skraćenice radi bolje čitljivosti i standardizovanja koda. 

### NumPy funkcije

NumPy nudi niz matematički funkcija. U tabeli ispod nalazi se niz korisnih funkcija ovog paketa.

| Naziv      | Opis                                               |
|------------|----------------------------------------------------|
| floor(x)   | zaokruživanje decimalnog broja x na manji ceo broj |
| ceil(x)    | zaokruživanje decimalnog broja x na veći ceo broj  |
| sqrt(x)    | kvadratni koren broja x                            |
| exp(x)     | eksponencijalni broj x                             |
| radians(x) | konverzija x iz radijana u stepene                 |
| log10(x)   | logaritam sa osnovom 10 broja x                    |
| degrees(x) | konverzija x iz stepena u radijane                 |
| sin(x)     | sinus broj x u radijanima                          |
| cos(x)     | kosinus broja x u radijanima                       |
| tan(x)     | tangens broja x u radijanima                       |
| arcsin(x)  | arkus sinus broja x u radijanima                   |
| arccos(x)  | arksu kosinus broja x u radijanima                 |
| fabs(x)    | apsolutna vrednost broja x                         |
| round(x)   | zaokruživanje decimalnog broja na ceo broj         |

Argument ovih funkcija može biti bilo koji broj ili izraz čiji je rezultat broj. Primer korišćenja izraza u okviru drugih funkcija je:

```python
print(np.log(np.sin(0.5)))
```

```bash
-0.7351666863853142
```

```python
print(np.log(np.sin(0.5)+1))
```

```bash
0.3916538628347176
```

U svim  ovim slučajevima demonstrirali smo korišćenje funkcija sa jednim ulazom i jednim izlazom. U principu, python funkcije imaju više ulaza i više izlaza.

### Primer

Pretpostavimo da želimo da izračunamo rastojanje između dve koordinate $(x_1, y_1, z_1)$ i $(x_2, y_2, z_2)$:

$$\Delta r = \sqrt{(x_2 - x_1)^2+(y_2 - y_1)^2+(z_2 - z_1)^2}$$

```python
# Izračunava rastojanje između dve 3d Kartezijan koordinate
import numpy as np

x1, y1, z1 = 23.7, -9.2, -7.8
x2, y2, z2 = -3.5, 4.8, 8.1

dr = np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

print(dr)
```

daje:

```bash
34.476803796175766
```

### Različiti načini uvoženja modula

Postoje različiti načini uvoženja modula u Pythona.

Često uvozimo čitave module korišćenjem naredbe import u obliku import ... as ... poput:

```python
import math
import numpy as np
```

Takođe je moguće uvesti i jednu funkciju ili podskup funkcija iz odgovarajućeg modula umesto uvoženja čitavog modula. Npr. pretpostavimo da želimo da uvezemo samo log funkciju iz NumPy:

```python
from numpy import log

a = log(5)
```

Pored jedne moguće je uvesti i čitavu grupu funkcija:

```python
from numpy import log, sin, cos
```

Ukoliko su uvezene na ovaj način moguće ih koristiti bez odgovarajućeg prefiksa kao funkcije koje su uvezene u opšti deo programa. Uopšteno, nije preporučeno koristiti oblik from module import functions način uvoženja funkcija jer se smanjuje čitljivost koda.

Postoji još jedan način uvoza čitavog modula:

```python
from numpy import *
from matplotlib.pyplot import *
```

Na ovaj način uveozimo čitav modul NumPy čime nam u opštem delu programa postaju dostupne sve funkcije modula bez prefiksa.

## Plotovanje

Grafičko prikazivanje podataka često se naziva i plotovanje i jedan je od najvažnijih alata za evaluaciju i shvatanje naučnih podataka i teorijskih predikcija. Plotovanje nije deo osnovne Python verzije ali je moguće kroz nekoliko biblioteka. Najčešće korišćena i razvijena biblioteka u Pythonu je matplotlib. Predstavlja moćan i fleksibilan program koji je postao de facto standard u 2D plotovanju u okviru Pythona.
Kako je matplotlib spoljašnja biblioteka - skup biblioteka - mora biti uvezen u svaku rutinu koja ga koristi. Postoji i više matplotlib podbiblioteka ali je pyplot biblioteka najzastupljenija je omogućava sve što je neophodno za 2D plotovanje. 

```python
import numpy as np
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 2, 3, 4, 3, 4, 5])
plt.grid(True)
plt.show()
```
