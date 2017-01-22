def Rangenum(t,a,b):
    result=''
    t=sorted(t)
    lastnum=0
	
    for x in t:
	if x>a and x<b:
            result+=str(str(a)+'-'+str(x-1)+','
            lastnum=t[len(t)-1]
	if x==lastnum:
	    result+=str(x)+'-'+str(b)
    return result

print(Rangenum([2,5,8,10,11,12,23,25,26,100],0,200))
