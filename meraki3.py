def sum_average(num1, num2, num3):
    i=1
    c=0
    while i<=3:
        sum=num1+num2+num3
        c+=1
        i+=1
    print(sum)
    print(sum/c)
num1=int(input("enter a 1st number: "))
num2=int(input("enter a 2nd number: "))
num3=int(input("enter a 3rd number: "))
sum_average(num1, num2, num3)
