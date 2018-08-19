def bub(a):
    for i in range(len(a)):
        for j in range(1,len(a)):
            if(a[j]<a[j-1]):
                temp=a[j]
                a[j]=a[j-1]
                a[j-1]=temp
    print ("This sorted array is:",end=" ")
    print (a)

a=list(map(int,input("Enter array elements: ").split()))

bub(a)

 
