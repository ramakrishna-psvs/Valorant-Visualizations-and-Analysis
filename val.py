import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import requests

csv_path='Players.csv'
df=pd.read_csv(csv_path, nrows=20)
df.head()
df_new=df.iloc[:, [1,6,7,8]]
df_new
print(df_new)
print("-----------------------------------------------------------------")


nam=df_new['Player']
ear=df_new['Earnings']
gam=df_new['Won']


#earnings
plt.barh(ear,nam,height=0.6,color='blue')
for index, value in enumerate(nam):
    plt.text(value, index,
             str(value))
plt.title("Top 20 Valorant Players and the money they made - April 2022")
plt.ylabel("Earnings")
plt.xlabel("Names")
plt.show()

#tournmentswon
plt.barh(nam,gam,color='orange', height=0.6)
for index, value in enumerate(gam):
    plt.text(value, index,
             int(value))
plt.title("Top 20 Valorant Players and the number of tournaments they won - April 2022")
plt.ylabel("Earnings")
plt.xlabel("Tournaments Won")
plt.show()

#split
na=len(df_new[df_new['Region']== 'North America'])
eu=len(df_new[df_new['Region']== 'EMEA'])

print("NA:", na)
print("EMEA:", eu)

y=np.array([na,eu])
mylabels=["NA", "EMEA"]
mycolours=["Cyan","Yellow"]

plt.pie(y, labels= mylabels, colors=mycolours, autopct='%.1f%%', explode=(0,0.1), 
wedgeprops={'linewidth': 3.0, 'edgecolor': 'black'}, textprops={'size': 'x-large', 'color':'black'}, shadow=True)
plt.title("The Split")
plt.legend(title="People:")
plt.show()

#part2
csv_path='Teams.csv'
df=pd.read_csv(csv_path, nrows=20)
df.head()
df_new1=df.iloc[:, [1,6,7,8]]
df_new1
print(df_new1)
print("-----------------------------------------------------------------")

tem=df_new1['Team']
eart=df_new1['Earnings']
gamt=df_new1['Won']


#earnings
plt.barh(eart,tem,height=0.6,color='blue')
for index, value in enumerate(tem):
    plt.text(value, index,
             str(value))
plt.title("Top 20 Valorant Players and the money they made - April 2022")
plt.ylabel("Earnings")
plt.xlabel("Teams")
plt.show()

#tournmentswon
plt.barh(tem,gamt,color='orange', height=0.6)
for index, value in enumerate(gamt):
    plt.text(value, index,
             int(value))
plt.title("Top 20 Valorant Players and the number of tournaments they won - April 2022")
plt.ylabel("Earnings")
plt.xlabel("Tournaments Won")
plt.show()

#split
na=len(df_new1[df_new1['Region']== 'North America'])
eu=len(df_new1[df_new1['Region']== 'EMEA'])
apac=len(df_new1[df_new1['Region']== 'APAC'])
kr=len(df_new1[df_new1['Region']== 'Korea'])
jp=len(df_new1[df_new1['Region']== 'Japan'])
lt=len(df_new1[df_new1['Region']== 'Latam'])

print("NA:", na)
print("EMEA:", eu)
print("APAC:", apac)
print("KOREA:", kr)
print("JAPAN:", jp)
print("LATAM:", lt)

y=np.array([na,eu,apac,kr,jp,lt])
mylabels1=["NA","EMEA","APAC","Korea","Japan","Latam"]
mycolours=["Cyan","Yellow", "Green", "Grey","Red", "Pink"]
myexplode = [0,0,0,0,0,0]
plt.pie(y, labels=mylabels1, colors=mycolours, autopct='%.1f%%',explode=myexplode,
wedgeprops={'linewidth': 1.0, 'edgecolor': 'black'}, textprops={ 'color':'black', 'fontsize':'10','verticalalignment':'bottom'}, shadow=True)
plt.title("The Split")
plt.legend(title="Team Regions:")
plt.show()