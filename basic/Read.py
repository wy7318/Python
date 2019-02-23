jabber = open("/Users/vazzo/Desktop/python/sample.txt",'r')

for line in jabber:
    if "jabberwock" in line.lower(): #lower method make it possible to search it regardless of lower or upper case
        print(line)

jabber.close()

#=======================================================================================================

with open("/Users/vazzo/Desktop/python/sample.txt",'r') as jabber:
    line = jabber.readline() #readline reads a single line from a file and returns a string
    while line:
        print(line, end='')
        line = jabber.readline()

#=======================================================================================================       
        
with open("/Users/vazzo/Desktop/python/sample.txt",'r') as jabber:
    lines = jabber.readlines() #readlines reads the entire file and returns a list of strings
print(lines) #printed as a list
for line in lines:
    print(line, end='')

#=======================================================================================================    
    
with open("/Users/vazzo/Desktop/python/sample.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines[::-1]: #read entire txt backward
    print(line, end='')

#=======================================================================================================    
    
with open("/Users/vazzo/Desktop/python/sample.txt",'r') as jabber:
    lines = jabber.read()
print(lines)
for line in lines[::-1]: #read every character backward
    print(line, end='')
