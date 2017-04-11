            cars = 100
spaceInCar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carPool = carsDriven * spaceInCar
avgPassengersPerCar = passengers / carsDriven

print "There are" ,cars ,"cars available."
print "There are only" ,drivers ,"drivers available."
print "There will be" ,carsNotDriven ,"empty cars today."
print "We have" ,passengers ,"to carpool today."
print "We can transpose" ,carPool ,"people today."
print "We need to put about" ,avgPassengersPerCar ,"in each car"



