for state in ["not pinin","no more"]:
    #print("this is "+state)
    print("this is {}".format(state))

#0 through 100 with 3 increment
for i in range(0, 100, 3):
    print("i is {}".format(i))

for i in range(1,10):
    for j in range(1,10):
        print("{} times {} is {}".format(i,j,i*j))
    print("===================")

#printing with condition
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for i in quote:
    if i in 'ZXCVBNMLKJHGFDSAWQRTYUIOP':
        print(i)
