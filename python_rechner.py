# -*- coding: utf-8 -*-

def rechne(auswahl="1"):
    """mache gewünschte Rechnung und liefere Ergebnis zurück"""
    auswahl = int(auswahl)
    zahl1 = raw_input("Bitte gib die erste Zahl der %s ein!"% horst[auswahl][1] )
    zahl2 = raw_input("Bitte gib die zweite Zahl der %s ein!"% horst[auswahl][1] )
    rechenstring = " %f %s %f" % (float(zahl1), horst[auswahl][0], float(zahl2))
    print rechenstring
    ergebnis = eval(rechenstring)
    return ergebnis


print "Der tollste Rechner in der GESCHICHTE"
print "powered by mathespass.at, der besten Homepage für KIDS!"
print ""
#print " Plusrechnen (1)"
#print " Minusrechnen (2)"
#print " Malrechnen (3)"
#print " Dividieren (4)"
#print "  "
#print " stop (0)"

horst= {1: ["+","Addition"],
        2: ["-","Subtraktion"],
        3: ["*","Multiplikation"],
        4: [":","Division"],
        5: ["**","Potenz"],
        0: ["Quit", "Programm verlassen"]    }




while True:
    # menü neu malens
    dingsda = horst.keys()
    dingsda.sort()
    for x in dingsda:
        print "%i .......%s (%s) " % (x, horst[x][1], horst[x][0]  )
    
    # user fragen welchen menüpunkt er möchte    
    auswahl = raw_input("Bitte gib eine Zahl ein, der zum entsprechenden Rechner führt")

    if auswahl == "0":
        break # entwische aus der while schleife
    
    if auswahl in ["1","2","3","4","5"]:
        # user war brav und hat eine gute auswahl getroffen
        ergebnis = rechne(auswahl)
        print "Das Ergebnis lautet: %f" % ergebnis
        
    else:
        # user war schlimm und wird geschimpft
        print "FEHLER"
    