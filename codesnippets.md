# Code snippets

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

I/O: COM porte (bruger 3rd party extension der hedder [pyserial](http://pyserial.sourceforge.net/), som kan installes med `pip install pyserial`)

Jeg har ikke selv proevet pyserial. Nedenstaaende eksempel er hentet fra stackoverflow: [Full examples of using Pyserial package](http://stackoverflow.com/questions/676172/full-examples-of-using-pyserial-package). Der er [flere (og nok bedre) eksempler](http://pyserial.sourceforge.net/examples.html) på pyserials hjemmeside.

Se ogsaa [Short Introduction to PySerial](http://pyserial.sourceforge.net/shortintro.html)

```python
import serial
ser = serial.Serial(0)  # open first serial port
print ser.portstr       # check which port was really used
ser.write("hello")      # write a string
ser.close()             # close port
```

Telnet:

```python
import getpass
import sys
import telnetlib

HOST = "localhost"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print tn.read_all()
```

Data parsing: hent vejret med JSON via web

```python
import urllib2
import json

# hent vejret for Koebenhavn via web
url = 'http://api.openweathermap.org/data/2.5/weather?q=Copenhagen,dk'
response = urllib2.urlopen(url)

# parse JSON resultatet
data = json.load(response)
print 'Weather in Copenhagen:', data['weather'][0]['description']
```

XML Parsing og navigering:

```python
# Read XML from file
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

root.tag
# 'data'
root.attrib
# {}

# Loop over root children
for child in root:
  print child.tag, child.attrib
```