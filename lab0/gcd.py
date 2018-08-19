def gcd(a,b):
    if a>b:
        temp=a
        a=b
        b=temp
    if a==0:
        return b
    else:
        return gcd(b%a,a)

a,b=map(int,input("Enter two numbers:").split(" "))
print (gcd(a,b))
        