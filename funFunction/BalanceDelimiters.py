def balanceDeli(a):
    data = []
    brackets = {'{':'}', '(':')', '[':']'}
    for i in a:
        if i in brackets:
            data.append(i)
        else:
            if not data or i != brackets[data[-1]]:
                return False
            else:
                data.pop()
    return True if not data else False
string = '({})'
print(balanceDeli(string))
