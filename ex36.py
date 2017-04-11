ten_things = "Apples Orange Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list."

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banna", "Girl", "Boy"]

while len(stuff) != 10:
    next = more_stuff.pop()
    print "Adding: ", next
    stuff.append(next)
    print "There are %d items now." %len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]

print stuff.pop()
print ','.join(stuff)
print '#'.join(stuff[0:10])

theFile = open("tmpFile.txt", 'w')
theFile.write(' '.join(stuff)+'\n')
theFile.close()

