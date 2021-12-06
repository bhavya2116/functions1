def prime (pos):
    i=1
    c=1
    while pos>=0:
        j=1
        fac=0
        while j<=i:
            if i%j==0:
                fac=fac+1
            j+=1
        if fac==2:
            if pos==c:
                print(i)
            c+=1
        i+=1
pos=int(input("enter position: "))
prime(pos)


