import math
def powerOf(x,y):
    res1 = math.log(y) / math.log(x)
    res2 = math.log(y) / math.log(x)

    return True if(int(res1)%res2==0) else False #Check two values are matching


print(powerOf(2,2))
