# Python Julski ispitni rok 2023

## Prvi zadatak
Napisati funkciju koja preuzima celobrojni niz i pozitivnim brojevima dodeljuje vrednost 0.
Funkcija glavnom programu vraća procenat članova koji su jednaki 0.

<details markdown='block'>
<summary>Rešenje</summary>
  
```python
def funkcija(niz):
    brojac = 0
    for broj in niz:
        if broj > 0:
            broj = 0
            brojac +=1
    return brojac/len(niz)*100
        

#glavni program:
print(funkcija([1, 2, -3, 4, -5]))

```
</details>

## Drugi zadatak
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
