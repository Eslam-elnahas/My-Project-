#6-Combining Data Frames
import pandas as pd 
import numpy as np
import seaborn as sns #مكتبة يتوفر فيها مجموعة من الداتا سيت المتنوعة 
item_cat=pd.read_csv('item_categories.csv')
item=pd.read_csv('items.csv')
shops=pd.read_csv('shops.csv')
sales_train=pd.read_csv('sales_train.csv')
print(item_cat.head())
print(item.head())
print(item_cat.iloc[40])
##داتا هنجرب عليها الدمج بالطرق الاربعة 
a=pd.DataFrame({'Cat name':['Elec','Games','Kitchen'],'cat id':[0,1,2]}) #لانشاء داتا فريم 
b=pd.DataFrame({'item name':['mackbook','paintaing','cup'],'item id':[0,1,2],'cat id':[0,5,2]})
print(a)
print(b)
c=pd.merge(a,b,how='inner',on='cat id') #1-inner join
print(c)
d=pd.merge(a,b,how='outer',on='cat id') #2-outer join
print(d)
e=pd.merge(a,b,how='right',on='cat id') #3-right join
print(e)
f=pd.merge(a,b,how='left',on='cat id')  #4-left join
print(f)
f=pd.merge(a,b,how='left',on='cat id')  #4-left join
print(f)
print(pd.merge(item_cat,item,how='right',on='item_category_id'))
merge1=pd.merge(item_cat,item,how='right',on='item_category_id')
merge2=pd.merge(merge1,sales_train,how='right',on='item_id')
print(merge2)
merge3=pd.merge(merge2,shops,how='right',on='shop_id') #لدمج المحلات بالمبيعات يجب دمج اول اتين مع بعض ثم دمجعهم مع المبيعات ثم دمجهم مع المحلات 
print(merge3)
left=pd.DataFrame({'key':['foo','bar'],'val':[1,2]})
right=pd.DataFrame({'key':['foo','bar'],'val':[4,5]})
print(left)
print(right)
l_r=pd.merge(left,right,how='inner',on='key') 
print(l_r)
l_r=pd.merge(left,right,how='inner',on='key',suffixes=('__from left','__from right')) #لتغيير اسم العمود المشترك علي حسب الرغبة 
print(l_r)
left=pd.DataFrame({'eslam':['foo','bar'],'val':[1,2]})
right=pd.DataFrame({'mostafa':['foo','bar'],'val':[4,5]})
ll_rr=pd.merge(left,right,how='inner',left_on='eslam',right_on='mostafa',suffixes=('__from left','__from right')) #لتغيير اسم العمود المشترك علي حسب الرغبة 
print(ll_rr) #لربط عموديين مخلفيين قي الاسماء 
ll_r=pd.merge(left,right,how='inner',left_on='eslam',right_on='mostafa',suffixes=('__from left','__from right')).drop(columns='mostafa')
print(ll_r)# drop(columns)لو عاوز تحذف عمود من اللي فوق تعمل 
print(left.join(right,how='outer',lsuffix='_from left',rsuffix='_from right'))#'صيغة اخري لعمل ربط 
#indexcesالجوين مشابه جدا للميرج ولكن الجوين بتربط  علي ال
#لو عاوز اخلي العمود كيي هو العمود الاول 
lef=pd.DataFrame({'key':['foo','bar'],'val':[1,2]})
righ=pd.DataFrame({'key':['foo','bar'],'val':[4,5]})
lef=lef.set_index('key')
righ=righ.set_index('key')
print(lef)
print(righ)  #الربط هيكون علي العمود الاول 
print(lef.join(righ,how='outer',lsuffix='_from left',rsuffix='_from right'))#'صيغة اخري لعمل ربط 
#7-ِAggregations & Groupby 
#Common aggregation functions in pandas:
# sum(): Calculates the total sum of values.
# mean(): Calculates the average of values.
# median(): Calculates the median (middle value) of values.
# min(): Finds the minimum value.
# max(): Finds the maximum value.
# count(): Counts the number of non-null values.
# std(): Calculates the standard deviation.
# var(): Calculates the variance.
# first(),last(): First and Last item 
# Prod (): Product of all item 
print(sales_train.head())
print(sales_train['item_price'].mean()) #لمعرفة متوسط سعر السلع
print(sales_train['item_price'].sum()) #لمعرفة مجموع سعر السلع
print(sales_train[['item_price','item_cnt_day']].mean()) #   لمعرفة متوسط سعر السلع في هذين العمودين
print(sales_train.describe()) #لتعرف علي محتويات الداتا بصورة سريعة
print(sales_train.groupby('shop_id')[['item_price','item_cnt_day']].mean()) #الحصول علي متوسط مبيعات كل محل واسعارة 
print(sales_train.groupby(['shop_id','item_id'])[['item_price','item_cnt_day']].mean()) #الحصول علي متوسط مبيعات كل محل واسعارة 
print(sales_train.groupby(['shop_id','item_id'])[['item_price','item_cnt_day']].mean().reset_index())
print(sales_train.groupby('shop_id')['item_price'].count()) #هنا هيعد كل محل عنده كام منتج
print(sales_train.groupby('shop_id')['item_price'].first()) #هنا بيجيب اول منتج اتكرر  
print(sales_train.groupby('shop_id')) #the out put ===> <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002324416C690>
#the soluation is for loop
for (shop__id,group) in sales_train.groupby('shop_id'):
    print(shop__id,group) #كده كاني عملت فصل للداتا كل محل اداني الدتا بتاعته علي حده 
print('////////////////////////////////////////////////////////////////')
#Aggregate Funcation
rng=np.random.RandomState(0)
Df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                 'Data1':range(6),
                 'Data2':rng.randint(0,10,6)},
                 columns=['key','Data1','Data2'])
print(Df)
print(Df.groupby('key').mean())
print(Df.groupby('key').aggregate([np.min,np.mean]))
print(Df.groupby('key').aggregate(['min','mean']))
print(Df.groupby('key').aggregate({'Data1':np.min,'Data2':np.max}))
#filter 
gp=Df.groupby('key')
for (key,group) in gp:
    print(key)
    print(group)

def filter_funcation (dataframe):
    return dataframe['Data2'].mean()<5
print(Df.groupby('key').filter(filter_funcation)) #   لان المتوسط بتاع الداتاc نلاحظ حذف الجروب 
def filter_fun (d):
    return d ['Data1'].mean()<2
print(Df.groupby('key').filter(filter_fun)) #  لان المتوسط بتاع الداتاc نلاحظ حذف الجروب 
#لحساب النسبة بين داتا 1وداتا 2
def ratio (dafarame):
    dafarame['ratio']=dafarame['Data1']/dafarame['Data2']
    return dafarame
print(Df.groupby('key').apply(ratio))
#8- Pivot tabels
Titanic=pd.read_csv('titanic.csv')
print(Titanic.head(10))
titanic=sns.load_dataset('titanic')
print(titanic)
print(titanic['sex'].value_counts()) #استخراج كم عدد القيم الموجودة في العمود 
print(titanic['who'].value_counts())
print(titanic.pivot_table(index='who',columns='class',values='age',aggfunc='mean'))
print(titanic.pivot_table(index='sex',columns='class',values='survived',aggfunc='mean'))
print(titanic.pivot_table(index='sex',columns='class',values='survived',aggfunc='count'))
print(titanic.pivot_table(index='who',columns='class',values=['age','survived'],aggfunc={'age':'mean','survived':'count'}))
print(titanic.pivot_table(index=['who','sex'],columns='class',values=['age','survived'],aggfunc={'age':'mean','survived':'count'}))
#9-Time Series
Mdf=pd.read_csv('Microsoft_Stock.csv')
print(Mdf.head())
print(Mdf.shape) #لمعرفة عدد صفوف واعمدة الداتا 
print(Mdf.info())
#print(Mdf.loc[0,'Date'].day_name())#Str هيجيب ايررو يقولس ان اسم اليوم ليس من النوع 
#date timeلذلك يجب تحويله الي نوع 
print(pd.to_datetime(Mdf['Date']))
# format يجب استخدام  day time اذا لم يتعرف علي نوع 
print(pd.to_datetime(Mdf['Date'],format='%m/%d/%Y %H:%M:%S'))
#لتعويض في الداتا الاصلية 
Mdf['Date']=pd.to_datetime(Mdf['Date'],format='%m/%d/%Y %H:%M:%S')
print(Mdf)
print(Mdf.loc[0,'Date'].day_name()) #اللي مكنتشي شغاله فوق
print(Mdf.loc[1,'Date'].day_name())
Mdf['Day of Week']=Mdf['Date'].dt.day_name()
print(Mdf)
print(Mdf['Date'].min()) #لمعرفة اقدم تاريخ في الداتا 
print(Mdf['Date'].max()) #لمعرفة احدث تاريخ في الداتا 
print(Mdf['Date'].max() - Mdf['Date'].min()) #لمعرفة عدد الايام بين التاريخين 
print(Mdf[Mdf['Date'] >'2020'])
print(Mdf[(Mdf['Date'] >'2020') & (Mdf['Date'] <'2021')])
print(Mdf[(Mdf['Date'] >='2020-01-01') & (Mdf['Date'] <='2020-12-31')])
print(Mdf.set_index('Date',inplace=True))
print(Mdf.loc['2020']) #index is Date ده نفع هنا علشان خلينا ال 
print(Mdf.loc['2020-02']['Close'].mean())
print(Mdf.loc['2020-02']['Close'].max())
print(Mdf.loc['2020-02']['Close'].plot())




















