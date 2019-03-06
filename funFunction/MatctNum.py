def common_elements(list1, list2):
    p1 = 0                                        #pointer of list1
    p2 = 0                                        #pointer of list2
    result = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:                #if match
            result.append(list1[p1])              #add mathcing item on result list
            p1 += 1                               #then move p1,p2 to next one
            p2 += 1                               
        elif list1[p1] > list2[p2]:               #if p1 is bigger
            p2 += 1                               #only move p2 to next and compare
        else:
            p1 += 1
    return result

list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
print(common_elements(list_a1, list_a2))
