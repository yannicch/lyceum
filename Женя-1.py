def f(x):
    i = 2
    d = []
    while i * i <= x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 1
    d.append(x)
    return d


def pr(x):
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            return False
    return True


k = 0
for i in range(8117600757, 100000000000):
    a = f(i)
    m = max(a) - min(a)
    if str(m).count('1') < 3 and pr(m):
        print(i, m)
        k += 1
        if k == 5:
            break
