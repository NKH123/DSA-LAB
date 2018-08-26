n=int(input("Enter n: "))
l=list()
def crlist(pos,N):
    if n%2==0:
        if pos==((n//2)-1):
            if n!=2:
                l.append(str(N))
            N=N+1*10**(pos+1)+1*10**(pos)
            l.append(str(N))
            N=N-1*10**(pos+1)-1*10**(pos)
            N=N+6*10**(pos+1)+9*10**(pos)
            l.append(str(N))
            N=N-6*10**(pos+1)-9*10**(pos)
            N=N+8*10**(pos+1)+8*10**(pos)
            l.append(str(N))
            N=N-8*10**(pos+1)-8*10**(pos)
            N=N+9*10**(pos+1)+6*10**(pos)
            l.append(str(N))
            return
    if n%2==1:
        if pos==((n//2)): 
            l.append(str(N))
            N=N+1*10**(pos)
            l.append(str(N))
            N=N-1*10**(pos)
            N=N+8*10**(pos)
            l.append(str(N))
            return
    N=N+1*(10)**(n-pos-1)+1*(10)**(pos)
    crlist(pos+1,N)
    N=N-1*(10)**(n-pos-1)-1*(10)**(pos)
    N=N+6*(10)**(n-pos-1)+9*(10)**(pos)
    crlist(pos+1,N)
    N=N-6*(10)**(n-pos-1)-9*(10)**(pos)
    N=N+8*(10)**(n-pos-1)+8*(10)**(pos)
    crlist(pos+1,N)
    N=N-8*(10)**(n-pos-1)-8*(10)**(pos)
    N=N+9*(10)**(n-pos-1)+6*(10)**(pos)
    crlist(pos+1,N)
crlist(0,0)
print (l)
