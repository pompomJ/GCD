def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            c = a % b
            a = c
        else:
            c = b % a
            b = c

    if a == 0 or b == 0:
        if a != 0:
            return a
        else:
            return b 


gcd = gcd(28, 42)
print("最大公約数は", gcd)
