# Vežbanje
## Prvi primer
Napisati program koji otvara spisak namirnica na stanju u magacinu kao magacin.txt.

Svaka linija fajla predstavlja informaciju o zalihama jednog proizvoda.


    {naziv proizvoda}  {stanje u magacinu}  {optimalno stanje}  {cena po komadu}


Program proverava brojno stanje namirnica. Ukoliko je stanje u magacinu manje od optimuma,
automatski se narucuje onoliko proizvoda koliko nedostaje do optimalnog stanja u magacinu.

Program stampa racun za porudzbinu u posebnom fajlu porudzbina.txt

```python
proizvodi = []                                                           # deklarisanje prazne liste
with open('magacin.txt', 'r') as fajl:                                   # otvaranje tekstualnog fajla
    for linija in fajl:                   
        naziv, stanje, optimum, cena = linija.rstrip().split(',')        # razdvajanje linije na mestu prosleđenog znaka (',') i smeštanje u promenljive
        if (int(stanje) < int(optimum)):                                 # ukoliko je stanje manje od optimalnog
            proizvod = {'naziv':naziv, 'cena':int(cena), 'kolicina':abs(int(stanje)-int(optimum))}     # definiši rečnik
            proizvodi.append(proizvod)                                   # smesti rečnik u listu

with open('narudzbina.txt', 'w') as fajl:                                # otvaramo izlazni fajl u modu za pisanje
    ukupno = 0 
    for proizvod in proizvodi:
        ukupno += proizvod['cena']*proizvod['kolicina']                  # izračunavanje ukupnog troška
 #upisivanje u fajl proizvoda, količine i ukupne cene proizvoda
        fajl.write(f"{proizvod['naziv']}, {proizvod['kolicina']}, {proizvod['cena']*proizvod['kolicina']}\n")   
    fajl.write(f'Ukupno {ukupno}')                                       # upisivanje ukupne vrednosti porudžbine
```





