def fact(n):
    m=[]
    d = 2
    while d**2 <= n:
        while n % d== 0:
            m.append(d)
            n //= d
        d+=1
    if n!= 1:
        m.append(n)
    return m

for i in range(8117600756, 10000000000):
    M=max(fact(i))-min(fact(i))
    if len(fact(M))==1 and str(М).count("1")>=4:
        print(i, М)
        count+=1
        if count==5:
            break
            

