ipAddress = input("please enter an IP address")
print(ipAddress.count(".")) #counting specific character

word_list=["wow", "this", "that", "more"]

word_list.append("plus") #adding word
for state in word_list:
    print("word list I have is " + state)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

number = even + odd #creating new list
number.sort() #sorting number
print(number)

numbers = even + odd
print(numbers)
print(sorted(number))#other way of sorting it
