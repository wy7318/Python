ipAddress = input("please enter an IP address")
print(ipAddress.count(".")) #counting specific character
#===============================================================================#
word_list=["wow", "this", "that", "more"]
#===============================================================================#
word_list.append("plus") #adding word
for state in word_list:
    print("word list I have is " + state)

#===============================================================================#

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

number = even + odd #creating new list
number.sort() #sorting number
print(number)

numbers = even + odd
print(numbers)
print(sorted(numbers))#other way of sorting it

number3 = [even, odd] #creating list of two lists
print(number3) 
#===============================================================================#
list_1 = [] #creating enpty list 1
list_2 = list() #creating enpty list 2
print("list_1 {}".format(list_1))
print("list_2 {}".format(list_2))

print(list("each character will be stored in list"))#cut and store each character

even_1 = [2, 4, 6, 8]
another_even = even_1 #another_even will become same as even_1, updated
another_even.sort(reverse=True)
print(even_1)

#===============================================================================#
menu=[]
menu.append(["egg", "spam", "bacon"])
menu.append(["milk", "spam", "sausage"])
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon", "milk"])
menu.append(["egg", "spam", "milk"])

print(menu) #print list of list added

for meal in menu:
    if "egg" not in meal: #list that does not include egg
        print(meal)
        for ingredient in meal:
            print(ingredient) #print eac item in the list
