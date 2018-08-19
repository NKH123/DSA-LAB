def isprime(n):
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return 0
    return 1


print (isprime(n=int(input('Enter number:'))))
