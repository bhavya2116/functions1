def My_fun():
    pick_up=input("enter your pick-up point: ")
    where_to=input("enter where you've go: ")
    distance=int(input("enter the distance from your place"))
    options=['Ubergo','UberAuto', 'Premier','UberXL', 'GoSedan']
    i=0
    while i<len(options):
        print((options[i]))
        i+=1
    select_cab=input("Choose your Ride: ")
    confirmation=input("are you going to confirm: ")
    if confirmation=="confirm":
        print("Your cab will reach soon")
        destination=input("did you reach to your destination: ")
        if destination==where_to:
            print("You've reached: ")
        total_payment=distance*5
        print("Total amount ",total_payment)
        pay=int(input("please pay: "))
        if pay==total_payment:
            print("thank you")
            # rate=[1, 2, 3, 4, 5]
            # j=0
            # while j<len(rate):
            #     print(rate[i])
            #     j+=1
            # give_rate=int(input("enter rate to ride: "))
            # rating=0
            # # while rating<len(rate):
        # def New_function():
        while True:
            again=input("if you want more rides press yes or no: ")
            if again=="yes":
                My_fun()
            break

        # New_function()
My_fun()


