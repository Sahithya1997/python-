#lists in Python
L=[1,2.2,'python',True,[1,1,2,2]]
'''
for i in L:
    print(i)'''
'''
print(L[1])
print(L[4][3])
#slicing[start:stop:skip]
print(L[1:4:2])
print(L[:2])
print(L[2:])
print(L[:5])'''
#methods
L.append([1,2])
print(L)
L.extend([2,3])
print(L)
L.copy()
print(L)
L.insert(0,[1,2,3])
print(L)
L.reverse()
print(L)
L.remove(2)#item delated
print(L)   #index value delated
L.pop(0)
print(L)
L.sort() #ascending Order
print(L) 
L.sort(revrse=True) #descending Order
print(L)
L.clear()
print(L)

