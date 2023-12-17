## Zadatak
Meteorološka stanica Kragujevac je dala spisak meseca sa prosečnim temperaturama i
vlažnosti vazduha u toku meseca. Spiask je dat u obliku fajla [vreme.csv][vreme]. Svaka linija sadrži podatke o
mesecima i temperaturama, odnosno vlažnosti vazduha u sledećem formatu:

  mesec;temparatura;vlažnost

Napraviti program koji poziva funkciju i prosledjuje joj naziv csv fajla. Napisati funkciju koja:
1) uzima tekstualni fajl i otvara ga za citanje
2) kreira listu recnika meseci - meseci = {ime:ime, temperatura:temperatura, vlažnost: vlažnost}
3) kreira listu meseca koji su topliji od 15 stepeni
4) racuna prosečnu temperaturu svih meseci
5) upisuje mesece u fajl izlaz.txt koji su imali vlažnost vazduha manju od 70%

```python
def napravi_izvestaj(ime_fajla):
  meseci = [] # prazna lista za sve rečnike student
	topli = [] # prazna lista za sve rečnike mesec ako je temp >=15
	suma_temp = 0 # početna vrednost promenljive za sumiranje temperature
	notvlazni = []
	
	with open(ime_fajla, 'r') as fajl:
		for linija in fajl:
			ime, temperatura, vlaznost = linija.rstrip().split(';')
			mesec = {} # kreiranje praznog rečnika
			mesec['ime'] = ime # smeštanje vrednosti ime na ključ ime
			mesec['temperatura'] = int(temperatura) # smeštanje vrednosti na ključ temp
			mesec['vlaznost'] = int(vlaznost) # smeštanje vrednosti na ključ vlaznost
			suma_temp += int(temperatura) # brojač poena svih studenata
			meseci.append(mesec) # dodavanje rečnika student u listu
			
	suma_temp = suma_temp/12
	print (suma_temp)
	
	for mesec in meseci: # petlja po svim rečnicima u listi meseci
		if mesec['temperatura'] >= 15: # ispitivanje uslova
			topli.append(mesec) # dodavanje rečnika ako je uslov ispunjen
	
	for mesec in meseci: # petlja po svim rečnicima u listi meseci
		if mesec['vlaznost'] <70: # ispitivanje uslova
			notvlazni.append(mesec) # dodavanje rečnika ako je uslov ispunjen
	
	
	with open('izlaz.txt', 'w') as fajl:
		fajl.write('Meseci koji su imali vlažnost vazduha manju od 70% \n')
		fajl.write('--------------------------------------------\n')
	
		for mesec in notvlazni:
			ime = mesec['ime']
			fajl.write(f"{ime:30} {mesec['vlaznost']:10}\n")
	
		fajl.write('--------------------------------------------\n')

# poziv funkcije u glavnom programu
napravi_izvestaj('vreme.csv')

[vreme]: /vreme.csv
