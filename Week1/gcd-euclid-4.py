#Previous approach using while loop
#For this approach, time taken is proportional to number of digits

def gcd(m,n):
    large = max(m,n)
    small = min(m,n)

    while(large%small != 0):
        r = large%small
        large, small = max(small, r), min(small, r)

    return small

print(gcd(12,36))        