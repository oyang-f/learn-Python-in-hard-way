#this one is like your scripts argv
def print_two (*args):
	arg1,arg2 =args
	print "arg1: %r, arg2: %r," % (arg1,arg2)

# OK, That *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)
	
# this just take one arguments
def print_one(arg1):
	print "arg1: %r" % arg1

# this one take no arguments
def print_none():
	print "I got nothin'."

print_two("Jingshan","Pan")
print_two_again("Jingshan","Pan")
print_one("First!")
print_none()
