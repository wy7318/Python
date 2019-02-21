fruit = {"orange":"a sweet, orange, citrus, fruit",
        "apple": "good for making cider",
        "lemon": "a small, sweet fruit growing in bunches",
        "lime": "a sour, green citrus fruit",
        "apple": "red fruit"}#update apple value with this

print(fruit)
print(fruit["lemon"])
fruit["pear"]="an odd shaped apple" #adding value to set
print(fruit)
fruit["pear"]="Great with tequila" #overriding existing value
print(fruit)
del fruit["lemon"] #deleting element
print(fruit)
fruit.clear() #clearing whole set
print(fruit)

#========Function of finding description of element of set================================
while True:
        dict_key = input("please enter a fruit:")
        if dict_key == "quit":
                break
        if dict_key in fruit:
                print(fruit[dict_key])
        else:
                print("Sorry, we don't have info of {}".format(dict_key))

                
#============================================================================================
ordered_keys = list(fruit.keys()) #keys method returns values of object
ordered_keys.sort() # this will make sure set will have same order(Alphabetical) each time
for i in ordered_keys:
        print(i + "-" + fruit[i])
#======================================Set to Tuple==============================================

print(fruit.items()) #creating tuples

for snack in fruit.items():
        item, description = snack
        print(item + " is " + description)
        
#====================================Join Method=====================================================  
myList = ["a", "b", "c", "d"]
letters="zxcvbnmmasdfghjklqwertyuiop"
newString = ",".join(myList)
newString2=",".join(letters)
print(newString)
print(newString2)

#============================Update, Copy Methods========================================================

veg = {"cabbage": "every child's favorite",
       "sprout" : "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}

veg.update(fruit) #addinf fruit to veg set
print(veg)
print(fruit.update(veg)) #does not do anything

nice_and_nasty = fruit.copy() #copy set
nice_and_nasty.update(veg)
print(nice_and_nasty)
