# Torke. Skupovi. Rečnici

## Torke

### Definicija torki

* način kreiranja torki

    ```python
    torka1 = (2, 3)
    torka2 = 1, 4, 5
    torka3 = tuple(['Racunarski alati', 'Matematika', 'Masinski materijali'])
    torka4 = (3, 7.6, True, 45, 'Student’)
    ```

* torke su veoma slične listama, osim što su neizmenjive (liste su izmenjive, torke su neizmenjive)
* jednom kada je kreirana njene vrednosti nije moguće promeniti
* naziv potiče od uređenih vrednosti – (2,3) uređeni par, (3,7,8) uređena trojka, (4,7,8,9) uređena četvorka, (3,6,0,1,2) uređena petorka (0,2,1,-9,4), uređena šestorka (2,3,7,9,11,2) uređena šestorka, .... **uređena n-torka ili samo torka**

### Karakteristike torki

* jednom kada su kreirane torke nije moguće izmeniti – dodati, obrisati ili izmeniti član ili celu torku
* na torke je moguće primeniti for petlje, pristupiti pojedinim članovima
* torke ređe koristimo i to najčešće kada želimo da sačuvamo vrednosti sa kojima radimo i da na njih primenimo samo pretragu po petljama

    ```python
    torka = (2, 4, 5)
    torka[1] = 10   # Error: tuples are immutable
    ```

* način izmene vrednosti u torkama – nije praktično

    ```python
    predmeti_torka = ('Racunarski alati', 'Matematika', 'Masinski materijali', 'Engleski jezik', 'Mehanika')
    predmeti_lista = list(predmeti)
    predmeti_lista[0] = 'Mehanika 1'
    predmeti_torka = tuple(predmeti_lista)
    ```

## Skupovi

### Rad sa skupovima

* skupovi su kolekcije podataka u kojima se vrednosti čuvaju u neuređenom rasporedu
* skupovi ne mogu sadržati ponovljene vrednosti (duplikate)
kreiranje skupova

    ```python
    predmeti = {'Matematika1', 'Mehanika1', 'Racunarski alati', 'Materijali'}
    predmeti = set(['Matematika1', 'Mehanika1', 'Racunarski alati', 'Materijali'])
    ```

* ukoliko koristimo funkciju print() rezultat štampanja biće skup – raspored elemenata će biti slučajan – neuređenost skupova

    ```python
    print(predmeti)
    ```

* za razliku od lista i torki glavna namena je provera da li neki element pripada ili ne pripada skupu vrednosti
* skupove je najoptimalniije koristiti kod uklanjanja ponovljenih vrednosti

    ```python
    brojevi = [0, 2, 5, 7 ,9, 1, 4, 6, 7, 2, 4, -3, 66, 2, 8 , 3, 3, 4, 1, 11, -4, 5, 33, 0]
    brojevi_bez_duplikata = set(brojevi)
    print(brojevi)
    print(brojevi_bez_duplikata)
    ```

* skupovi su optimizovani za rad sa ključnom rečju in – za pretragu pripadnosti elementa skupu

    ```python
    for broj in range(30):
        print(broj in brojevi_bez_duplikata)

    predmeti = {'Matematika1', 'Mehanika1', 'Racunarski alati', 'Materijali'}

    print('Engleski' in predmeti)
    print('Matematika1' in predmeti)
    print('Materijali' in predmeti)
    ```

### Metode za rad sa skupovima

* metoda union() – unija dva skupa sadrži sve elemente sadržane u svako od skupova (ili u oba skupa):

    ```python
    A = {1, 2, 3}
    B = {2, 4}
    AUB = A.union(B)
    print(AUB)
    ```

* metoda intersection() – presek dva skupa, sadrži elemente koji se nalaze u oba skupa:

    ```python
    APB = A.intersection(B)
    print(APB)
    ```

* metoda difference() – sadrži elemente koje sadrži skup A a ne sadrži skup B

    ```python
    ARB = A.difference(B)
    print(ARB)
    BRA = B.difference(A)
    print(BRA)
    ```

## Rečnici

### Rad sa rečnicima

* rečnici su kolekcije podataka koji čuva elemente kao parove ključ-vrednost
kreiranje rečnika

    ```python
    recnik = {kljuc1: vrednost1, kljuc2: vrednost2, ... }
    ```

    ```python
    recnik = dict(kluc1=vrednost1, kljuc2=vrednost2, ...)
    ```

* ključevi mogu biti samo tipovi podataka koji su neizmenjvi – niske, celobrojne i torke, dok vrednosti mogu biti svi tipovi podataka

    ```python
    student = {'ime' : 'Milan', 'godine': 22, 'predmeti' : ['Matematika1', 'Racunarski alati']}
    ```  

* celobrojna kao ključ

    ```python
        student2 = {1 : 'Milica', 2 : 21, 3 : ['Matematika',  'Racunarski alati', 'Engleski']}

    print(student2[1])
    print(student2[3])
    ```

* pristupanje članovima rečnika

    ```python
    ime_studenta = student['ime']
    print(ime_studenta)
    predmeti_koje_slusa = student['predmeti']
    print(predmeti_koje_slusa)
    broj_bodova = student['broj_bodova']   # greska - Key error, ne postoji taj ključ
    ```

    bolje je članovima rečnika pristupiti metodom .get():

    ```python
    telefon = student.get('telefon')
    print(telefon)
    ```

    dodatno je moguce proslediti poruku koja se ispisuje ako nema ključa u recniku:

    ```python
    telefon = student.get('telefon', 'Nema trazenog kljuca u recniku')
    print(telefon)
    ```

* izmena članova rečnika

    ```python
    student1 = {'ime' : 'Milan', 'godine': 22, 'predmeti' : ['Matematika1', 'Racunarski alati']}
    student2 = {1 : 'Milica', 2 : 21, 3 : ['Matematika', 'Racunarski alati', 'Engleski jezik']}
    student1['ime'] = 'Aleksandar'
    student2[2] = 20
    ```

* dodavanje članova rečnika

    ```python
    student1['budzet'] = True
    print(student1)
    ```

* brisanje članova rečnika

    ```python
    del(student1['godine'])
    print(student1)
    ```

### Kjučevi i vrednosti

* funkcija len() vraća broj ključeva u rečniku

    ```python
    student1 = {'ime' : 'Milan', 'godine': 22, 'predmeti' : ['Matematika1', 'Racunarski alati']}
    print(len(student1))
    ```

* metode keys() I values() vraćaju ključeve i vrednosti:

    ```python
    koordinate_tacaka = {'A' : (2, 4, 6), 'B' : (2, -6, 1), 'C' : (5, 0, 8), 'D' : (4, 4, 1)}
    print(koordinate_tacaka.keys())
    print(koordinate_tacaka.values())
    ```

* metoda items() vraća uređene parove (ključ, vrednost)

    ```python
    print(koordinate_tacaka.items())
    ```

### For petlje i rečnici

* ako koristimo for petlju sa rečnicima dobijamo ključeve:

    ```python
    student1 = {'ime' : 'Milan', 'godine': 22, 'predmeti' : ['Matematika1', 'Racunarski alati']}
    for kljuc in student1:
        print(kljuc)
    ```

* ako želimo parove ključ-vrednost kroz for petlju, koristimo metodu items():

    ```python
    for kljuc, vrednost in student1.items():
        #print(kljuc, vrednost)
        print(f'{kljuc} = {vrednost}')
    ```

### Rečnici i drugi tipovi podataka

* rečnici i torke

    ```python
    koordinate_tacaka = {'A' : (2, 4, 6), 'B' : (2, -6, 1), 'C' : (5, 0, 8),  'D' : (4, 4, 1)}
    print(koordinate_tacaka)
    ```

* rečnici i liste

    ```python
    student1 = {'ime' : 'Milan', 'godine': 22, 'predmeti' : ['Matematika1', 'Racunarski alati']}
    student2 = {'ime' : 'Ana', 'godine': 20, 'predmeti' : ['Mehanika1', 'Racunarski alati']}
    student3 = {'ime' : 'Filip', 'godine': 21, 'predmeti' : ['Matematika1', 'Engleski']} 
    lista_studenata = [student1, student2, student3] 
    print(lista_studenata)
    ```

### Kreiranje praznih kolekcija

* prazna lista

    ```python
    prazna_lista1 = []
    prazna_lista2 = list()
    print(prazna_lista1)
    print(prazna_lista2)
    ```

* prazne torke

    ```python
    prazna_torka1 = ()
    prazna_torka2 = ()
    print(prazna_torka1)
    print(prazna_torka2)
    ```

* prazni skupovi

    ```python
    prazan_skup1 = {}       # greska, ovo je prazan recnik
    prazan_skup2 = set()
    print(prazan_skup1)     # greska, ovo je prazan recnik
    print(prazan_skup2)
    ```
