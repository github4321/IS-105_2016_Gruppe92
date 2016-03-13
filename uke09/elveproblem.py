# -*- coding: utf-8 -*-

#Setter opp hvordan spillet starter
leftSide = ["Høne", "Korn", "Rev"]
rightSide = []
inventory = []
boat = 0
frakt = "ingenting"

def start():
    print "En mann skal flytte en rev, ei høne og en sekk med korn fra en side av en elv"
    print "til den andre."
    print "Mannen har en båt som kan bære ham og en av de andre."
    print "Kornsekken og høna kan ikke være alene, fordi høna spiser kornet."
    move()

def move():
    print "På venstre side er: " + ', '.join(leftSide)
    print "På høyre side er: " + ', '.join(rightSide)    
    global frakt
    frakt = input("Hva skal mannen frakte? ")
    if frakt == "Høne" or "høne":
        load()
    elif frakt == "Korn" or "Rev":
        print "Dette valget gjør at kornet eller høna blir spist."
        exit()
    else:
        print "Du har skrevet noe som er feil. Too bad for you."
        exit()
        
def load():
    #Laster opp i båten. Fjerner den valgte gjenstanden fra elvesiden og opp i båten
    #Printer ut hva som er flyttet til båten og hva som er på hver side
    global frakt
    leftSide.remove(frakt)
    inventory.append(frakt)
    print "Du har flyttet " + frakt + " til båten."
    if len(leftSide) == 0:
        print 'Det står ingenting på venstre side.'  
    else:
        print "På venstre side er: " + ', '.join(leftSide)
    if len(rightSide) == 0:
            print 'Det står ingenting på høyre side.'    
    else:
        print "På høyre side er: " + ', '.join(rightSide)
    sail()
    
def sail():
    #Flytter båten fra en side av elven til den andre
    global boat
    if boat == 0:
        boat = 1
    else:
        boat = 0
    unload()
    
def unload():
    global frakt
    global boat
    inventory.remove(frakt)
    if boat == 0:
        leftSide.append(frakt)
    else:
        rightSide.append(frakt)
    move()
        
start()
