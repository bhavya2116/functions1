def string_lenght(first, second):
    if len(first)>len(second):
        print(first)
    elif len(first)==len(second):
        print(first,second)
    else:
        print(second)
first=input("enter any string: ")
second=input("enter anything: ")
string_lenght(first, second)
