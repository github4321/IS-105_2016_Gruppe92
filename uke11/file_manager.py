# -*- coding: utf-8 -*-

# Burde legge inn flere 'if exists'  


import os
import shutil
from os.path import exists

print "\nWhat would you like to do?\n"
print "Type 'dir' to list directory."
print "Press 'r' to read a file."
print "Press 'a' to add text to file."
print "Press 'c' to copy a file."
print "Press 'n' to create a new file."
print "Press 'd' to delete a file."
print "Type 'folder' to create a new foldder."
print "Type 'move' to move a file."
print "Press CTRL-C to exit."

	
choice = raw_input(">")

# Viser innholdet i directory, må endres for hver bruker
if choice == "dir":
	print os.listdir("C:\Users\eier\Documents\IS-105\ica_uke_11")

# Printer ut teksten i valgt fil
elif choice == "r":
	filename = raw_input("What file would you like to read?\n>")
	txt = open(filename)
	print txt.read()
	txt.close()
	
# Legger til tekst i valgt fil
elif choice == "a":  
	filename = raw_input("Choose file:\n>")
	txt = open(filename, "a")
	print "Type what you want to add and press RETURN."
	added_txt = raw_input(">")
	txt.write(" ")
	txt.write(added_txt)
	txt.close()
	print "Text added."
	
# Kopierer en eksisterende fil til en ny
elif choice == "c":
	filename = raw_input("Choose file to copy from: \n>" )
	in_file = open(filename)
	indata = in_file.read()
	new_file = raw_input("Name the new file:\n>")
	copy = open(new_file, "w")
	copy.write(indata)
	in_file.close()
	copy.close()
	print "File copied."
	
# Lager en ny fil 
elif choice == "n":
	filename = raw_input("Name your file:\n>")
	new_file = open(filename, "w")
	new_file.close()
	print "New file created."
	
# Sletter valgt fil
elif choice == "d":
	filename = raw_input("Choose file to delete:\n>")
	if os.path.exists(filename):
		os.remove(filename)
		print "File deleted."
	else:
		print "%s does not exists. Please try again." % filename
	
# Lager en ny mappe
elif choice == "folder":
	new_folder = raw_input("Name the folder:\n>")
	os.makedirs(new_folder)
	print "New folder created."
	
# Flytter en valgt fil 
elif choice == "move":
	current = raw_input("Enter current file path:\n>")
	new = raw_input("Enter new filepath:\n>")
	shutil.move(current, new)
	print "File moved."

else:
	print "Unknown command. Please start over."
