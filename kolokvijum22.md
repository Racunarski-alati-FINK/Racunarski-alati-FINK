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
