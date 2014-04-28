# To-dages introduktion til Python

Vi koder fra starten af. Vi løser opgaver og skriver rigtige programmer. Vi bruger nettet til at finde hjælp og lærer hvilke sider er bedst. Der er mange fordele ved Python; en af dem er at der er så mange aktive udviklere, at der altid er nogen der har stillet det samme spørgsmål som dig, og svaret findes næsten altid på [stackoverflow](http://stackoverflow.com/) (søg enten via Google eller direkte på stackoverflow).

* Du vil lære hvad Python er
* Du vil lære hvilke værktøjer du skal bruge
* Du vil lære at kode Python til [kommandolinjen](http://stackoverflow.com/questions/1077347/hello-world-in-python), [web-programmering](http://flask.pocoo.org/docs/quickstart/) og [GUI-programmerings](http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm)
* Vi bruger Python 2 (stort set det samme som Python 3, og bruges af utroligt mange)

## Links

* [Python docs: oversigt over indbyggede funktioner](https://docs.python.org/2/library/functions.html)
* [Python docs: documentation af syntax](https://docs.python.org/2/reference/index.html)
* [Python docs: documentation af standardbibliotet](https://docs.python.org/2/library/index.html)
* [StackOverflow](http://stackoverflow.com/)
* [Learn Python](http://www.learnpython.org/)

## Brugbare kode-stumper

Functional programmering: list comprehension, map, filter, reduce

```python
# list comprehension, f.eks. lav en liste af tal-par
x = [(i, i**2) for i in range(7)]
# x: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]

# map, f.eks. udvaelg element nummer to fra hvert par
x = map(lambda x: x[1], x)
# x: [0, 1, 4, 9, 16, 25, 36]

# filter, f.eks. filtre ulige tal fra
x = filter(lambda x: x % 2 == 0, x)
# x: [0, 4, 16, 36]

# reduce, f.eks. beregn sum af listens elementer
x = reduce(lambda x, y: x + y, x, 0)
# x: 56
```

Functional programming: zip, dict

```python
# importer string modulet, indeholder f.eks. et ord med alle bogstaver
import string

# list comprehension, f.eks. lav en liste af alle smaa bogstaver (latinske)
x = [c for c in string.letters if c.islower()]
# x: ['a', 'b', 'c', 'd', 'e', 'f', 'g', ... , 'z']

# lav en liste af tal der er lige så lang som listen af bogstaver
y = range(len(x))

# zip de to lister sammen til en liste af par
xy = zip(x, y)
# xy: [('a', 0), ('b', 1), ('c', 2), ... , ('z', 25)]

# lav et dictionary ud af listen af par
d = dict(xy)
# d: {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, ..., 'x': 23, 'z': 25}
# bemaerk at raekkefoelgen af keys ikke er den samme som i listen
```

Regular expressions: soegning i text efter moenster (se ogsaa Python doc: [regular expressions](https://docs.python.org/2/library/re.html))

```python
# importer regular expression modulet, re
import re

# lav en sætning med de ord vi vil finde
s = 'en mand gik 50 KILOMETER, en anden mand gik 49 km'

# find alle tal der står foran ordet kilometer
# (uanset case og uanset om der står kilometer eller km)
regex_pattern = '(\d+) [kilometer|km]'
re.findall(regex_pattern, s.lower())

# [50, 49]
```

Konvertering: fra en liste af tal -> text string m. komma-separerede tal

```python
# Lav  en liste af tal
s = [1, 2, 3, 4, 5]

# Konverter til en liste af text-tal
s = map(lambda x: str(x), l)

# Konverter til en enkelt tekst-streng bestaaende af tal adskilt af komma
s = ', '.join(l)
# s: '1, 2, 3, 4, 5'

# konverter tilbage til en liste af tal
# bruger list comprehension og casting af text -> int
s = [int(c.strip()) for c in s.split(',')]
```

I/O: filer (read):

```python
# aaben en fil i read-mode og print dens indholdet
f = open('eksempel.txt', 'r')
for line in f:
	print line
f.close()

# bedre maade at aabne filer paa
# saa behoever man ikke lukke dem
with open('eksempel.txt', 'r') as f:
	for line in f:
		# rstrip, saa der ikke kommer to linjeskift
		print line.rstrip()
```

I/O: filer (append):

```python
# lav en liste af ord, split string på mellemrum
words = 'the quick brown fox'.split()

# append ord til fil ('a' option)
# hvert ord på sin egen linje, p.g.a. '\n'.join(words)
with open('eksempel2.txt', 'a') as f:
	for word in '\n'.join(words):
		f.write(word)
```

Data parsing: hent vejret med JSON via web

```
import urllib2
import json

# hent vejret for Koebenhavn via web
url = 'http://api.openweathermap.org/data/2.5/weather?q=Copenhagen,dk'
response = urllib2.urlopen(url)

# parse JSON resultatet
data = json.load(response)
print 'Weather in Copenhagen:', data['weather'][0]['description']
```

## Program - dag 1

### 8:30 - 9:00 (navnerunde og test af installation)

1. Vi starter med en navnerunde. Sig dit navn og fortæl kort om din tidligere erfaringer med programmering (ikke kun Python).
2. Interaktiv Python: Åben kommando-prompten (i Windows eller *nix) og skriv 'python' (får du en fejl eller en Python prompt?). Hvis det virkede har du startet Python i interaktiv mode. Beskriv hvad du ser. Prøv at skrive 1+1 og tryk enter.
3. Opret en mappe på din computer, som vil indeholde de program-filer du skriver i de næste to dage.
4. Lav en fil med navn 'hello.py' i mappen og skriv følgende indhold i filen:

Dette er et Python program. Kør programmet ved at skrive `python hello.py` på kommandolinjen (du skal stå i samme mappe som filen er gemt i). Virkede det?

```python
print 'Hello world'
```

**Tips**: check din PATH variabel hvis det ikke virker. Skriv 'quit()' + enter for at afslutte python fortolkeren (hvis det virker og du er færdig).


### 9:00 - 12:00 (grundlæggende Python)

* Udtryk, [variable og types](http://www.learnpython.org/en/Variables_and_Types)
* Datastrukturer: [lister](http://www.learnpython.org/en/Lists), tupler, [dictionaries](http://www.learnpython.org/en/Dictionaries) og [mængder](http://www.learnpython.org/en/Sets)
* Kontrolstrukturer: [conditions](http://www.learnpython.org/en/Conditions) og [loops](http://www.learnpython.org/en/Loops)
* [Funktioner](http://www.learnpython.org/en/Functions)
* Funktionel programmering (map, filter, aggregate, lambda, list comprehension)

### 12:30 - 16:30 (videregående Python)

* [Objekter og Klasser](http://www.learnpython.org/en/Classes_and_Objects)
* [Håndtering af fejl med exceptions](http://www.learnpython.org/en/Exception_Handling)
* Dokumentation i Python (docstrings og dir/help funktioner)
* [Strenge, tekst og formattering](http://www.learnpython.org/en/String_Formatting)
* [Grundlæggende operationer på strings](http://www.learnpython.org/en/Basic_String_Operations)