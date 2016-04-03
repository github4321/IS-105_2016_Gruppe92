# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv 


txt = open(filename)

print "Opening %r:" % filename
print "\n"
print txt.read()
print "\n"

print "To edit press RETURN."
print "To exit press CTRL-C."

raw_input()

txt = open(filename)

print "Type what you want to add and press RETURN:"

edit = raw_input(">")

txt = open(filename, "a")
txt.write(edit)

print "Closing file."

txt.close()