#Boolean variable example code
#Boolean values can be computed, assigned and passed around like numerical values

def divides(m, n):

    if n % m == 0:
        return True
    else:
        return False  

def even(n):
    return(divides(2, n))

def odd(n):
    return(not divides(2, n)) 

print(even(67))
print(odd(67))     