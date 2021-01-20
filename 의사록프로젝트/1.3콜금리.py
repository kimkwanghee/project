
import pandas as pd
import datetime
from datetime import timedelta
df= pd.read_csv('call_rate1.csv')
def daycopy(n):
    n1 = datetime.datetime.strptime(n,'%Y.%m.%d')
    time1 = n1 - timedelta(28)
    return time1
df['date2'] = df['날짜'].apply(daycopy)
#print(df.index)
call_2=[]
for i in range(28,len(df['콜금리'])+28):
    if i >= len(df['콜금리']) :
        call_2.append(0)
    else:
        call_2.append(df['콜금리'][i])
df["call2"]=call_2
up_down=[]
def up_down_call():
    for i in range(len(df['콜금리'])):
        if df["콜금리"][i]>df["call2"][i]:
            up_down.append('up')
        elif df["콜금리"][i]==df["call2"][i]:
            up_down.append('same')
        else:
            up_down.append('down')
up_down_call()
df["up_down"]=up_down
a=[]
for i in range(2837,2865):
    a.append(i)
df.drop(a,inplace=True)
print(df)
#2839 2866
# df_concat = pd.concat([df,df_t] ,axis=1)
# #df_concat
# df_concat=pd.DataFrame(df_concat)
# df_concat.to_csv('df_concat.csv',encoding='utf-8')