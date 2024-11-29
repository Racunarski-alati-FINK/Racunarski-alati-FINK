# Vežbanje
## Prvi primer
Naći vrednost polinoma x² + 2x³ + 3x⁴ + ... + 9x¹⁰ za uneto x.
```python
x = int(input("Unesi broj x = "))
vrednost = 0
for i in range(1,10):
    vrednost = vrednost + i * x ** (i+1)
print(f"Rešenje polinoma za uneto {x} je {vrednost}.")
```
## Drugi primer
Naći vrednost polinoma 4x² + 6x³ + 8x⁴ + ... + 20x¹⁰ za uneto x.
```python
x = int(input("Unesi broj x = "))
polinom = 0
for i in range(4,21,2):
    polinom = polinom + i * x ** (i/2)
print(f"Vrednsot polinoma za uneto {x} je {polinom}.")
```
ili:
```python
polinom = 0
for i in range(2,11):
    polinom = polinom + 2*i * x ** (i)
print(f"Vrednost polinoma za x = {x} je {polinom}")
```
ili:
```python
x = int(input("Unesi broj x = "))
polinom = 0
koeficijent = 4
stepen = 2
for i in range(9):
    polinom = polinom + koeficijent * x ** stepen
    koeficijent += 2
    stepen += 1
print(f"Vrednost polinoma za uneto {x} je {polinom}.")
```
## Treći primer
Napisati program koji u unetom nizu A dimenzije n sve negativne clanove niza zamenjuje nulom.
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
## Četvrti primer
Napisati program koji uneti niz A dimenzije n deli na dva niza B i C. 
Niz B treba da sadrži sve parne članove niza A, dok niz C treba da sadrži sve neparne 
članove niza A.
```python
#nizA = [1,2,3,4,5,6,7,8,9,10]     #ako se ne unosi sa tastature
nizA = []
n = int(input("Unesi broj članova niza "))
for i in range(n):
# for i in range len(nizA)) # ako niz nije unet sa tastature
    clan = int(input(f"Unesi A[{i}] = "))
    nizA.append(clan)
print(nizA)
nizB = []   #prazan niz B
nizC = []   # prazan niz C
for i in range(n):
# for i in range len(nizA)) # ako niz nije unet sa tastature
    if nizA[i] % 2 == 0:        # ako je i-ti član niza deljiv sa 2
        nizB.append(nizA[i])    # dodaj ga u niz B  
    else:                       # u suprotnom
        nizC.append(nizA[i])    # dodaj ga u niz C
print(f"Niz B je {nizB}, a niz C je {nizC}.")
```
## Peti primer
Napisati program koji unetoj reči zamenjuje velika i mala slova engleske abecede (AcA = aCa).
```python
rec = input("Unesite reč ")
nova_rec = ""                                    # deklarisanje promenljive kao prazna niska
for slovo in rec:
    if slovo >="a" and slovo <="z":              # ukoliko se slovo nalazi u opsegu malih slova
        nova_rec = nova_rec + slovo.upper()      # prebaci ga u veliko, metodom upper()
    elif slovo >="A" and slovo <= "Z":           # ukoliko se slovo nalazi u opsegu velikih slova
        nova_rec = nova_rec + slovo.lower()      # prebaci ga u malo, metodom lower()
    else:
        nova_rec = nova_rec + slovo              # sve što nije slovo se prepisuje
print(f"Vaša reč {rec}, nakon zamene velikih i maloh slova je {nova_rec}")
```
## Šesti primer
Napisati program koji za unetu rečenicu izdvaja reč najveće dužine.
```python
recenica = input("Unesi rečenicu ")
najduza_rec = recenica[0]                 # pretpostavljamo da je najduža reč prvo slovo
rec = ""                                  # deklarišemo privremenu promenljivu "reč" kao praznu nisku
for slovo in recenica:                    # za svako slovo u rečenici
    if slovo != " ":                      # ukoliko je slovo različito od razmaka
        rec = rec + slovo                 # dodaj ga u privremenu promenljivu "reč"
        if len(rec) > len(najduza_rec):   # ako je dužina trenutne reči duža od trenutno najduže reči
            najduza_rec = rec             # nova najduza_rec postaje ta reč
    else:
        rec = ""                          # ukoliko se slovo ne razlikuje od razmaka, resetuj promenljivu reč u praznu nisku
print(f"U unetoj rečenici '{recenica}', najduža reč je '{najduza_rec}'")
```
