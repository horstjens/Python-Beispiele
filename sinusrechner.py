# -*- coding: utf-8 -*-
import math

def rechne(auswahl="1"):
    """mache gewünschte Rechnung und liefere Ergebnis zurück"""
    auswahl = int(auswahl)
    winkel = float(raw_input("Bitte gib den Winkel in Grad ein! (z.B. 14.9)"))
    if len(horst[auswahl]) == 4:
        untergrenze = horst[auswahl][2]
        obergrenze = horst[auswahl][3]
        if winkel<untergrenze or winkel>obergrenze:
            print""
            print "WINKEL ausserhalb des erlaubten Bereiches %i,%i" %(untergrenze,obergrenze)
            return 0,0,True
    winkel2 = winkel*math.pi/180.0 #Winkel von Grad in Radiant umrechnen GENAUER!
    #zahl2 = raw_input("Bitte gib die zweite Zahl der %s ein!"% horst[auswahl][1] )
    rechenstring = "math.%s(%f)" %(horst[auswahl][0],winkel2)
    #print rechenstring
    # y = math.sin(x)
    ergebnis = eval(rechenstring)
    #print ergebnis
    ergebnis2=ergebnis*180.0/math.pi #Ergebnis nun wieder in Grad
    return ergebnis,ergebnis2,False


print "Der tollste Sinusrechner in der GESCHICHTE"
print "powered by mathespass.at, der besten Homepage für KIDS!"
print ""

horst= {1: ["sin","Sinus"],
        2: ["cos","Cosinus"],
        3: ["tan","Tangens"],
        4: ["acos","arcCosinus", -1, 1],
        5: ["atan","arcTangens"],
        6: ["asin","arcSinus", -1, 1],
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
    
    if auswahl in ["1","2","3","4","5","6"]:
        # user war brav und hat eine gute auswahl getroffen
        ergebnis,ergebnis2,fehler = rechne(auswahl)
        if fehler:
            print "FEHLER! Keine Berechnung möglich"
            print""
        else:
            print ""
            print "Das Ergebnis lautet: %f GRAD" % ergebnis2
            print "Das Ergebnis lautet: %f RADIANT" % ergebnis
            print""
        
    else:
        # user war schlimm und wird geschimpft
        print "FEHLER"