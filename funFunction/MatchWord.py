def common_word(str1, str2):
    str1_s=str1.split()
    str2_s=str2.split()
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(str1_s) and p2 < len(str2_s):
        if str1_s[p1] == str2_s[p2]:
            result.append(str1_s[p1])
            p1 += 1
            p2 += 1
        else:
            p1 += 1
            if str1_s[p1] == str2_s[p2]:
                result.append(str1_s[p1])
                p1 += 1
                p2 += 1
            else:
                p2 += 1

    return result

str1="hello world really this easy"
str2="hi world this"
print(common_word(str1,str2))
