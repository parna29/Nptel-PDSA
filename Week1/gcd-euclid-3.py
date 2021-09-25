#Previous approach not feasible
#New approach: m = qn + r -> ad = q(bd) + r -> r also divisible by d

def gcd(m,n):
    large = max(m,n)
    small = min(m,n)

    if large%small == 0:
        return small

    else:
        return gcd(small, large%small)

print(gcd(12,36))            
