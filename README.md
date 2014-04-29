# To-dages introduktion til Python

Vi koder fra starten af. Vi løser opgaver og skriver rigtige programmer. Vi bruger nettet til at finde hjælp og lærer hvilke sider er bedst. Der er mange fordele ved Python; en af dem er at der er så mange aktive udviklere, at der altid er nogen der har stillet det samme spørgsmål som dig, og svaret findes næsten altid på [stackoverflow](http://stackoverflow.com/) (søg enten via Google eller direkte på stackoverflow).

* Du vil lære hvad Python er
* Du vil lære hvilke værktøjer du skal bruge
* Du vil lære at kode Python til [kommandolinjen](http://stackoverflow.com/questions/1077347/hello-world-in-python), [web-programmering](http://flask.pocoo.org/docs/quickstart/) og [GUI-programmerings](http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm)
* Vi bruger Python 2 (stort set det samme som Python 3, og bruges af utroligt mange)

Under kurset viser jeg nogle små code snippets, som kan genbruges i mange sammenhænge. Du finder dem i dokumentet [codesnippets.md](codesnippets.md).

## Documentation, hjælp og tutorials

Documentation:

* [Python docs: startsiden](https://docs.python.org/2/)
* [Python docs: documentation af syntax](https://docs.python.org/2/reference/index.html)
* [Python docs: documentation af standardbibliotet](https://docs.python.org/2/library/index.html)

Hjælp:

* [StackOverflow](http://stackoverflow.com/)

Tutorials:

* [Learn Python](http://www.learnpython.org/)
* [Officiel tutorial](https://docs.python.org/2/tutorial/)


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