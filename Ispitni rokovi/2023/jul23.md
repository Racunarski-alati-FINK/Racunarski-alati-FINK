# Python Julski ispitni rok 2023.
## Prvi zadatak
Napisati funkciju koja uzima celobrojni niz. Funkcija stampa sume svih opadajucih pod nizova.

<details markdown='block'>
<summary>Rešenje</summary>
  
```python
def funkcija(niz):
    privremeni = [niz[0]]
    glavni = []
    for i in range(0,len(niz)-1):
        if niz[i] > niz[i+1]:
            privremeni.append(niz[i+1])
        else:
            if len(privremeni) > 1:
                glavni.append(privremeni)
                privremeni = [niz[i+1]]
            else:
                privremeni = [niz[i+1]]
    glavni.append(privremeni)
             
    for podniz in glavni:
        print(sum(podniz))

funkcija([5, 4, 9, -11 , 13, 19, 2, 6, -7])
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl spisak.txt u kome svaka linija sadrži naziv proizvoda, količinu i cenu u formatu:

    namirnica, kolicina, cena

Program čita fajl i kreira novi fajl u kome se štampaju imena proizvoda i novac potrošen na tu namirnicu (količina*cena po komadu).
Format izlaznog fajla kupovina.txt:

    namirnica novac 
                                    
poslednja linija fajla je:    ukupno = suma potrošenog novca

<details markdown='block'>
<summary>Rešenje</summary>
  
```python
 def kupovina(ulaz):
     korpa = []
     suma = 0
     with open(ulaz, 'r') as fajl:
         for linija in fajl:
             namirnica, kolicina, cena = linija.rstrip().split(',')
             korpa.append((namirnica, int(kolicina)*int(cena)))
            
     with open('kupovina.txt', 'w') as fajl:
         for proizvod in korpa:
             suma += proizvod[1]
             fajl.write(f'{proizvod[0]} {proizvod[1]}\n')
         fajl.write(f'Ukupno = {suma}')
#glavni program:
kupovina('spisak.txt')
```
</details>


