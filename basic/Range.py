my_list = list(range(20)) #creating list using range
print(my_list)

even = list(range(0, 10, 2)) #list of number incremented by 2, start from 0 to 10
odd = list(range(1, 10, 2)) #list of number incremented by 2, start from 1 to 10

print(even)
print(odd)

my_string="abcdefghijklmnoptqrstuvwxyz"
print(my_string.index('e')) #print number of location of 'e'
print(my_string[4]) #print 4th letter in the list

#=========================================================================
r = range(0,100)
print(r)

for i in r[::-2]:
    print(i)

for i in range(99,0,-2):
    print(i)

backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])

