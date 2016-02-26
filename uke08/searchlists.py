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
                'Mrs Black', 'Bellatrix Lestrange']

def search_fast(hpcharacters, 'Gregory Goyle'):
    for item in hpcharacters:
        if item == 'Gregory Goyle':
            return True
    return False
def search_slow(hpcharacters, 'Gregory Goyle'):
    return_value = False
    for item in hpcharacters:
        if item == 'Gregory Goyle':
            return_value = True
    return return_value