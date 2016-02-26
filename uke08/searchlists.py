import timeit

hpcharacters = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Arthur Weasley',
                'Molly Weasley', 'Percy Weasley', 'Bill Weasley', 'Charlie Weasley',
                'Ginny Weasley', 'Aunt Muriel', 'Albus Dumbledore', 'Kendra Dumbledore',
                'Percival Dumbledore', 'Aberforth Dumbledore', 'Ariana Dumbledore',
                'Rubeus Hagrid', 'Fang', 'Fluffy', 'Aragog', 'Buckbeak', 'Walden Macnair',
                'Severus Snape', 'Lily Potter', 'James Potter', 'Albus Severus Potter',
                'Luna Lovegood', 'Xenophilius Lovegood', 'Neville Longbottom',
                'Augusta Longbottom', 'Fleur Delacour', 'Gabrielle Delacour', 'Fawkes',
                'Hedwig', 'Errol', 'Pigwidgeon', 'Frank Bryce', 'Remus Lupin', 'Nymphadora Tonks',
                'Ted Tonks', 'Draco Malfoy', 'Lucius Malfoy', 'Narcissa Malfoy', 'Gregory Goyle',
                'Vincent Crabbe', 'Sirius Black', 'Phineus Nigellus Black', 'Regulus Arcturus Black',
                'Mrs Black', 'Bellatrix Lestrange', 'Antonin Dolohov', 'Yaxley', 'Avery', 'Troy', 'Moran',
                'Aidan Lynch', 'Hassan Mostafa', 'Dirk Cresswell', 'Albert Runcorn', 'Mary Cattermole',
                'Reg Cattermole', 'Mafalda Hopkirk', 'Professor Quirrell', 'Gilderoy Lockhart', 'Sybil Trelawney',
                'Alastor Moody', 'Bartemius Crouch', 'Barty Crouch Jr', 'Bertha Jorkins', 'Ludo Bagman',
                'Rita Skeeter', 'Bathilda Bagshot', 'Nagini', 'Ernie Prang', 'Stan Shunpike', 'Ernie MacMillan',
                'Hannah Abbott', 'Susan Bones', 'Justin Finch-Fletchley', 'Marcus Belby', 'Terry Boot',
                'Michael Corner', 'Colin Creevey', 'Dennis Creevey', 'Dudley Dursley',
                'Vernon Dursley', 'Petunia Dursley', 'Marge Dursley', 'Piers Polkiss',
                'Mundungus Fletcher', 'Arabella Figg', 'Ronan', 'Magorian', 'Bane', 'Firenze',
                'Mr Roberts', 'Demelza Robins', 'Oliver Wood', 'Angelina Johnson',
                'Cormac MacLaggen', 'Alicia Spinnet', 'Katie Bell', 'Roger Davies',
                'Marcus Flint', 'Warrington', 'Montague', 'Tom', 'Madam Malkin',
                'Rosmerta', 'Borgin', 'Burke', 'Beedle the Bard', 'Scabior', 'Fenrir']

hpshort = ['Harry', 'Hermione', 'Ron', 'Hagrid', 'Snape', 'Hedwig', 'Voldemort']

character = 'Hedwig'

def search_fast(hpcharacters, character):
    for item in hpcharacters:
        if item == character:
            return True
    return False
def search_slow(hpcharacters, character):
    return_value = False
    for item in hpcharacters:
        if item == character:
            return_value = True
    return return_value

search_slow(hpcharacters, character)
print(timeit.timeit("search_slow(hpcharacters, character)", setup="from __main__ import search_slow, hpcharacters, character"))

search_fast(hpcharacters, character)
print(timeit.timeit("search_fast(hpcharacters, character)", setup="from __main__ import search_fast, hpcharacters, character"))


def search_fast(hpshort, character):
    for item in hpshort:
        if item == character:
            return True
    return False
def search_slow(hpshort, character):
    return_value = False
    for item in hpshort:
        if item == character:
            return_value = True
    return return_value

search_slow(hpshort, character)
print(timeit.timeit("search_slow(hpshort, character)", setup="from __main__ import search_slow, hpshort, character"))

search_fast(hpshort, character)
print(timeit.timeit("search_fast(hpshort, character)", setup="from __main__ import search_fast, hpshort, character"))