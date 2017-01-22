def Selectionsort(t):
    for x in range(0,len(t)-1):
        minval=t[x]
        for y in range(x+1,len(t)):
            if t[y]<minval:
                minval=t[y]
                minindex=y
        t[x],t[minindex]=t[minindex],t[x]
    return t

print(Selectionsort([5,77,2,44,11,0,92]))
        
