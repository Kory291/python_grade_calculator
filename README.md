# python_grade_calculator
A python project containing a grade calculator for demonstration of basic python functions.


## Grundlagen

### Daten, ihre Typen und speichern

#### Zahlen

Zahlen können in zwei Typen unterschieden werden. Das sind die folgenden:
- ganze Zahlen: `int`
- Dezimalzahlen: `float`

Das Gute ist, dass Python macht das selber schon und nimmt den richtigen Datentyp.

Zuweisung:
```python
meine_ganze_zahl = 1
meine_dezimalzahl = 2.4
```
**Achtung:** Anders als vielleicht gewohnt, muss hier ein Punkt statt einem Komma nuzten. Das ist also wie im Englischen.

#### Text

Ein weiterer Datentyp ist Text. Dieser ist allgemein als `string` bekannt.
Strings können kombiniert werden. Strings können auch getrennt werden. 
Es sind auch weitere Bearbeitungen möglich, aber die sind hier nicht relevant. 

Zuweisung:
```python
mein_text = "Hallo Welt!"
```

Kombination von zwei Texten
```python
mein_erster_text = "Hallo"
mein_zweiter_text = "Welt!"

mein_zusammengefügter_text = mein_erster_text + " " + mein_zweiter_text
```
Hier wird noch ein `" "` eingefügt, um `Hallo Welt!`, statt `HalloWelt!` zu erhalten.

#### Wahrheitswerte

Es gibt für Wahrheitswerte einen eigenen Datentyp. Dieser wird weiter unten interessant.
Dieser Datentyp wird `bool` genannt. Zusammengefasst soll er "Ja" oder "Nein" ausdrücken.
Die zwei Wahrheitswerte sind `True` und `False`

```python
ja = True     # Zuweisung des Wahrheitswerts "Ja" beziehungsweise True auf die Variable ja
nein = False  # Zuweisung des Wahrheitswerts "Nein" beziehungsweise False auf die Variable nein 
```

#### Listen

Listen speichern mehrere Elemente. Diese müssen auch nicht zwingend vom selben Typ sein. Sie können besonders bei Schleifen interessant sein.

Erstellung:
```python
meine_liste = ["Wert 1", "Wert 2", "Wert 3"]  # Erstellung und Speicherung mit den Textwerten "Wert 1", "Wert 2", "Wert 3"
```

Hinzufügen von Elementen:
```python
meine_liste = ["Wert 1", "Wert 2", "Wert 3"]  # erste Erstellung der Liste
meine_liste.append("Wert 4")                  # Hinzufügen des Werts "Wert 4" zur Liste meine_liste
```

Abfragen von Elementen:
```python
meine_liste = ["Wert 1", "Wert 2", "Wert 3"]  # erste Erstellung der Liste
wert_1 = meine_liste[0]                       # der erste Wert der Liste wird abgefragt und auf der Variablen wert_1 gespeichert. 
```
**Achtung:** In den allermeisten Programmiersprachen fängt man bei 0 an zu zählen. Das heißt, möchte man den ersten Wert einer Liste abfragen, muss man mit 0 anfangen, statt 1 anfangen.


#### Wörterbücher

Ein etwas komplizierterer Datentyp ist das Wörterbuch, oder auch `dict`.
Es speichert Werte anhand von Schlüsseln. Über diese Schlüssel können 
dann die Werte abgerufen werden.

Erstellung:
```python
mein_dict = {}                          # leer (ohne Elemente)
mein_dict = {"Schluessel 1": "Wert 1"}  # befüllt
```

Abfrage:
```python
mein_dict = {"Schluessel 1": "Wert 1"}   # Erstellung des Wörterbuchs
abfrage = mein_dict.get("Schluessel 1")  # Abfrage des Werts über den Schlüssel "Schluessel 1"
```

Zuweisung:
```python
mein_dict = {"Schluessel 1": "Wert 1"}  # Erstellung des Wörterbuchs
mein_dict["Schluessel 2"] = "Wert 2"    # eigentliche Zuweisung
```

### Eingabe und Ausgabe

Die Ausgabe von Variablen ist ein wichtiger Teil, um dem Nutzer und auch einem 
Entwickler Aktionen sichtbar zu machen. Dafür gibt es eine Funktion, die genutzt werden kann.
```python
meine_variable = 2     # Zuweisung einer Variable zur späteren Nutzung
print(meine_variable)  # Ausgabe der gespeicherten Variable
print("Hier kann auch direkt ein Text stehen")  # direkte Ausgabe eines Textes
```  

Um ein Programm / Skript für einen Nutzer brauchbar zu machen, 
muss eine Form von Nutzereingabe unterstützt werden.
```python
eingabe = input()  # Hier wird die Nutzereingabe auf der Variable eingabe gespeichert
```

### Operationen

#### mathematische Operationen

Im Grunde sind das die Operationen, die man schon seit der Grundschule kennt. 
Also Plus, Minus, Mal und Geteilt.

Plus:
```python
meine_zahl_1 = 2
meine_zahl_2 = 4

ergebnis = meine_zahl_1 + meine_zahl_2  # Ergebnis: 6
```

Minus:
```python
meine_zahl_1 = 2
meine_zahl_2 = 4

ergebnis = meine_zahl_1 - meine_zahl_2  # Ergebnis: -2
```

Mal:
```python
meine_zahl_1 = 2
meine_zahl_2 = 4

ergebnis = meine_zahl_1 * meine_zahl_2  # Ergebnis: 8
```

Geteilt:
```python
meine_zahl_1 = 2
meine_zahl_2 = 4

ergebnis = meine_zahl_1 / meine_zahl_2  # Ergebnis: 0.5
```

#### logische Operationen

Hier werden die Wahrheitswerte interessant. Diese sind das Ergebnis der folgenden Befehle. 

Prüfung auf Gleichheit:
```python
wert_1 = 2
wert_2 = 3

ergebnis = wert_1 == wert_2  # Ergebnis: False -> 2 ist nicht gleich 3 
```
**Achtung:** Beachte, dass hier `==` bei der Prüfung genutzt wird. Das ist ein typischer Fehler, der im ersten Semester eines Studiums gemacht wird.

Prüfung auf Ungleichheit:
```python
wert_1 = 2
wert_2 = 3

ergebnis = wert_1 != wert_2  # Ergebnis: True -> 2 ist ungleich 3
```

### Kontrollsequenzen


#### Schleifen

Um Wiederholungen im Programmablauf zu nutzen, können sogenannte Schleifen genutzt 
werden. Im Wesentlichen gibt es zwei Arten von Schleifen:
1. "Mache etwas solange bis" -- `while`
    Die Schleife wird solange ausgeführt, wie oben True steht. D.h. schreibt man `True` direkt oben rein, läuft die Schleife unendlich lang.

    ```python
    while True:
        print("Ausgabe in Schleife")
    ```
2. "Mache etwas für X Wiederholungen" -- `for`
    Die Schleife wird für eine bestimmte Anzahl von Wiederholungen ausgeführt.
    ```python
    for x in range(5):  # x wird der Wert in der Schleife. Mit der range()-Funktion wird eine Liste erstellt
        print(x)
    # Ausgabe:
    # 0
    # 1
    # 2
    # 3
    # 4
    ```
    Alternativ kann man auch über die einzelnen Elemente einer Schleife laufen.
    ```python
    meine_werte = ["Wert 1", "Wert 2", "Wert 3", "Wert 4"]  # Erstellung der Liste über die iteriert werden soll
    for wert in meine_werte:
        print(wert)
    # Ausgabe:
    # Wert 1
    # Wert 2
    # Wert 3
    # Wert 4
    ```
**Achtung:** Beachte die Einrückungen unter dem `while` und `for`.

#### Wenn-Dann

Wenn-Dann Anweisungen können in Kombination mit Wahrheitswerten genutzt werden, um Abzweigungen in der Programmlogik abzubilden.
Sie können also Entscheidungen von zum Beispiel Nutzereingaben vornehmen.

Beispiel, wo die Entscheidung getroffen wird und der Code im `if`-Block ausgeführt wird.
```python
if True:
    print("Das war die richtige Entscheidung")
```

Beispiel, wo die Entscheidung nicht getroffen wird und der Code im `if`-Block nicht ausgeführt wird.
```python
if False:
    print("Diesen Text wird nie jemand sehen")
```

Es muss also der Wahrheitswert `True` hinter dem `if` stehen, damit der `if`-Block ausgeführt wird.
Außerdem kann die Verkettung aber auch so vorgenommen werden, dass aus dem "Wenn-Dann" ein "Wenn-Dann-Sonst" wird. Das sieht dann folgendermaßen aus.

Beispiel, wo der Pfad des "Sonst" beziehungsweise des `else`-Blocks nicht ausgeführt wird:
```python
if True:
    print("Das war die richtige Entscheidung")
else:
    print("Diesen Text wird nie jemand sehen")
```

Beispiel, wo der Pfad des "Sonst" beziehungsweise des `else`-Blocks ausgeführt wird:
```python
if False:
    print("Diesen Text wird nie jemand sehen")
else:
    print("Das war die richtige Entscheidung")
```

**Achtung:** Beachte auch hier die Einrückungen unter dem `if`

## Fazit
Das sollte erstmal das Gröbste zusammenfassen.
Natürlich ist das nur ein Einstieg, also nutze auch gerne das Internet 
zu deinem Vorteil und suche nach Beispielen oder Problemen, die du findest.