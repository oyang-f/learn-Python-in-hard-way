from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

#we could do these two on one line too, how?
open(to_file,'w').write(open(from_file).read())



#from_file.close()
#to_file.close()
