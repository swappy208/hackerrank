##def Simplegen(x):
##    simplegen=(f+f for f in range (x))
##    for f in simplegen:
##        print(f)
##    return f
##
##print(Simplegen(10))


def Usingyield(n):
    currentn=0
    while currentn <= n:
        yield currentn
        currentn+=1

print(sum(Usingyield(10)))
