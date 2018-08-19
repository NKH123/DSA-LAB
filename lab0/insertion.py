def insert(a):
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while(j>=0 and temp<a[j]):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
    print ("The sorted array is:",end=" ")
    print (a)


a=list(map(int,input("Enter array: ").split()))
insert(a)