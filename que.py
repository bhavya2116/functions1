def add_numbers(num1,num2):
    a=num1+num2
    print(a)
num1=56
num2=12
add_numbers (num1,num2)

def add_numbers_list(a,b):
    i=0
    while i<len(a):
        sum=a[i]+b[i]
        i+=1
        print(sum)
add_numbers_list(a=[50,60,70],b=[10, 20,13])

