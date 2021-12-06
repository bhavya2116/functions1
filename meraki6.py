def speed_driver(speed):
    if speed<70:
        print("ok")
    elif speed>70:
        minus=speed-70
        point=minus/5
        print(point)
        if point>12:
            print("license suspended")            
speed=int(input("enter speed: "))
speed_driver(speed)



