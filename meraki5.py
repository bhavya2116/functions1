def multiple(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0:
            sum=sum+i
        elif i%5==0:
            sum=sum+i
        i+=1
    print(sum)
multiple(10)

