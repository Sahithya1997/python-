#loops
#print 1st n even numbers
'''n=int(input("enter no:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)'''
#prime number
n=int(input())
fact=0
for i in range(2,n):
    if n%i==0:
        fact=fact+1
if fact==0:
        print("prime number")
else:
        print("not prime number")