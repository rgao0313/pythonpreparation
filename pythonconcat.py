import pandas as pd
import numpy as np
#concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
#ignore_index means to reshuffle the data index after merge
print(res)
ef1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
outjoin=pd.concat([df1,df2],join='outer')
#merge the data like a combination
print(outjoin)
innerjoin=pd.concat([df1,df2],join='inner')
#Only show the results of intersection columns between two data
print(innerjoin)
#join_axes
join_axes=pd.concat([df1,df2],axis=1,join_axes=[df1.index])
#if we do not use join_axes, all the data will be merged by index,
# if use,only use the chosen index to merge data,which means the index only appear in the other will be lost
print(join_axes)
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
append=df1.append(s1,ignore_index=True)
#we can only append vertically, horizontally append is not available
print(append)