# Vežbanje sa funkcijama
## Prvi primer
Napisati funkciju koja vrši sumiranje niza bez vraćanja vrednosti - vrednost se štampa unutar funkcije

```python
def sumiranje(niz):
    """Funkcija koja računa sumu niza"""
    suma = 0                                        # početna vrednost sume je nula
    for clan in niz:                                # petlja po članovima niza x
        suma += clan                                # isto kao i suma = suma + clan
    """
    for i in range(len(niz)):                       # isti i rezultat ali petlja po indeksima 
        suma += niz[i]
    """
    print("Suma niza {} je {}.".format(niz,suma))   # ako pozivamo funkciju, bez return, štampamo rezultat u funkciji
# glavni program:
sumiranje([1,2,3,4,5,6])                            # pozivanje bez return
```
## Drugi primer
Napisati funkciju koja sumira prosleđeni niz, a rezultat vraća glavnom programu

```python
def sumiranje(niz):
    """Funkcija koja računa sumu niza"""
    suma = 0                                        # početna vrednost sume je nula
    for clan in niz:                                # petlja po članovima niza x
        suma += clan                                # isto kao i suma = suma + clan
    """
    for i in range(len(niz)):                       # isti i rezultat ali petlja po indeksima 
        suma += niz[i]
    """
    return suma
#glavni program:
print(sumiranje([5,6,7,8,9,10]))                    # pozivanje ako koristimo return
```

## Treći primer
Funkcija koja korisniku omogućava da unese niz sa tastature

```python
def unesi_niz():
    """ Funkcija za unošenje niza sa tastature """
    n = int(input("Uneti broj članova niza n = "))   # broj članova niza mora biti ceo broj - integer
    niz = []                                         # formiramo praznu listu
    for i in range(n):                               # petlja za unošenje članova
        niz.append(float(input(f"Uneti a[{i}] = "))) # dodavanje elementa (float) na kraj petlje sa tastature
    print(f"Uneli ste niz {niz}.")
    return niz
# glavni program:
a = unesi_niz()                                    # pozivanje funkcije i unošenje niza a
```
Ukoliko hoćemo uneti niz da sumiramo prethodnom funkcijom za sumiranje to radimo na sledeći način:

```python
print(sumiranje(a))                                # sabiranje niza unetog funkcijom unesi_niz()
```

## Četvrti primer
Funkcija koja korisniku omogućava da unese matricu sa tastature

```python
def unesi_matricu():
    """ Funkcija za unošenje matrice sa tastature """
    n = int(input("Uneti broj vrsta matrice n = "))
    m = int(input("Uneti broj kolona matrice m = "))
    matrica = []                                     # prazna matrica
    for i in range(n):                               # petlja po vrstama matrice
        red = []                                     # prazan red
        for j in range(m):                           # petlja po kolonama matrice
            red.append(int(input(f"Uneti član matrice A[{i}][{j}] = "))) # unošenje članova u vrstu
        matrica.append(red)                         # unošenje vrste u matricu
    print("Uneli ste matricu: ")
    for red in matrica: print(red)                  # štampanje matrice vrsta po vrsta
#glavni program:
A = unesi_matricu()                                # pozivanje funkcije i unošenje matrice A
```

## Peti primer
Funkcija koja korisniku omogućava da prebroji parne članove niza. Glavnom programu vraća broj izbrojanih članova.

```python
def prebroj_parne(niz):
    """Funkcija koja broji parne članove niza"""
    brojac = 0
    for i in range(len(niz)):
        if niz[i] % 2 == 0:
            brojac += 1                                 #isto kao brojac = brojac + 1
    return brojac
```
Ukoliko hoćemo niz da unesemo sa tastature, pozivamo funkciju unesi_niz()

```python
A = unesi_niz()
```
A onda pozivamo funkciju prebroj_parne(A)

```python
print("Broj parnih članova unetog niza je: ", prebroj_parne(A))
```
Takođe, možemo funkciju da pozovemo i bez unošenja niza sa tasature, direktnim definisanjem niza kao argumenta funkcije:

```python
print(prebroj_parne([1,2,3,4,5,6,7,8,9,10]))
```
## Šesti primer
Funkcija koja u celobrojnom nizu proizvoljne duzine neparnim brojevima dodeljuje vrednost 0 (nula). Glavnom programu vraća procenat od ukupnog broja članova
koji je različit od nule.

```python
def unuli_neparne(niz):
    """ Funkcija koja pretvara sve neparne članove niza u 0 i vraća procenat
    nepromenjenih """ 
    brojac = 0
    print("Niz pre izmena ", niz)
    for i in range(len(niz)):
        if niz[i] % 2 != 0:                      # ako je ostatak pri deljenju člana niza različit od 0 - znači neparan
            niz[i] = 0                           # pretvori ga u nulu
            brojac += 1                          # uvećaj brojač za 1
    print("Niz nakon izmena ", niz)
    return str((len(niz)-brojac)/len(niz)*100) + " %"        # procenat preostalih
#glavni program:
print(unuli_neparne([1,2,3,4,5,6]))
```

## Sedmi primer
Funkcija izračunava srednju vrednost niza. Glavnom programu vraća dobijenu srednju vrednost:

```python
def srednja_vrednost_niza(niz):
    """Funkcija za izračunavanje srednje vrednsoti niza"""
    brojac = 0
    suma = 0
    for clan in niz:
        suma += clan
        brojac += 1
    return suma/brojac
```
### Osmi primer
Funkcija koja vrednostima niza koje su manje od srednje vrednosti dodeljuje vrednost nula.     
_Napomena: funkcija podrazumeva izračunavanje srednje vrednosti funkcijom iz prethodnog primera_

```python
def unuli_manje_od_srvr(niz):
    """Funkcija koja članovima niza manjim od srednje vrednosti niza dodeljuje vrednost nula
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    NE FUNKCIONIŠE BEZ PRETHODNE srednja_vrednost_niza() FUNKCIJE
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    print("Unet niz je ", niz)
    print("Srednja vrednost niza je ", srednja_vrednost_niza(niz)) # oslanja se na prethodnu srednja_vrednost_niza() funkciju
    for i in range(len(niz)):
        if niz[i] < srednja_vrednost_niza(niz):
            niz[i] = 0
    return niz
#glavni program
print(unuli_manje_od_srvr([1,2,3,4,5,6]))
```
## Deveti primer
Funkcija koja preuzima matricu i transponuje je, a glavnom programu vraća transponovanu matricu.

```python
def transponuj_matricu(matrica):
    """Funkcija koja transponuje datu matricu dimenzije nxm"""
    print("Matrica za transponovanje: ")
    for red in matrica: print(red)
    n = len(matrica)                                # broj vrsta polazne matrice
    m = len(matrica[0])                             # broj kolona polazne matrice
    transponovana = [[0]*n for i in range(m)]       # definisanje nula matrice dimenzije transponovane matrice
    for i in range(m):                              # petlja po vrstama transponovane matrice
        for j in range(n):                          # petlja po kolonama transponovane matrice
            transponovana[i][j] = matrica[j][i]     # transponovanje matrice
    print("Transponovana matrica je: ")
    return transponovana
#glavni program
A = [[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
AT = transponuj_matricu(A)
for red in AT: print(red) # štampanje transponovane matrice red po red
```

## Deseti primer
Funkcija koja pronalazi maksimalni član matrice i prosleđuje ga glavnom programu

```python
def maksimum_matrice(matrica):
    maksimum = matrica[0][0]                             # pretpostavka da je element A[0][0] maksimalan
    for i in range(len(matrica)):                        # petlja po vrstama matrice
        for j in range(len(matrica[0])):                 # petlja po kolonama matrice
            if matrica[i][j] > maksimum:                 # ako je neki član veći od pretpostavljenog maksimuma
                maksimum = matrica[i][j]                 # novi maksimum postaje taj član
    print("Maksimum matrice je: ")
    return maksimum
#glavni program:
print(maksimum_matrice(A))
```

## Jedanaesti primer
Funkcija vraća vrednost  $({{X}_1 + {X}_2 + {X}_3 + ... + {X}}_m)$- $({{Y}_1 \cdot {Y}_2 \cdot {Y}_3 \cdot  \ldots  \cdot {Y}}_m$)
    gde su X i Y članovi neparnih odnosno parnih kolona matrice koja se preuzima iz glavnog programa
    
primer matrice:
    
   | X1 Y1 X4 Y4 X7 |   
   | X2 Y2 X5 Y5 X8 |   
   | X3 Y3 X6 Y6 X9 |   

   rezultat = (X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 + X9) - (Y1 * Y2 * Y3 * Y4 * Y5 * Y6)

```python
def sumaX_proizvodY(matrica):
    """
    Funkcija vraća vrednsot (X1 + X2 + X3 + ... + Xm) - (Y1 * Y2 * Y3 * ... * Ym)
    gde su X i Y članovi neparnih odnosno parnih kolona matrice koja se preuzima iz glavnog programa
    
    primer matrice:
   | X1 Y1 X4 Y4 X7 |
   | X2 Y2 X5 Y5 X8 |
   | X3 Y3 X6 Y6 X9 |

   rezultat = (X1+X2+X3+X4+X5+X6+X7+X8+X9) - (Y1*Y2*Y3*Y4*Y5*Y6)
    """
    sumaX = 0
    proizvodY = 1 
    for i in range(len(matrica)):
        for j in range(len(matrica[0])):
            if j % 2 == 0:
                sumaX += matrica[i][j]
            else:
                proizvodY *= matrica[i][j]
    return sumaX - proizvodY
# glavni program:
print(sumaX_proizvodY([[1,2,3],[1,2,3]]))
```

