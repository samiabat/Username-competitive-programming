def ts(n,m,v):
    if v == 1:
        return n*m
    return (((n+v-1)//v)*((m+v-1)//v))
a,b,c = [ int(i) for i in input().split()]
print(ts(a,b,c))