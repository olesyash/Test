from greeter import greeter
#Default is "World"
#Author is Olesya <ilana.olesya@gmail.com>
import  sys
if len(sys.argv)>1:
	print "Hello " + sys.argv[1]
else:	
	print "Hello world"