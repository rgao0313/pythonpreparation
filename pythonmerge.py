import pandas as pd

#merging two df by key/keys.(may be used in database)
#simple example
left=pd.DataFrame({'key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
print(left)
print(right)
res=pd.merge(left,right,on='key')
#res=pd.merge(left,right,on=['key1','key2'],how='inner')
#default is how ='inner'. it can be how='outer',how='right',how='left'
print(res)
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
out=pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
# the default ignore index, if you wanna use index ,you can declear it as .merge(left,right,left_index=True）

print(df1)
print(df2)
print(out)

#differentiate data from different belongings
boys=pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls=pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
dif=pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='outer')
print(dif)