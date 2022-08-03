#write a program for vote elgibile for above 18 year
'''
age=int(input("enter your age:"))
if age==18 or age>=18:
    print("your eligible")
else:
    print("your not eligible")'''
'''electricity bill print
0-50=2/- ,51-150=3/-,151-250=5/-,251 and above=8/- per unit
total bill+20% charges'''
u=int(input("enter units:"))
if u<=50:
    total_bill=u*1.95
elif u==51 and u<=150:
    total_bill=u*3
elif u==151 and u<=250:
    total_bill=u*5
else:
    total_bill=u*8 
charges=(20/100)*total_bill
print(total_bill+charges)


