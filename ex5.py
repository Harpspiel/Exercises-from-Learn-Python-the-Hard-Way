name = 'Zed. A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

def inches_to_centimeters (inches):
    return inches * 2.54

def pounds_to_kilos (pounds):
    return pounds * 0.45359237

print "Let's talk about %s." % name
print "He's %d centimeters tall." % inches_to_centimeters(height)
print "He's %d pounds heavy." % pounds_to_kilos(weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
