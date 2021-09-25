#Find all factors of a number

def factors(n):
    flist = []

    for i in range(1, n+1):

        if n % i == 0:
            flist = flist + [i]
    return flist           #in for loop we know exactly how many times it will be executed


from datetime import datetime
start = datetime.now()

print(factors(1000))
print('time taken :', datetime.now()-start)

