# Vežbanje
## Prvi primer
Preformulisati polinom oblika x^2 + 2x^3 + 3x^4 + ... 9x^10 
u python kod i izracunati njegovu vrednost za uneto x.
```python
x = int(input("Unesi broj x = "))
vrednost = 0
for i in range(1,10):
    vrednost = vrednost + i * x ** (i+1)
print(f"Rešenje polinoma za uneto {x} je {vrednost}.")
```
## Drugi primer
Preformulisati polinom oblika 4x^2 + 6x^3 + 8x^4 + ... 20x^10 
u python kod i izracunati njegovu vrednost za uneto x.
```python
x = int(input("Unesi broj x = "))
vrednost = 0
for i in range(4,21,2):
    vrednost = vrednost + i * x ** (i/2)
print(f"Rešenje polinoma za uneto {x} je {vrednost}.")
```
ili:
```python
x = int(input("Unesi broj x = "))
vrednost = 0
koeficijent = 4
stepen = 2
for i in range(9):
    vrednost = vrednost + koeficijent * x ** stepen
    koeficijent += 2
    stepen += 1
print(f"Rešenje polinoma za uneto {x} je {vrednost}.")
```
## Treći primer
Napisati program koji uneti niz A dimenzije N deli na dva niza B i C. 
Niz B treba da sadrzi sve parne clanove, dok niz C treba da sadrzi sve neparne 
clanove niza A.
```python
#niz = [1,2,3,4,5,6,7,8,9,10]     #ako se ne unosi sa tastature
nizA = []
n = int(input("Unesi broj članova niza "))
for i in range(n):                # for i in range len(niz)) # ako niz nije unet sa tastature
    clan = int(input(f"Unesi A[{i}] = "))
    nizA.append(clan)
print(nizA)
nizB = []   #prazan niz B
nizC = []   # prazan niz C
for i in range(n):
    if nizA[i] % 2 == 0:        # ako je i-ti član niza deljiv sa 2
        nizB.append(nizA[i])    # dodaj ga u niz B  
    else:                       # u suprotnom
        nizC.append(nizA[i])    # dodaj ga u niz C
print(f"Niz B je {nizB}, a niz C je {nizC}.")
```
## Četvrti primer
Napisati program koji u unetom nizu A dimenzije N sve 
negativne clanove niza zamenjuje nulom.
```python
n = int(input("Unesi broj članova niza "))
nizA = []
for i in range(0,n):
    clan = int(input(f"Unesi A[{i}] = "))
    nizA.append(clan)
print(nizA)
for i in range(0,n):
    if nizA[i] < 0:        # ako je i-ti član niza manji od nule
        nizA[i] = 0        # dodeli mu vrednost 0
print(nizA)
```























