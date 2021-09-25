#Euclid's algorithm
#Approach: Suppose d divides both m and n
# m - n = (a -b)*d
#d divides m - n as well


def gcd(m,n):

    large = max(m,n)
    small = min(m,n)

    if large%small == 0:
        return small
    else:
        return gcd(small, large-small)

print(gcd(12,36))            