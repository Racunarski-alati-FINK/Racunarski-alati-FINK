# Python Februarski ispitni rok 2023.

## Grupa 1a
## Prvi zadatak
Napisati funkciju koja uzima niz celih brojeva A i ceo broj X, a zatim računa srednju vrednost članova manjih od X i najmanju vrednost u nizu. 
Funkcija glavnom programu vraća razliku srednje vrednosti članova manjih od X i najmanje vrednosti niza

primer: 

	A = [1, 2, -3, 4, -5]
    razlika = 3.75


<details markdown='block'>
<summary>Rešenje </summary>

```python
def funkcija(A,X):
    suma = 0
    br = 0
    for i in range(len(A)):
        if A[i] < X:
            suma += A[i]
            br += 1
    srednja_vrednost = suma/br
    min = A[0]
    for i in range(1,len(A)):
        if A[i] < min:
            min = A[i]
    return srednja_vrednost - min


# poziv glavnog programa
print(funkcija([1, 2, -3, 4, -5],4)
```
</details>

## Drugi zadatak
Napisati program koji otvara fajl [bioskop.txt](https://github.com/Racunarski-alati-FINK/Racunarski-alati-FINK/blob/main/Ispitni%20rokovi/Ulazni%20fajlovi/2023/Februar/bioskop.txt) koji sadrži spisak filmova formatu:

    naziv filma,vreme početka, trajanjae (min)
    Avatar, 14:52, 130
U izlazni fajl štampati nazive filmova sortirane u rastućem redosledu po vremenu završetka.

<details markdown='block'>
<summary>Rešenje </summary>
spisak = []
with open ('bioskop.txt','r') as fajl:
    for linija in fajl:
        naziv_filma, vreme_pocetka, trajanje = linija.lstrip().rstrip().split(',')   
        sati, minuti = vreme_pocetka.split(':')
        ukupno_vreme = int(sati) * 60 + int(minuti) + int(trajanje)
        film = {'naziv_filma':naziv_filma, 'vreme_zavrsetka':ukupno_vreme}
        spisak.append(film)


with open ('rezultat_1a.txt', 'w') as fajl:
    for film in sorted(spisak, key = lambda film:film['vreme_zavrsetka']):
        fajl.write(f"{film['naziv_filma']}\n")
```
</details>
