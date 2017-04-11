def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print "You have %d cheeses!" %cheeseCount
    print "You have %d boxes of crackers." %boxesOfCrackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheeseAndCrackers(20, 30)

print "Or, we can use variables from our script:"
cheeseCount = 19
crackersCount = 50

cheeseAndCrackers(cheeseCount, crackersCount)

print "We can even do math:"
cheeseAndCrackers(10+20, 5-1)

print "And we can combine two, variables and math:"
cheeseAndCrackers(cheeseCount + 1, crackersCount - 1)