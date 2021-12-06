def calculator(num1, num2, operator):
    if operator=='+':
        add=num1+num2
        return add
    elif operator=='*':
        multy=num1*num2
        return multy
    elif operator=='-':
        substract=num1-num2
        return substract
    elif operator=='/':
        devide=num1/num2
        return devide
num1=int(input("enter a number: "))
num2=int(input("enter a number: ")) 
operator=input("enter any operator: ")
a=calculator(num1, num2, operator)
print(a)
def list_change (l1, l2):
    i=0
    a=[]
    while i<len(l1):
        Multy=calculator(l1[i],l2[i],"*")
        i+=1
        a.append(Multy)
    return a
New_list=list_change(l1=[5, 10, 50, 20],l2=[2, 20, 3, 5])
print(New_list)



