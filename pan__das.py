import pandas as pd 
import numpy as np 
#the pandas series and data frame objects 
#1- creating series objects from a list or array
# data=pd.Series([12,15,20,30,40,25])
# ar_ray=np.array([12,15,20,30,40,25])
# print(data)
# print('-------------------------')
# print(ar_ray)
# #convert data of series to numpy array
# num_pyarray=data.values #لتحويل الداتا من باندس الي ننباي اراي
# print('++++++++++++++++++++++++++++')
# print(num_pyarray)
# print(data[3]) #لاستخراج اندكس في مكان معين 
# #custom indexing تغير الندكس الي الاول الثاني وهكذا 
# data=pd.Series([10,11,12,30,15,60],index=['first','second','third','fourth','fifth','sixth'])
# print(data)
# es=pd.Series([10,11,12,30,15,60],index=[5,6,7,8,10,12]) #لو عاوز تغير في ترتيب الاندكس
# print(es)
# dictioray={'cairo':5000, #تحويل الدكشنري الي سيرز
#            'alex':1000,
#            'menufia':2000}
# dd=pd.Series(dictioray)
# print(dd)
# print(dd['cairo':'alex'])
#1- creating data frame  
#يمكن انشاءها بعدة طرق 
#1-from pandas dictionary
# area={'cairo':50,
#       'alex':10,
#       'menufia':20}
# da_ta=pd.DataFrame({'popoulation':dictioray,'Area':area})
# print(da_ta)
# #2-from python dictionary 
# d_ata=pd.DataFrame({'population':[5000,1000,2000],'Area':[50,10,20]},index=['cairo','alex','giza'])
# print(d_ata)
# print(d_ata.index)
# print(d_ata.columns)
# print(d_ata['Area'])
# print(d_ata['Area']['cairo'])
#3-from a single series object
# print(pd.DataFrame(area,columns=['Area']))
# print(pd.DataFrame({'Area':area}))
# print(pd.DataFrame([{'a':1,'b':2},{'b':1.5,'c':2}])) #when some key are missing
# #4-from a two dimensional numpy array 
# arr=np.random.randint(1,20,30).reshape(10,3)
# print(pd.DataFrame(arr,columns=['Ahmed','Eslam','Mostafa']))
# #3-indexing and selection 
df=pd.read_csv('ramenratings.csv')
#print(df.head()) #لعرض اول خمس صفوف في الملف 
#print(df.head(10)) #لعرض اول 10 صفوف في الملف 
#print(df['Country']) #لعرض عمود معين 
#print(df.Brand) #لعرض عمود معين 
#استخلاص الداتا بطرقتين 
#1-index(index based selection) وهي اسم راس العمود 
# print(df.iloc[0,:]) #لعرض الصف الاول وكل الاعمدة
# print(df.iloc[:,0]) #لعرض العمود الاول وكل الصفوف 
# print(df.iloc[:3,:]) #لعرض اول ثلاث صفوف 
# print(df.head(3)) #لعرض اول 3 صفوف في الملف طريقة اخري 
# print(df.iloc[:,-1]) #لعرض اخر عمود 
# print(df.iloc[:,-2]) #لعرض العمود قبل الاخير د  
# #Fancy indexing يعني لو عاوز الصف الاول والرابع والخمسين 
# print(df.iloc[[1,4,50],:]) 
# print(df.iloc[-10:,:]) # لعرض اخر 10 صفوف     
 #2-label(label based selection) وهي عن طريق رقم الصف ورقم العمود او اسمهم
# print(df.loc[:,['Brand','Style','Stars']]) #لعرض اعمدة معينة
# #Difrance between iloc , loc
# print(df.loc[1:4]) #الصف الرابع هيدخل معانا 
# print(df.iloc[1:4]) #الصف الرابع مش  هيدخل معانا 
# print(df.set_index('Review #')) #لو عاوز تغير الاندكس بتاع الداتا تخليه يبدا من عمود معين 
# df_1=df.set_index('Review #')
# print(df_1.iloc[0:3,:])
# print(df_1.loc[2580:2578,:]) #وهنا هيظهر الفرق اكتر 
#4-Conditional Selection & Assigning
# لاستخراج داتا معينةو تستخدم في تحليل وفهم الداتا 
# print(df['Country']=='Taiwan') # لاستخراج دولة تايوان وهتجيب ترو و فولس
# Df_Taiwan=df.loc[df['Country']=='Taiwan']
# print(Df_Taiwan) # لاستخراج دولة تايوان
# print(df.loc[df['Stars']=='Unrated']) #لاستخراج الداتا الغير مصنفه
# df_Rated=Df_Taiwan.loc[Df_Taiwan['Stars']!='Unrated'] #لاستخراج الداتا المصنفه
# print(df_Rated) #لاستخراج الداتا المصنفه
# df_Rated.Stars=df_Rated.Stars.astype(float) # لتحويل الداتا الي فللوت 
# print(df_Rated.Stars)
# print(df_Rated[df_Rated.Stars > 2.5])
# #لو عاوز اعملها علي طول من غير ماقعد احفظ في متغيرات اعملها من  الداتا الاصلية 
# #الحل هو الconditional selection logical operators & | ~ and or not 
# df=df.loc[df['Stars']!='Unrated']
# df.Stars=df.Stars.astype(float) #unrated لتحويل الدتا ال فلووت ولازم تشيل الاسماء مثل 
# print(df.loc[(df.Country=='Taiwan') & (df.Stars> 2.5)])
# #لو عاوز عمود معين 
# print(df.loc[(df['Country']=='Taiwan')& (df['Stars']> 2.5),['Brand','Style','Country']])
# #لو عاوز تستخرج الداتا من بلدين مخلتلفين 
# print(df.loc[df.Country.isin(['Finland','Sweden'])]) # لاستخراج دولتين  فينلدوهسوليد
# #لو عاوز الصفوف اللي من افضل عشرة 
# print(df.loc[~df['Top Ten'].isnull()]) #~ notمعناها 
# print(df.loc[df['Top Ten'].notnull()]) #طريقة اخري 
# #ِ#ِ Assigning Data
# #df['Brand']='Hi' #لو عاوز تبدل مالعمود بكلمة هاي
# #print(df['Brand'])
# df['is style cup']=df['Style']=='Cup'  #لو عاوز تعمل عمود جديد
# print(df)
# # الي 1و2و3و4و  Review # لو عاوز اغير العمود 
# df['Review #']=list(range(1,2578))
# print(df)
# #'طريقة اخري 
# df.loc[:,['Review #']]=list(range(1,2578))
# print(df)
#5-Handing missing values
#  في الداتا واعملها هندله nan value لو عاوز اتعرف علي p
print(df.isnull().sum(axis=0)) #  axis =0 علشان nan value هنا بنعرض الاعمدة  اللي فيها 
print(df.shape) #هنا بيطلع الداتا كام صف وكام عمود
print((df.isnull().sum(axis=0)/df.shape[0])*100) #  لو عاوز اطلع نسبة مئوية للقيم النل 
print(df.dropna()) #لحدف الصفوف اللي فيها نان فاليو
print(df.dropna(axis='columns')) #لحدف الاعمدة اللي فيها نان فاليو
print(df.dropna(subset=['Brand'])) # لحدف الصفوف اللي فيها نان فاليو في العمود براند فقط 
print(df.dropna(subset=['Style'])) # لحدف الصفوف اللي فيها نان فاليو في العمود استايل فقط 
print(df.dropna(subset=['Style','Top Ten'])) # لحدف الصفوف اللي فيها نان فاليو في العمود استايل و توب تين فقط 
print(df.fillna(0)) # لتعويض الصفوف اللي فيها نان فاليو في الداتا بصفر 
df_1=df.fillna(0)
print(df.loc[df.Style.isnull()])  #لو عاوزين نتاكد من صحة الداتا اللي اتغيرت 
print(df_1.loc[df_1.Style==0])
print(df.fillna({'Style':'Eslam','Top Ten':-2})) #لتعويض الداتا في عمود الاستايل بكلمة والعمود توب تين برقم
df_2=df.fillna({'Style':'Eslam','Top Ten':-2})
print(df_2.loc[df_2.Style=="Eslam"]) #لتاكد من ان القيم اتغيرت في العمود استايل 
print(df_2.iloc[[2152,2442],:]) #اظهارهم هنا برقم الصف وكل الاعمدة 
print(df['Style'].value_counts())  #هتعطينا هنا كل قيمة اتكررت كام مرة في العمود استايل 
print(df['Stars'].value_counts())  #هتعطينا هنا كل قيمة اتكررت كام مرة في العمودستارز 
df.Stars=df.Stars.replace('Unrated', np.nan) #هنا هنبدل الغير مقيم بالقيمة نان علشان نقدر نحذفها 
print(df['Stars'].value_counts())  #  هتعطينا هنا كل قيمة اتكررت كام مرة في العمودستارز بس في نفس القيم محسوبة مش مع بعض 
df.dropna(subset=['Stars'],inplace=True) #inplace = true علشان اعوض الداتا الاصلية بهذه القيم
df.Stars=df.Stars.astype(float) #كده احنا حولنا العمود ده اللي فلووت علشان اعرف اهندله 
print(df)
print(df['Stars'].value_counts())  #  هتعطينا هنا كل قيمة اتكررت كام مرة في العمودستارز وكل القيم هتجمع مع المتسابه علشان انا حوت الداتا الي فلووت








