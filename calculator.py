i = 0
GesamtNote = 0

def NeueNote():
    global GesamtNote
    global i
    print("Gib bitte eine Note an, welche du speichern möchtest:")
    Note = input()
    if Note:
        Note = int(Note)
        if 0<Note<7:
            Noten.append(Note)
            print(Noten)
        else:
            print("Please input a valid grade.")
    else:
        print("Please input a valid grade.")
    GesamtNote += Note
    i += 1
    Finish()

def Finish():
    Finished = input("Are you finished? [y/n]")
    print(Finished)
    if Finished == "y":
        print(GesamtNote)
        Durchschnitt = GesamtNote/len(Noten)
        print(Durchschnitt)
    elif Finished == "n":
        NeueNote()
    else:
        print(Finished)
        print("Please give a valid input")
        Finish()

if __name__ == '__main__':
    print("Willkommen zum Notenrechner!")
    Noten = []
    NeueNote()
