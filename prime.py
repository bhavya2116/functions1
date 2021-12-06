def prime(n):
    i=1
    fac=0
    while i<=n:
        if n%i==0:
            fac=fac+1
        i+=1
    if fac==2:
        print(n)
def find_prime():
    i=1
    while i<=50:
        prime(i)
        i+=1
find_prime()

