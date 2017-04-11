states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    "New York": 'NY',
    'Michigan': 'MI'
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def printTen():
    print '-' * 10

printTen()
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

printTen()

print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbrevitation is: ", states['Florida']

printTen()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

printTen()

for state,abbrev in states.items():
    print "%s is abbreviated as: %s" %(state, abbrev)

printTen()

for abbrev, city in cities.items():
    print "%s has the city %s" %(abbrev, city)

printTen()
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(
        state ,abbrev, cities[abbrev]
    )

printTen()

state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" %city
