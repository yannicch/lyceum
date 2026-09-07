# def fact(n):
#     m=[]
#     i=2
#     while i**2 <= n:
#         while n%i ==0:
#             m.append(i)
#             n//=i
#         i+=1
#     if n!= 1:
#         m.append(n)
#     return m
# k=1
# n=[]
# for i in range(2626695891, 2627000000+1):
#     a=fact(i)
#     if len(a)==2:
#        if str(a[0]).count('67')==1 and str(a[1]).count('67')==1:
#             print(i, min(a))
#             k+=1
#        if k==5:
#            break

def fact(n):
    m=[]
    i=2
    while i**2 <= n:
        while n%i ==0:
            m.append(i)
            n//=i
        i+=1
    if n!= 1:
        m.append(n)
    return m
def f(x):
    for i in range(2, x):
        if x %i !=0:
            return True
    return False
kol=0
for i in range(8_117_600_756,10_000_000_000):
    a= fact(i)
    b=max(a)-min(a)
    if str(b).count('1')>=4 and f(b):
        print(i, b)
        kol+=1
    if kol==5:
        break
