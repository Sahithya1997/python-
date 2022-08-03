'''p=int(input("enter princple value:"))
t=int(input("enter time:"))
r=int(input("enter rate of intrest:"))
compound_intrest=p*(1+(r/100))**t
print(compound_intrest)
'''
import pandas as pd
name="sandel"
prices=500
deliverys="free delivery"
Brand="xxxx"
l1=[123,4,5,6]
sandel=[name,prices,deliverys,Brand]

df=pd.DataFrame(sandel,index=["name","price","delivery","Brand"])
df.to_csv('sandal_data.csv')
print(df)


