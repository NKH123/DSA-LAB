def gcd(a,b):
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if a>b:
        t=a
        a=b
        b=t
    if a==0:
        return b

    else:
        return gcd(b%a,a)





class Fraction:

    def __init__(self,num,den):
        
        t=gcd(num,den)
        self.num=num//t
        self.den=den//t


    def inverse(self):
        """Returns the inverse of this Fraction"""
        return Fraction(self.den,self.num)

    def add(self,f):
        """Adds the Fraction f to this Fraction and returns the result"""
        num1=self.den*f.num+self.num*f.den
        den1=self.den*f.den
        return Fraction(num1,den1)

    def subtract(self,f):
        """Subtracts the Fraction f from this Fraction and returns the result"""
        num1=self.num*f.den-self.den*f.num
        den1=self.den*f.den
        return Fraction(num1,den1)

    def multiply(self,f):
        """Multiplies the Fraction f to this Fraction and returns the result"""
        num1=self.num*f.num
        den1=self.den*f.den
        return Fraction(num1,den1)

    def divide(self,f):
        """Divides the Fraction f from this Fraction and returns the result"""
        num1=self.num*f.den
        den1=self.den*f.num
        return Fraction(num1,den1)
        

    def __str__(self):
        """Returns a string representation of this fraction"""
        return (str(self.num)+"/"+str(self.den))

def main():
    f1 = Fraction(2,3)
    print ('Fraction 1 is', f1)
    f2 = Fraction(3,4)
    print ('Fraction 2 is', f2)
    print ('The inverse of f1 is', f1.inverse())
    print ('The inverse of f2 is', f2.inverse())
    print ('f1+f2 is', f1.add(f2))
    print ('f1-f2 is', f1.subtract(f2))
    print ('f1 * f2 is', f1.multiply(f2))
    print ('f1 / f2 is', f1.divide(f2))

if __name__ == '__main__':
    main()
