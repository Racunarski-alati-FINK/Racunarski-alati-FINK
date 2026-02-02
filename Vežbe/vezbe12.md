# Vežbanje
## Prvi primer
Napisati program koji otvara spisak namirnica na stanju u magacinu kao magacin.txt.

Svaka linija fajla predstavlja informaciju o zalihama jednog proizvoda.

{naziv proizvoda},{stanje u magacinu},{optimalno stanje},{cena po komadu}

Program proverava brojno stanje namirnica. Ukoliko je stanje u magacinu manje od optimuma,
automatski se narucuje onoliko proizvoda koliko nedostaje do optimalnog stanja u magacinu.

Program stampa racun za porudzbinu u posebnom fajlu porudzbina.txt

```python
proizvodi = []
with open('magacin.txt', 'r') as fajl:
    for linija in fajl:
        naziv, stanje, optimum, cena = linija.rstrip().split(',')
        if (int(stanje) < int(optimum)):
            proizvod = {'naziv':naziv, 'cena':int(cena), 'kolicina':abs(int(stanje)-int(optimum))}
            proizvodi.append(proizvod)

with open('narudzbina.txt', 'w') as fajl:
    ukupno = 0 
    for proizvod in proizvodi:
        ukupno += proizvod['cena']*proizvod['kolicina']
        fajl.write(f"{proizvod['naziv']}, {proizvod['kolicina']}, {proizvod['cena']*proizvod['kolicina']}\n")
    fajl.write(f'Ukupno {ukupno}')
```

