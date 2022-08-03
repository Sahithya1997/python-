from datetime import datetime
room=[]
food=[]
wifi=[]
Total=0

name1='sahithya'
password=12345
name=input("enter your name:")
password_1=int(input("enter your password:"))
our_services='''
1.room
2.food
3.wifi'''
if name1==name and password==password_1:
    print(our_services)
select=int(input("enter your option:"))
if select==1:
    print("1.roomA=1000 rs \n"
    "2.roomB=800 rs \n"
    "3.roomC=500 rs \n")
    select_1=int(input("enter your option:"))
    if select_1==1:
        room.append(1000)
        print(room)
    elif select_1==2:
        room.append(800)
        print(room)
    elif select_1==3:
        room.append(500)
        print(room)

select2=int(input("for our services to continue,press2: \n"
"press3 for exit:" ))
if select2==2:
    print(our_services)
select=int(input("enter you otion:"))
if select==2:
    print("1.rice=100 rs \n"
    "2.tiffin=50 rs \n"
    "3.snacks=50 rs \n")
    select_2=int(input("enter your option:"))
    if select_2==1:
        (food.append(100))
        print(food)

    elif select_2==2:
        food.append(50)
        print(food)
    elif select_2==3:
        food.append(50)
        print(food)
else:print("exit")
select2=int(input("for our services to continue,press2: \n"
"press3 for exit:" ))
if select2==2:print(our_services)
select=int(input("enter your option:"))
if select==3:
    wifi.append(100)
    print(wifi)
price=room+food+wifi
print(price)
total=sum(price)
gst=(5/100)*total
finalamount=total+gst
int1=input("if you want bill generate press yes or no")
if int1=='yes':
    if total!=0:
        print(25*"=","sahithya Hotel",25*"=")
        print(25*"","Dharmapuri")
        print("Name:",name,30*"","date:",datetime.now())
        print(75*"-")
        print("sno",30*"","services",30*"","price")
        print("1.",30*"","room",30*"",room)
        print("2.",30*"","food",30*"",food)
        print("3.",30*"","wifi",30*"",wifi)
        print(75*"-")
        print(60*"","totalamount:","rs",total)
        print("gst amount",40*"","gst rs",gst)
        print(75*"-")
        print(50*"","finalamount:","rs",finalamount)
        print(75*"-")
        print(30*"","Thanks for visiting")
        print(75*"-")








    

