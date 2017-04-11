from sys import argv

script, fname = argv

txt = open(fname)

print "Here's your file %r:" %fname
print txt.read()

print "Type the filename again:"
fileAgain = raw_input("> ")
txtAgain = open(fileAgain)

print txtAgain.read()