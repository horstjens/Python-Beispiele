# -*- coding: utf-8 -*-
import random
import math
import easygui
leon = True
anfangszahl = 1
endzahl =100
versuche = 5
while leon:
    ergebnis = easygui.buttonbox("Willkommen bei dem Zahlenratespiel!                    Voreingestellte Werte: 1,100 als Zahlengrenze und 5 Versuche!","Das Zahlenratespiel",("Beginnen","Einstellungen","Exit"))
    if ergebnis=="Beginnen":
        zufallszahl = random.randint(anfangszahl,endzahl)
        rennen=True
        while rennen:
            if versuche==0:
                easygui.msgbox("Du hast leider keine Versuche mehr!","Verloren","Zurück zum Hauptmenü")
                rennen=False
            if versuche>0:
                versuche = versuche-1
                versuch = easygui.integerbox("Bitte gib deinen Versuch ein!", "Versuch", lowerbound=1, upperbound=endzahl)
                if versuch>zufallszahl:
                    stop = easygui.buttonbox("Du hast die Zahl nicht erraten! TIPP: Die Zahl ist kleiner!", "Nicht erraten", ("Nochmal versuchen","Aufhören"))
                    if stop=="Aufhören":
                        rennen=False
                if versuch<zufallszahl:
                    stop = easygui.buttonbox("Du hast die Zahl nicht erraten! TIPP: Die Zahl ist größer", "Nicht erraten", ("Nochmal versuchen","Aufhören"))
                    if stop=="Aufhören":
                        rennen=False
                if versuch==zufallszahl:
                    easygui.msgbox("Du hast die Zahl erraten! Herzliche Gratulation!")
                    rennen = False
        else:
            print ""
    if ergebnis=="Exit":
        leon = False
    if ergebnis == "Einstellungen":
        frischauf = True
        while frischauf:
            einstellungenantwort = easygui.buttonbox("Hier kannst du benutzerdefinierte Einstellungen vornehmen! (die Spielfreude kann verringert werden, bei benutzerdefinierten Obergrenzen oder Versuchen, aber man kann die Normale Einstellungen-Schaltfläche nutzen, um zu den Anfangseinstellungen zurückkehren zu können!)","Einstellungen",("Fortfahren","Normale Einstellungen","Zurück"))
            if einstellungenantwort == "Zurück":
                frischauf = False
            if einstellungenantwort == "Normale Einstellungen":
                anfangszahl = 1
                endzahl =100
                versuche = 5
                frischauf = False
            if einstellungenantwort== "Fortfahren":
                neuerwert = easygui.integerbox("Bitte gib einen eigenen Wert für die obere Schranke des Zahlenratespiels ein (TIPP: ab 1000 wird es sehr knifflig, es geht bis 1000000 als Höchstwert!)", "Egene Zahl eingeben", lowerbound=10, upperbound=1000000)
                endzahl = neuerwert
                versuche = easygui.integerbox("Bitte gib die die Zahl ein, wie viele Versuche du maximal brauchen darfst!)", "Höchste Versuchsanzahl eingeben", lowerbound=1, upperbound=1000)
                frischauf = False