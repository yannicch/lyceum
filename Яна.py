def fact(n):
    m = []
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            m.append(i)
            n //= i
        i += 1
    if n != 1:
        m.append(n)
    return m


t = 0
for j in range(8117600757, 10 ** 15):
    de = fact(j)
    if len(de) > 0:
        s = max(de) - min(de)
        if len(fact(s)) == 1 and str(s).count('1') > 4:
            print(j, s)
            t += 1
    if t == 5:
        break