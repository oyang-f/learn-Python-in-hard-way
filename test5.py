name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_cm = round(height * 2.54)
weight_in_kg = weight * 0.45

print "Let's talk about %r." % name
print "He's %r inches or %.2f cm tall." % (height,height_in_cm)
print "He's %r pounds or %r kg heavy." % (weight,weight_in_kg)
print "Actually that' not too heavy."
print "He's got %r eyes and %s hair." % (eyes,hair)
print "His teeth are usually %r depending on the coffee." % teeth

#This line is tricky ,try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age,height,weight,age+height+weight)
