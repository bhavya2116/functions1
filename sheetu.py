water=int(input("add water: "))
if water<1:
    print("water needs to fill")
elif water>=1 and water<=10:
    print("no need to fill water")
else:
    print("overflow")
    
