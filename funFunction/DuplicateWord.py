res=input().lower().split()


def isDuplicate(word):
    hashTable ={}
    dup=[]
    for i in range(0,len(word)):
        if word[i] not in hashTable:
            hashTable[word[i]]=True #element insertion if not in hash table
        else:
            dup.append(word[i]) #if element in the hash table, we know it is duplicate

    return dup

print(isDuplicate(res))
