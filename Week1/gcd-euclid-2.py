#Euclid's algorithm with while loop
#Time taken is proportional to the input numbers
#Suppose gcd(101,2) is given as output to gcd-euclid-2.py
#It will take about 50 steps to get the answer

def gcd(m,n):

    large = max(m,n)
    small = min(m,n)

    while(large%small != 0):
        diff = large - small
        large, small = max(small, diff), min(small,diff)

    return small    

print(gcd(12,36))        
