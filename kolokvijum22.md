# Python II kolokvijum 2022.

## Grupa 1a

## Prvi zadatak
Napisati funkciju koja ce izracunavati razliku izmedju zbira negativnih clanova ispod glavne dijagonale i proizvoda clanova iznad glavne dijagonale kvadratne celobrojne matrice dimenzija n x n.

<details markdown='block'>
<summary>Rešenje </summary>

```python
def funkcija(matrica):
	suma_ispod = 0
	proizvod_iznad = 1
	for i in range(len(matrica)):
    	for j in range(len(matrica)):
        	if i > j:
            	if matrica[i][j] < 0:
                	suma_ispod += matrica[i][j]
             elif i < j:
                     proizvod_iznad *= matrica[i][j]
	return suma_ispod - proizvod_iznad

# poziv glavnog programa
print(funkcija([[2, -4, 3], [3, -2, 1], [-8, 5, 2]]))
```
</details>


## Drugi zadatak
Napisati program koji otvara fajl rezultati.txt u kome svaka linija sadrzi ime studenta, poene na prvom i drugom kolokvijumu u formatu:
ime,poeni1,poen2
Program čita fajl i kreira fajlove položili.txt i nisu_polozili.txt u kojima se u abecednom redu ispisuju imena studenata. Student je položio ako je suma poena > 51. Format:
ime studenta

<details markdown='block'>
<summary>Rešenje korišćenjem uređenenih parova </summary>
	
```python
polozili = []
nisu_polozili = []
with open('ulaz1a.txt') as fajl:
	for linija in fajl:
	    ime, poeni1, poeni2 = linija.rstrip().split(',')
         poeni = int(poeni1) + int(poeni2)
         if poeni > 51:
             polozili.append((ime, poeni))
         else:
             nisu_polozili.append((ime, poeni))


with open('polozili.txt', 'w') as fajl:
 	for student in sorted(polozili):
        fajl.write(f"{student[0]}\n")

with open('nisu_polozili.txt', 'w') as fajl:
	for student in sorted(nisu_polozili):
    	fajl.write(f"{student[0]}\n")
```

</details>

<details markdown='block'>
<summary>Rešenje korišćenjem rečnika </summary>
	
``` python
polozili = []
nisu_polozili = []
with open('ulaz1a.txt') as fajl:
	for linija in fajl:
    	ime, poeni1, poeni2 = linija.rstrip().split(',')
        poeni = int(poeni1) + int(poeni2)
        student = {'ime':ime, 'poeni':poeni}
        if poeni > 51:
            polozili.append(student)
        else:
            nisu_polozili.append(student)

with open('polozili_recnici.txt', 'w') as fajl:
	for student in sorted(polozili, key=lambda student: student['ime'], reverse=False):
		fajl.write(f"{student['ime']}\n")

with open('nisu_polozili_recnici.txt', 'w') as fajl:
	for student in sorted(nisu_polozili, key=lambda student: student['ime'], reverse=False):
		fajl.write(f"{student['ime']}\n")
```
</details>
