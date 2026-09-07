def divisors(n):
    primes = []
    x = n
    if x % 2 == 0:
        primes.append(2)
        while x % 2 == 0:
            x //= 2
    p = 3
    while p * p <= x:
        if x % p == 0:
            primes.append(p)
            while x % p == 0:
                x //= p
        p += 2
    if x > 1:
        primes.append(x)
    if len(primes) < 2:
        return 0
    return primes[-1] - primes[0]
def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
def counter(n):
    return str(n).count('1') >= 4
n = 8117600757
c = 0
res = []
while c < 5:
    m = divisors(n)
    if m > 0 and prime(m) and counter(m):
        res.append((n, m))
        c += 1
    n += 1
for num, m in res:
    print(num, m)
