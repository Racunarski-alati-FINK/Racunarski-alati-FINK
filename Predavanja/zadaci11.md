# Zadaci za vežbanje

## Primer 1

Loptica je bačena vertikalno naviše u vazduh sa visine $h_0$ početnom brzinom $v_0$. Visina na koju stiže loptica i brzina
na toj visini dati su formulama:
$$h = h_0 + v_0t - \frac{1}{2}gt^2$$
$$v = v0 - gt$$

Napisati funkciju koja uzima početnu visinu $h_0$, početnu brzinu $v_0$ i vreme kao niz 10 vrednosti od 0 do 10. Funkcija vraća korisniku jednu od dve poruke:

- loptica je pala na pod
- loptica nije pala na pod

```python
h0 = float(input('Unesi h0: '))
v0 = float(input('Unesi v0: '))
g = 9.81
vreme = [t for t in range(0, 10, 0.1)]
print(vreme)
visina = []
trenutak = []

for t in vreme:
     h = h0 + v0*t - 0.5*g*t**2
     if h > 0:
         visina.append(h)
         trenutak.append(t)

import matplotlib.pyplot as plt
plt.plot(trenutak, visina)
plt.show()
```

## Primer 2

Napisati funkciju koja uzima jedan ceo prirodan broj i štampa sve njegove delioce u neuređenom rasporedu.
Primer:

$$ 8 = 2 * 2 * 2$$
$$ 9 = 3 * 3 $$
$$ 7 = 7 $$
$$ 120 = 2 * 2 * 2 * 3 * 5 $$

```python
def faktorizacija(broj):
    k = 2
    while broj > 1:
        while broj % k != 0:
            k = k + 1
        print(k)
        broj = broj // k
```

## Primer 3

Napisati funkciju koja na ekranu crta figuru. Funkcija uzima ceo broj - dužinu stranice kvadrata i karakter kojim će biti iscrtan kvadrat.
Napomena: kreirati funkciju sa podrazumevanim parametrima a = 10 i oznaka = '-'.

```python
def nacrtaj_kvadrat(stranica=10, oznaka='-'):
    for i in range(1, stranica+1):
        if ((i == 1) or (i==stranica)):
            print(stranica*oznaka)
        else:
            print(f'{oznaka}{" " * (stranica-2)}{oznaka}' )

nacrtaj_kvadrat(7, 'x')
nacrtaj_kvadrat(3, 'o')
nacrtaj_kvadrat(10, '-')
nacrtaj_kvadrat(5, '#')
nacrtaj_kvadrat(6, '@')
nacrtaj_kvadrat()
```

## Primer 4

Napisati funkciju koja uzima listu koeficijenata polinoma $a$ i decimalni broj $x$. Funkcija računa vrednost polinoma:

$$p(x)=a_0 + a_1 \cdot x + a_2 \cdot x^2 + \ldots + a_n \cdot x^n$$    

```python
def polinom(koeficijenti, x):
    p = 0.0
    for i in range(0, len(koeficijenti)):
        p += koeficijenti[i]*x**i
    print(f'Vrednost polinoma za dato x je {p}')

polinom([1, 2, 3, 4], 2)
```

## Primer 5

Napisati funkciju koja uzima ceo prirodan broj i proverava da li je broj Hemingov broj. Prirodan broj je Hemingov ako su jedini njegovi prosti činioci 2, 3 ili 5.

$$ 8 = 2 \cdot 2 \cdot 2  -> jeste $$

$$ 9 = 3 \cdot 3  -> jeste $$

$$ 105 = 3 \cdot 5 \cdot 7  -> nije $$  

```python
 def hemingov_broj(broj):
    n = broj
    while(broj%2 == 0):
        broj = broj // 2
        print(broj)
    while (broj % 3 == 0):
        broj = broj // 3
    while (broj % 5 == 0):
        broj = broj // 5
   
    if broj != 1:
        print(f'{n} nije Hemingov broj.')
    else:
        print(f'Broj {n} jeste Hemingov broj.')

hemingov_broj(24)
hemingov_broj(105)
hemingov_broj(125)
hemingov_broj(63)
hemingov_broj(45)
```

## Primer 6

Napisati funkciju koja za 2 prosleđena cela broja a i b računa sumu i proizvod svih brojeva izmedju a i b isključujući te brojeve.

```python
def funkcija(a, b):
    suma = 0
    proizvod = 1
    for i in range(min(a, b), max(a, b)):
        if i != 0:
            suma += i
            proizvod *= i

    print(f'Suma prirodnih brojeva između brojeva {a} i {b} je {suma}.')
    print(f'Proizvod svih brojeva između brojeva {a} i {b} je {proizvod}')
    

funkcija(2, -5)
funkcija(2, 5)
funkcija(4, -2)
funkcija(-2, 3)
```

## Primer 7

Napisati program koji za uneti prirodni broj računa sumu i proizvod svih prirodnih brojeva koju su manji od ili jednaki unetom broju.

```python
def suma_svih_do(n):
    suma = 0
    proizvod = 1
    if n > 0:
        for i in range(1, n):
            suma += i
            proizvod *= i
    else:
        for i in range(-1, n, -1):
            print(i)
            suma += i
            proizvod *= i
            
    print(f'Suma prirodnih brojeva do broja {n} je {suma}.')
    print(f'Proizvod svih brojeva do broja {n} je {proizvod}')

suma_svih_do(11)
suma_svih_do(7)
suma_svih_do(5)
suma_svih_do(-4)
```

## Primer 8

Napisati funkciju koja uzima dva decimalna broja i tabelarno prikazuje vrednost funkcije $y = asin(x) + bcos(x)$ za vrednosti $x = 0.1, 0.2,...$ Prikaz obustaviti kada se dogodi da dve susedne vrednosti y imaju suprotne predznake.

```python
import math

def tabelarna_funkcija(a, b):
    x = 0.0
    y = 0.0

    y_pre = a*math.sin(x) + b*math.cos(x)
    while (y * y_pre >= 0):
        y_pre = y
        x += 0.1
        y = a*math.sin(x) + b*math.cos(x)
        if (y_pre * y >= 0):
            print(f'{x:.3f} {y:.3f}')
        else:
            break

tabelarna_funkcija(0.3, -4)
```

## Primer 9

Napisati funkciju koja uzima dva decimalna broja i tabelarno prikazuje vrednost funkcije $y = -a*x^3 + bx^2 + 2$ sve dok je vrednost funkcije veća od nule. Vrednost $x$ se menja sa korakom 0.1 u svakoj iteraciji $x = 0.1, 0.2,...$

```python
def tabelarna_funkcija(a, b):
    x = 0.0
    y = 0.0

    while (y >= 0.0):
        y = -a*x**3 + b*x**2 + 2    
        if y < 0:
            break
        else:
            print(f'{x:.2f} {y:.2f}')
            x += 0.1

tabelarna_funkcija(3, 5)
tabelarna_funkcija(2, 1)
tabelarna_funkcija(5, 6)
```

## Primer 10

Napisati program koji simulira rad jednostavnog kalkulatora, koji će za dva uneta decimalna broja i jedan operator (string) dati vrednost izvršene operacije.

```python
 def kalkulator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return 'Nije operator'
    
glavni program
kalkulator(3.4, 6.7, '+')
kalkulator(4.1, -1, '-')
kalkulator(6.5, -2, '*')
kalkulator(1.2, 0.2, '/')
kalkulator(3, 8, 'plus')
```
