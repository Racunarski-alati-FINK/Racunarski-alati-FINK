# Linijski i razgranati programi

## Linijski programi

Kod linijskih programa sve komande (naredbe) se izvršavaju jedna za drugom. Primer linijskog programa dat je na slici ispod.

![Definicija i primer linijskog programa](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/08774075-819e-4f89-807e-1d71686468f9)

Primer linijskog programa:

```python
broj1 = float(input('Unesi prvi broj: '))
broj2 = float(input('Unesi drugi broj: '))
zbir = broj1 + broj2

print('Zbir je '+ str(zbir))
```

## Razgranati programi

### Naredba if

Grafički prikaz naredbe if u programu prikazan je na slici dole.

![Grafički prikaz naredbe if](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/79278f05-469d-4bb3-8b69-ce4f203c31bb)

```python
if uslov:
    naredba
```

```python
if broj > 0:
    print('broj je pozitivan')
```

### Naredba if-else

Grafički prikaz naredbe if-else u programu prikazan je na slici dole.

![Grafički prikaz naredbe if-else](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/183f573d-52f9-4d40-b5ec-24d998278348)

```python
if uslov:
    prva naredba
else:
    druga naredba
```

```python
if broj % 2 == 0:
    print('broj je paran')
else:
    print('broj je neparan')
```

### Naredba if-elif-else

Grafički prikaz naredbe if-else u programu prikazan je na slici dole.

![Grafički prikaz naredbe if-elif-else](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/assets/152398242/bcf901b9-8826-4746-a4d8-f564d926b90e)

```python
if uslov:
    prva naredba
elif uslov :
    druga naredba
elif uslov :
    treća naredba
....
else:
    n-ta naredba
```

```python
if a > 0:
    print('broj je pozitivan')
elif a < 0:
    print('broj je negativan')
else:
    print('nula')
```

### Indentacija - uvlačenje blokova

Sve komande koje pripadaju određenom bloku if naredbe moraju biti uvučene jedan tab ispod početne linije if naredbe.

```python
if uslov:
    naredba
```

Isto važi i za if-else i if-elif-else strukturu bez obzira na broj blokova komandi:

```python
if uslov:
    prva naredba
else:
    druga naredba
```

```python
if uslov:
    prva naredba
elif uslov :
    druga naredba
else:
    n-ta naredba
```

Pored prikazanih moguće je imati i ugnježđene if naredbe (if naredbe u okviru if naredbi). I u tom slučaju treba poštovati indentaciju odnosno uvlačenje blokova:

```python
if uslov1:
   if uslov2:
      if uslov3:
         naredba
```

**Svaki novi blok naredbi je odvojen uvlačenjem (najčešće 4 razmaka)!**

### Relacijski operatori

| Znak  | Opis                   | Primer      |
|-------|-------------------------|-------------|
| ==     | jednakost            | a==b           |
| >    | veće od       | a>b        |
| <     | manje od | c<d   |
| >=     | veće ili jednako     | a>=b |
| <=     | manje ili jednako     | d<=f |
| !=     | različito     | a!=b |
| and     | i(oba moraju biti tačna)     | a^b |
| or     | ili (makar jedna mora biti tačan)    | a||b |
| not     | negacija     | !a |

Relacijski operatori se koriste za:

* ispitivanje jednakosti:
  
  ```python
  a = 10; b = 3
  a == b => False
  
  ime_studenta = "Ana Petrovic"
  ime_studenta == "Ana Petrovic" => True
  ```

* veće ili manje, veće ili jednako, manje ili jednako

  ```python
  a = 10; b = 3
  a >= b => True
  a <= b => False
  ```

* ispitivanje različitosti
  
  ```python
  broj = 7
  broj % 2 != 0 => True

  ime_studenta = "Ana Petrovic"
  ime_studenta != "Ana Petrovic" => False
  ```

* povezivanje sa and i or

  ```python
  student_masinstva = True
  student_medicine = False
  diplomirao = True

  masinski_inzenjer = student_masinstva and diplomirao
  student = student_masinstva or student_medicine
  ```

* složeni izrazi - poređenje i logički operatori

  ```python
  godine = 21
  (godine >= 19) and (godine <= 30)
  ```

### Primer

Date su koordinate tri temena pravougaonika sa celobrojnim koordinatama čije su stranice paralelne sa koordinatnim osama. Temena su zadata u proizvoljnom redosledu. Napisati program kojim se određuju koordinatne ose četvrtog temena.

![Primer 1](primer1.png)

```python
Ax = int(input('Unesi x koordinatu tacke A: '))
Ay = int(input('Unesi y koordinatu tacke A: '))
Bx = int(input('Unesi x koordinatu tacke B: '))
By = int(input('Unesi y koordinatu tacke B: '))
Cx = int(input('Unesi x koordinatu tacke C: '))
Cy = int(input('Unesi y koordinatu tacke C: ))
if Ax == Bx:
    Dx = Cx
if Ax == Cx:
    Dx = Bx
if Bx == Cx:
    Dx = Ax
if Ay == By:
    Dy = Cy
if Ay == Cy:
    Dy = By
if By == Cy:
    Dy = Ay
print(f"Koordinate tacke D su ({Dx},{Dy})")
```

### Primer 2

Napisati program koji prema tabeli izračunava ocenu studenta.

| Broj poena | Ocena  |
|-------|-----|
| 91-100     | 10            |
| 81-90    | 9       |
| 71-80     | 8 |
| 61-70   | 7     |
| 51-60     | 6 |
| <51     | 5 |

```python
if broj_poena >= 90:
   ocena = 10
if broj_poena >= 80 and broj_poena < 90:
   ocena = 9
if broj_poena >= 70 and broj_poena < 80:
   ocena = 8
if broj_poena >= 60 and broj_poena < 70:
   ocena = 7
if broj_poena >= 51 and broj_poena < 60:
   ocena = 6
if broj_poena <= 50:
   ocena = 5
    
print(f"Ocena studenta je {ocena}")
```

### Primer 3

Napisati program koji za uneti ceo broj stampa mešoviti broj – celobrojni deo i razlomak.

```python
brojilac = int(input('Unesi brojilac: '))
imenilac = int(input('Unesi delilac: '))

ceo_broj = brojilac // imenilac
ostatak = brojilac % imenilac 
print(f"Mesovit broj je {ceo_broj} {ostatak}/{imenilac}")
```

izbegavanje deljenja nulom:

```python
brojilac = int(input('Unesi brojilac: '))
imenilac = int(input('Unesi delilac: '))

ceo_broj = brojilac // imenilac
ostatak = brojilac % imenilac 
if ceo_broj != 0:
     print(f"Mesovit broj je {ceo_broj} {ostatak}/{imenilac}")
else:
     print(f"Mesovit broj je {ostatak}/{imenilac}")
```

### Primer 4

Napisati program računa funkciju $y=(x1, x2)$ izračunava za unete realne brojeve prema:

* $y = x1 + x2$ ako je $x1 < x2$
* $y = x1 * x2$ ako je $x1 = x2$
* $y = x1 + x2$ ako je $x1 > x2$

```python
x1 = float(input('Unesite x1: '))
x2 = float(input('Unesite x2: '))
if x1 < x2:
   y = x1 + x2
elif x1 == x2:
   y = x1 * x2
else:
   y = x1 - x2
print(f"y = {y}")
```

### Primer 5

Napisati program koji proverava da li je uneta godina prestupna. Godina se smatra prestupnom ako je broj godine deljiv sa 4 a nije deljiv sa 100, ili je deljiv sa 400.

```python
godina = int(input('Unesi godinu: '))
if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print("prestupna godina")
else:
    print('godina nije prestupna')
```

### Primer 6

Napisati program koji omogućava izvršavanje osnovnih računskih operacija.

```python
prvi_broj = float(input('Unesi prvi broj: '))
drugi_broj = float(input('Drugi broj: '))
operacija = input('Unesi racunsku operaciju (+, -, *, /): ')
if operacija == '+':
    rezultat = prvi_broj + drugi_broj
elif operacija == '-':
    rezultat = prvi_broj - drugi_broj
elif operacija == '*':
    rezultat = prvi_broj * drugi_broj
elif operacija == '/':
    rezultat = prvi_broj / drugi_broj
print(f"Rezultat operacije {operacija} na brojevima {prvi_broj} i {drugi_broj} je: {rezultat}")
```

```python
prvi_broj = float(input('Unesi prvi broj: '))
drugi_broj = float(input('Drugi broj: '))
operacija = input('Unesi racunsku operaciju (+, -, *, /): ')
if operacija == '+':
   rezultat = prvi_broj + drugi_broj
elif operacija == '-':
   rezultat = prvi_broj - drugi_broj
elif operacija == '*':
   rezultat = prvi_broj * drugi_broj
elif operacija == '/':
   rezultat = prvi_broj / drugi_broj
else:
   print('Niste uneli jednu od operacija, rezulat se nece stampati')
    
print(f"Rezultat operacije {operacija} na brojevima {prvi_broj} i {drugi_broj} je: {rezultat:.3f}")
```

```python
racunaj = True
prvi_broj = float(input('Unesi prvi broj: '))
drugi_broj = float(input('Drugi broj: '))
operacija = input('Unesi racunsku operaciju (+, -, *, /): ')
if operacija == '+':
   rezultat = prvi_broj + drugi_broj
elif operacija == '-':
   rezultat = prvi_broj - drugi_broj
elif operacija == '*':
   rezultat = prvi_broj * drugi_broj
elif operacija == '/':
   rezultat = prvi_broj / drugi_broj
else:
   print('Niste uneli jednu od operacija, rezulat se nece stampati')
   racunaj = False
    
if racunaj:  # isto sto i racunaj == True
   print(f"Rezultat operacije {operacija} na brojevima {prvi_broj} i {drugi_broj} je: {rezultat:.3f}")
```

### Primer 7

Napisati program koji utvrđuje da li su dva uneta broja istog znaka.

```python
a = int(input())
b = int(input())
if a > 0:
      if b > 0:
         istog_znaka = True
      else: # b < 0
         istog_znaka = False
else: # a < 0
   if b > 0:
      istog_znaka = False
   else: # b < 0
      istog_znaka = True
if istog_znaka:
   print('da')
else:
   print('ne')
```

```python
a = int(input())
b = int(input())
istog_znaka = False
if (a > 0 and b > 0) or (a < 0 and b < 0):
   istog_znaka = True
if istog_znaka:
    print(f"Brojevi {a} i {b} su istog znaka")
else:
   print(f"Brojevi {a} i {b} nisu istog znaka")
```

```python
a = int(input())
b = int(input())
istog_znaka = False
if a * b > 0:
   istog_znaka = True
if istog_znaka:
   print(f"Brojevi {a} i {b} su istog znaka")
else:
   print(f"Brojevi {a} i {b} nisu istog znaka")
```
