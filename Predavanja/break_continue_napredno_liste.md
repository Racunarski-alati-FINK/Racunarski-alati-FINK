# Break. Continue. Napredni rad sa listama

## Break i continue

Naredbe break i continue imaju različite uloge:

* pri pozivu naredbe break u okviru tela petlje dolazi do napuštanja čitave petlje – petlja se prekida

    ```python
    for x in niz:
        if x == 0:
            break
        else:
            print(f'x = {x}')
    ```

    ```python
    brojevi = [1, 3, 5, 8, 11, 34]
    neparan_broj = True
    i = 0
    while neparan_broj:
        if brojevi[i] % 2 != 0:
            print(brojevi[i])
        else:
            neparan_broj = False
        i = i + 1
    ```

    ```python
    brojevi = [1, 3, 5, 8, 11, 34]
    i = 0
    while i < len(brojevi):
        if brojevi[i] % 2 != 0:
            print(brojevi[i])
        else:
            break
        i = i + 1
    ```

* pri pozivu naredbe continue u okviru tela petlje dolazi do napuštanja tela petlje – petlja se ponovo izvršava

    ```python
    for x in niz:
        if x == 0:
            continue
        else:
            print(f'x = {x}')
    ```

    ```python
    brojevi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for broj in brojevi:
        if broj % 2 == 0:
            continue
        print(broj)

    for i in range(len(brojevi)):
        if brojevi[i] % 2 == 0:
            continue
        print(brojevi[i])
    ```

## Napredni rad sa listama

Napredno kreiranje listi moguće je na više načina:

* dodavanjem elemenata iz određenog opsega u listu

    ```python
    lista = [i for i in range(100)]
    ```

    isto kao i:

    ```python
    lista = []
    for i in range(100):
          lista.append(i)
    print(lista)
    ```

* dodavanjem elementa nakon izračunavanja u listu

    ```python
    dvostruki = [2*i for i in range(100)]
    ```

    isto kao i:

    ```python
    dvostruki = []
    for i in range(0, 100):
          dvostruki.append(2*i)  
    ```

* dodavanjem elementa iz opsega ili kolekcije prema nekom uslovu u listu

    ```python
    kvadrati_deljivih_sa_5 = [broj*broj for broj in range(0, 100) if broj % 5 == 0]
    ```

    isto kao i:

    ```python
    kvadrati_deljivih_sa_5 = []
    for broj in range(0, 100):
          if broj % 5 == 0:
                kvadrati_deljivih_sa_5.append(broj*broj)
    ```

* dodavanje elemenata iz postojeće liste prema nekom uslovu u listu ili unosom od strane korisnika

    ```python
    niz = [1, 6, 8, 3, 7, 12, 67, -3, 8, 90, 44, 2, 6, -87, 11, 90, 32, -66, 9]
    lista = [broj for broj in niz if broj % 9]
    ```

    ```python
    niz = [3, 6, 8, 1, 4, 8, 2, 7]
    kvadrati = []
    for x in niz:
        kvadrati.append(x*x)
    ```

    ```python
    niz = [3, 6, 8, 1, 4, 8, 2, 7]
    kvadrati = [x*x for x in niz]
    ```

    ```python
    lista_korisnik = [int(input("Dodaj ceo broj u listu: ")) for i in range(5)]
    print("Kreirana lista:", lista_korisnik)
    ```

* ugnežđeno dodavanje u listu

    ```python
    n = int(input("Unesi dimenzije matrice: "))
    matrica = []
    for i in range(n):
        red = []
        for j in range(n):
            clan = int(input("Unesi clan matrice: "))
            red.append(clan)
        matrica.append(red)
    for red in matrica:
        for kolona in red:
            print(kolona)
    for red in matrica:
        print(red)
    ```

    ```python
    n = int(input("Unesi broj redova i kolona matrice: "))
    matrica = [[int(input(f"Unesi clan matrice [{i}][{j}]")) for j in range(n)] for i in range(n)]
    ```

### for petlje i enumerate()

Ukoliko pri iterciji kroz listu želimo da dobijemo i indeks i vrednost člana koristimo funkciju enumerate():

```python
predmeti = ['Racunarski alati', 'Matematika', 'Masinski materijali', 'Engleski jezik', 'Mehanika’]

for predmet in predmeti:
    print(predmeti)

for redni_broj, predmet in enumerate(predmeti):
    print(redni_broj, predmet)
```

### Metode join() i split()

* za povezivanje elemenata liste koristimo metodu join()

    ```python
    predmeti = ['Racunarski alati', 'Matematika', 'Masinski materijali', 'Engleski jezik', 'Mehanika’]
    niska_predmeti = ', '.join(predmeti)
    print(niska_predmeti)
    ```

* za razdvajanje (podeli niske) koristimo metodu split()

    ```python
    niska_predmeti = ' - '.join(predmeti)
    print(niska_predmeti)
    nova_lista = niska_predmeti.split(' - ')
    print(nova_lista)
    ```
