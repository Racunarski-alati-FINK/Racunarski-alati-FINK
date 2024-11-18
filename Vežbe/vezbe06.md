# Vežbanje
## Prvi primer
Izračunaj zbir cifara unetog trocifrenog broja:

```python
n = int(input("Unesi najviše trocifreni broj "))                                 # unošenje broja sa tastature i pretvaranje unete vrednosti u celobrojnu - int
if len(str(broj)) <= 3:                                                          # provera da li broj ima tri cifre ili manje - pretvaramo u str jer len() ne može nad int
#if n < 999:                                                                     # ako želimo da izbegnemo len()  
    jedinice = broj % 10                                                         # ostatak pri deljenju unetog broja sa 10 je cifra jedinica, npr 123 % 10 = 12 (ostatak je 3)
    desetice = broj % 100 // 10                                                  # prvo odredimo ostatak pri deljenju unetog broja brojem 100 (123 % 100 = 23) ž
                                                                                 # a onda ostatak celobrojno podelimo sa 10 (23 // 10 = 2 (ostatak 3)) - dobijemo cifru desetica
    stotine = broj // 100                                                        # celobrojno deljenje unetog broja sa 100 je cifra stotina, npr 123 // 100 = 1 (ostatak je 23)
    print(f"Stotine: {stotine}, desetice: {desetice}, jedinice: {jedinice}")     # štampanje pojedinačnih cifara
    zbir = jedinice + desetice + stotine                                         # izračunavanje zbira cifara
    print(f"Zbir cifara broja {broj} je {zbir}.")                                # štampanje zbira cifara
else:
    print("Broj je veći od trocifrenog!")                                        # ako uslov nije ispunjen da broj ima najviše tri cifre, ispisuje se poruka
```

Ako želimo da uradimo isti zadatak bez ograničenja u broju cifara, koristićemo WHILE petlju

```python
zbir = 0
broj = int(input("Unesi broj "))
polazna = broj                                    # čuvanje polazne vrednosti broja
while broj > 0:                                   # ciklus se ponavlja sve do poslednje cifre broja
    cifra = broj % 10                             # određujemo cifru jedinica broja  primer: 123456 ---> 6
    zbir += cifra                                 # dodaje tu cifru na zbir; isto kao zbir = zbir + cifra
    broj = broj // 10                             # uklanjanje poslednje cifre iz broja  primer:  123456 // 10 = 12345
print(f"Zbir cifara unetog broja {polazna} je {zbir}")

```
A možemo i posmatranjem unosa kao da je string:

```python
zbir = 0
broj = input("Unesi broj ")                       # input() funkcija podrazumeva da je unos tipa string
for cifra in broj:                                # petlja ide po svakom elementu broja
    zbir += int(cifra)                            # dodaje cifru, kao celobrojnu vrednost, na zbir; isto kao zbir = zbir + cifra
    
print(f"Zbir cifara unetog broja {broj} je {zbir}")
```


## Drugi primer
Proveriti da li je uneti TROCIFRENI broj Armstrongov.  
Broj je Armstrongov ako je zbir kubova njegovih cifara jednak samom broju 
    
    primer: 1³ + 5³ + 3³ = 153

```python
broj = int(input("Unesi najviše trocifreni broj n = "))        # unošenje broja sa tastature
if len(str(n)) <= 3:                                           # provera od koliko se cifara broj sastoji
    jedinice = broj % 10
    desetice = broj % 100 // 10
    stotine = broj // 100
    if jedinice ** 3 + desetice ** 3 + stotine ** 3 == n:      # provera da li je zbir kubova cifara jednak broju
        print(f"Broj {broj} jeste Armstrongov")                # ispis ako je uslov ispunjen   
    else:
        print(f"Broj {broj} nije Armstrongov")                 # ispis ako uslov nije ispunjen
else:
    print("Broj je veći od trocifrenog!")                      #ispis ako je unet broj veći od trocifrenog
```

Analogno prethodnom zadatku, rešenje ovog zadatka korišćenjem WHILE petlje:

```python
zbir = 0
broj = int(input("Unesi broj "))
polazna = broj                                    # čuvanje polazne vrednosti broja                                          
while broj > 0:                                   # ciklus se ponavlja sve do poslednje cifre broja
    cifra = broj % 10                             # određujemo cifru jedinica broja  primer: 123456 ---> 6
    zbir += cifra**3                              # dodaje kub te cifre na zbir; isto kao zbir = zbir + cifra ** 3
    broj = broj // 10                             # uklanjanje poslednje cifre iz broja  primer:  123456 // 10 = 12345
if zbir == polazna:
    print(f"Broj {polazna} jeste Armstrongov broj.")
else:
    print(f"Broj {polazna} nije Armstrongov broj.")

```

## Treći primer
Unetoj niski prebrojati samoglasnike

```python
niska = input("Unesi nisku: ")
samoglasnici = 0
for slovo in niska:
    if slovo in "aeiouAEIOU":
        samoglasnici = samoglasnici + 1
print(f"Niska {niska} se sastoji od {samoglasnici} samoglasnika.")
```
Ako bismo prebrojavali i suglasnike:

```python
niska = input("Unesi nisku: ")
samoglasnici = 0
suglasnici = 0
for slovo in niska:
    if slovo in "aeiouAEIOU":
        samoglasnici = samoglasnici + 1
    else:
        suglasnici = suglasnici + 1
print(f"Niska {niska} se sastoji od {samoglasnici} samoglasnika i {suglasnici} suglasnika.")
```

ovako urađen zadatak računa i razmake, brojeve i specijalne karaktere kao suglasnike, ako prebrojavamo samo slova, koristimo metodu [isalfa()](https://www.w3schools.com/python/ref_string_isalpha.asp)

```python
niska = input("Unesi nisku: ")
samoglasnici = 0
suglasnici = 0
for slovo in niska:
    if slovo in "aeiouAEIOU":
        samoglasnici = samoglasnici + 1
    elif slovo.isalfa():
        suglasnici = suglasnici + 1
print(f"Niska {niska} se sastoji od {samoglasnici} samoglasnika i {suglasnici} suglasnika.")
```

## Četvrti primer
Za unetu reč odrediti da li je palindrom - reči koje se i sa desna i sa leva čitaju na isti način (potop, melem)

```python
rec = input("Uneti reč: ")
rec = rec.lower()                           # metoda koja pretvara sva slova niske u mala; pogledajte više na: https://www.w3schools.com/python/python_strings_methods.asp
if rec == rec[::-1]:                        # rec[::-1] ispisuje rec od prvog do poslednjeg slova korakom -1, odnosno u nazad 
    print(f"{rec} jeste palindrom")
else:
    print(f"{rec} nije palindrom")
```

Ako bismo proveravali da li je uneta rečenica palindrom, morali bismo da uklonimo razmake. To možemo da uradimo primenom metode [replace(" ","")](
https://www.w3schools.com/python/ref_string_replace.asp):


```python
recenica = input("Uneti reč: ")
recenica = recenica.lower()
recenica = recenica.replace(" ","")                          
if recenica == recenica[::-1]:                        
    print(f"Rečenica {recenica} jeste palindrom")
else:
    print(f"Rečenica {recenica} nije palindrom")
```


## Peti primer
Za unete dve reči odrediti da li su anagrami - reči koje se sastoje od istog broja istih slova (ortoped - torpedo)

```python
rec1 = input("Uneti prvu reč: " )
rec2 = input("Uneti drugu reč: ")
if sorted(rec1) == sorted(rec2):                            # sortira slova unutar reči po abecednom redu i proverava da li su tako sortirane reči jednake, što znači da su anagrami
    print(f"Reči {rec1} i {rec2} jesu anagrami")
else:
    print(f"Reči {rec1} i {rec2} nisu anagrami")
```

primer:

```python
    >>> print(sorted("ortoped")
        ['d', 'e', 'o', 'o', 'p', 'r', 't']
    >>> print(sorted("torpedo"))
        ['d', 'e', 'o', 'o', 'p', 'r', 't']
# pošto su dobijene liste jednake, reči jesu anagrami 

    >>> print(sorted("ortoped"))
        ['d', 'e', 'o', 'o', 'p', 'r', 't']
    >>> print(sorted("pedijatar"))
        ['a', 'a', 'd', 'e', 'i', 'j', 'p', 'r', 't']
# dobijene liste nisu jednake, reči nisu anagrami

```

## Šesti primer
Za unetu rečenicu štampati početno slovo svake reči

```python
recenica = input("Unesi rečenicu: ")
print(recenica[0])                                          # štampanje prvog slova rečenice
for i in range(0,len(recenica)):                            # petlja po indeksima rečenice
    if recenica[i] == " ":                                  # ako je element rečenice sa indeksom "i" jednak razmaku                                 
        print(recenica[i+1])                                # onda štampati sledeći karakter [i+1], jer prvo slovo reči obavezno sledi iza razmaka
```
