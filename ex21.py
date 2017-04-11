def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "multiplying %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "dividing %d / %d" %(a, b)
    return a / b

def power(a, b):
    res = 1
    while b > 0:
        res *= a
        b -= 1
    return res 

print "Let's do some math:"

age = add(20, 7)
height = subtract(200, 20)
weight = multiply(40, 2.1)
iq = divide(500, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(
    age, height, weight, iq
)
print "2^5 = ",power(3 ,3)
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ",what, "Can you do it ?"
