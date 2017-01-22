def merge(a,b):
    n=0
    merge=""
    c=''
    if len(a)<len(b):
        c=a
        a=b
        b=c
    while n<len(b):
        merge+=a[n]+b[n]
        n=n+1
    x=len(a)
    y=len(b)
    z=0
    while z<(x-y)-1:
        merge+=a[-z]
        z=z+1
        
    return merge

print(merge('abc','defghh'))
