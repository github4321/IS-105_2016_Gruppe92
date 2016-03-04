# -*- coding: utf-8 -*-

leftSide = ["H", "K", "R"]
rightSide = ["empty"]
inventory = ["empty"]
boat = 0

def sail():
    if boat == 0:
        boat = 1
    else:
        boat = 0
        
def load(move):
    leftSide.remove(move)
    rightSide.append
    print ', '.join(rightSide)
    print ', '.join(leftSide)
    

print "På høyre side av elva står en mann, en rev, en høne, og en kornsekk."
print "Mannen har en båt som kan bære ham og en av de andre."
print "Høna og reven kan ikke være alene, fordi reven spiser høna."
print "Kornsekken og høna kan ikke være alene, fordi høna spiser kornet."
print "H for Høne, R for Rev, K for Korn."

move = input("Hvem skal han frakte først? ")
if move == "H":
    load(move)
elif move == "K" or "R":
    print "Dette valget gjør at kornet eller høna blir spist."
    exit()
else:
    print "Du har skrevet noe som er feil."
    exit()



"""
if runde1 == "H":
    sail()
elif runde1 == "K" or "R"
    print ""
    
Load(Sted, item)
    “””Flytter objekt fra Sted (høyre/venstre) til båt”””
    Innhold = innhold + item
    Side = side – item
    If side == Høne/Rev
        print “You idiot. Høna e spist.”
        Exit()
    Elif side == Høne/Korn
        print “No corn for you!”
        Exit()
    Else
        sail()
Unload(Sted)
    “””Flytter objekt fra båt til Sted (høyre/venstre)”””
    Sted = sted + innhold
    Innhold = innhold – innhold
    If side == Høne/Rev
        print “You idiot. Høna e spist.”
        Exit()
    Elif side == Høne/Korn
        print “No corn for you!”
        Exit()
    Elif 	“Do you want to load?”
        If yes
            load()
    Else
        sail()
"""