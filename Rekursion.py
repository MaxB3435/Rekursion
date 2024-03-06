
def fact_rec(n):
    if n==1:
        return n
    else:
        return n*fact_rec(n-1)

#print(fact_rec(4))

def har_rec(n):
    if n==1:
        return n
    else:
        return 1/(n) + har_rec(n-1)
    
#print(har_rec(3))

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1,15):
    print(fib(i))
