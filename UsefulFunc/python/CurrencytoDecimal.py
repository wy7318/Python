from decimal import Decimal


money1="$123,123,500.00"
money2="-123,123,500.00"
money3="123123,500.00"
money4="-$123,123,500.00"

def Digitize(val):
    if val == None:
        return None
    elif val =='':
        return val
    else:
        return Decimal("".join(d for d in val if d.isdigit() or d == '.' or d == '-'))

print(Digitize(money1))
print(Digitize(money2))
print(Digitize(money3))
print(Digitize(money4))
