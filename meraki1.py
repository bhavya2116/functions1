# def first_function():
#     s = 'I love India'
#     def second_function():
#         s="MY NAME IS JACK"
#         print(s)     
#     second_function()
#     print(s)    
 
# first_function()
def perfect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i+=1
    if sum==num:
        print("Perfect number",num)
def perfect_num():
    i=1
    while i<=1000:
        perfect(i)        
        i+=1
perfect_num()
