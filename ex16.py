from sys import argv

script, fname = argv

print "We're going to erase %r." %fname
print "If you don't want that, hit CTRL -C (^C)."
print "If you do want that, hit RETURN."

raw_input("> ")

print "Opening the file..."
target = open(fname, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
def newLine():
    target.write('\n')


target.write(line1)
newLine()
target.write(line2)
newLine()
target.write(line3)
newLine()

print "And finally we close it."
target.close()