from sys import argv
import socket

script,domain_name=argv

ip_list=[]
address=socket.getaddrinfo(domain_name,0,0,0,0)
print address
print "\n"
for result in address:
    print result
    print '\n'
    print result[-1][0]
    print '\n'
    ip_list.append(result[-1][0])

print ip_list
