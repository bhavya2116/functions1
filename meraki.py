# def check_numbers_list (a, b):
#     i=0
#     while i<len(a):
#         if a[i]%2==0 and b[i]%2==0:
#             print("dono even hain")
#         else:
#             print("dono even nhi hain")
#         i=i+1
# check_numbers_list(a=[2, 3, 6, 8], b=[12, 9, 5, 20])

i=1
while i<=1000:
    j=1
    sum=0
    while j<i:
        if i%j==0:
            sum=sum+j
        j+=1
    if sum==i:
        print(i)
    i+=1
    