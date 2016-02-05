# -*- coding: utf-8 -*-
import random

#ver 1.3 29.01.2016
#Rebecca Iversen
#generer en tilfeldig valør og farge

valor = [1,2,3,4,5,6,7,8,9,10,11,12,13]
farge = ["klover", "hjerter", "spar", "ruter"]

random.shuffle(valor, random=None)
random.shuffle(farge, random=None)

valor[10] = "Knekt"
valor[11] = "Dronning"
valor[12] = "Konge"
valor[0] = "Ess"


print(random.choice(valor)),
print(random.choice(farge))
print(random.choice(valor)),
print(random.choice(farge))
print(random.choice(valor)),
print(random.choice(farge))
print(random.choice(valor)),
print(random.choice(farge))
print(random.choice(valor)),
print(random.choice(farge))