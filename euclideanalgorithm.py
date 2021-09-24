# Greatest Common Denominator and Least Common Multiple using the Euclidean Algorithm

# Greatest Common Denominator of two integers (a, b)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Least Common Multiple of two integers (a, b)
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

