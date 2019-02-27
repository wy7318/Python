def stringMatch(str1=input()):
    if str1 == str1[::-1]:
        print(str1 == str1[::-1]) #if match, return true
    else:
        print(str1 == str1[::-1]) #if not, return false

stringMatch()
