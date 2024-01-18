n=0
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
while n<=10:
    print(factorial(n))
    n+=1
    
    