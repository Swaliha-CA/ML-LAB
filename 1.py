import pandas as pd
import matplotlib.pyplot as plt

'''s=pd.Series([1,3,5,7,9])
print(s)
print()

s=pd.Series ([1,3,5,7,9],index=['a','b','c','d','e'])
print(s)
print()


data={'Name':['Alice','Bob','Charlie'],
    'Age':[20,50,70],
    'city':['Tokyo','china','Jammu']}
    
print(data)
print()'''


data={"year":[2015,2016,2017,2018,2019,2020],
    "Sales":[200,250,300,350,400,450]}
df=pd.DataFrame(data)

df.plot(x="year",y="Sales",kind="line",title="yearly sales" )

plt.show()
    






