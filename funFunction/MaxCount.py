def most_frequent(a):
    count ={}
    max_count=0
    max_item=None
    for i in a:
        if i not in count:        #if item is not in count
            count[i] = 1          #add and count it 
        else:
            count[i] += 1         #already exist, we count increase
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item

a=[1,1,3,3,3,6,5,4]
print(most_frequent(a))
