import pandas as pd 
import numpy as np
df=pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
print(df.head())
print(df.info())
Data=df.iloc[:,-3:].values #.values =>  numpy array لتحويلها الي ِ
print(Data)
#Exercise & Soluations 
print('---Q1----')
##1-Find The number of dimensions,size and the shape of array ?
print(Data.ndim) #عدد الابعاد يعني الاري 
print(Data.shape) #كام فيي كام  
print(Data.size)  # 500*3=1500   حاصل ضرب الصفوف في العمدة 
print('---Q2----')
##2-what is the data type of this array ? 
print(Data.dtype) #نوع البيانات 
print('---Q3----')
##3-Return the target value of 500 observations .  #يعني عاوز اخر عمود اللي فيه مؤشر كتلة الجسم 
print(Data[:,-1])
print('---Q4----')
##4-Extract every 3 observations of data . #يعني عاوز صف وتسيب صفين وبعدين صف وتسيب صفين وهكذا 
print(Data[::3,:])
print('---Q5----')
##5-Extract the first and last columns in one array .(using hstack)
x=Data[:,0].reshape(500,1) #Reshape==> 2dعلشان احولها الي 
#x=Data[:,0].reshape(-1,1) #لو متعرفشي عدد الصفوف كام 
y=Data[:,-1].reshape(500,1)
#y=Data[:,-1].reshape(-1,1)
print(np.hstack([x,y]))
print('---Q6----')
##6-Reverse the array (the last observation become the first)
print(Data[::-1,:]) #لعكس الصفوف
print(Data[:,::-1]) #لعكس العمدة
print('---Q7----')
##7- What is the Minimum and  Maximum height?
print(5*6,''+'years old') #طريقة كتابة الحروف مع الارقام 
heights=Data[:,0]
min= np.min(heights)
print('Min : ', min ,' cm')
max= np.max(heights)
print('Max : ',max,' cm')
print('---Q8----')
##8- What is the Minimum and  Maximum weight?
weights=Data[:,1]
min1= np.min(weights)
print('Min : ', min1 ,' kg')
max1= np.max(weights)
print('Max : ',max1,' kg')
print('---Q9----')
##9-find the mean and standered deviation of height using the simple operations only (np.sum)
#حساب المتوسط والانحراف المعياري بالتفصيل 
heights=Data[:,0]
mean=np.sum(heights)/np.size(heights)
print('Mean for heights = ', mean)
diff=heights-mean
squared_diff=np.power(diff,2)
summ=np.sum(squared_diff)
n=np.size(heights)
squared_standered=summ/(n-1)
standered_deviation=np.sqrt(squared_standered)
print('standered_deviation for heights = ',standered_deviation)
print('---Q10----')
##10-find the mean and standered deviation of weight .
#حساب المتوسط والانحراف المعياري بالدوال مباشرة
weights=Data[:,1]
mean1=np.mean(weights)
print('Mean for weight = ', mean1)
std=np.std(weights)
print('standered_deviation for weight = ',std)
print('---Q11----')
##11-find the 25th and 75th percentile and the median of height 
f_perct=np.percentile(heights,25)
H_perct=np.percentile(heights,50)
s_perct=np.percentile(heights,75)
print(f_perct,H_perct,s_perct)
print(np.percentile(heights,[25,50,75]))
#50th percentile is the median 
median=np.median(heights)
print(median)
print('---Q12----')
##12-find the 25th and 75th percentile and the median of weight 
f_perct1=np.percentile(weights,25)
H_perct1=np.percentile(weights,50)
s_perct1=np.percentile(weights,75)
print(f_perct1,H_perct1,s_perct1)
print(np.percentile(weights,[25,50,75]))
#50th percentile is the median 
median1=np.median(weights)
print(median1)
print('---Q13----')
#13-Normalize height and weight 
normalized_height=(heights-mean)/standered_deviation
print(normalized_height)
normalized_weight=(weights-mean)/std
print(normalized_weight)
print('---Q14----')
##14-find min max scaler 
print((heights-np.min(heights)) / (heights.max() - heights.min()))
print('---Q15----')
##15-what are the indices of  the tallest people ?
print(np.argmax(heights)) #index لو القيمة اتكررت اكتر من مرة الدالة بترجع اول 
print('---Q16----')
##16-create two array representing the squared of both height and weight 
heights_squared=heights**2
weights_squared=weights**2
print(heights_squared,weights_squared)
print('---Q17----')
##17-create two array representing the square root of both height and weight 
heights_square_root=np.sqrt(heights)
weights_square_root=np.sqrt(weights)
print(heights_square_root,weights_square_root)
print('---Q18----')
##18-Extract the last column of the data (the target),what will be it's shape ?
bmi=Data[:,-1]
print(bmi,np.shape(bmi))
print('---Q19----')
##19-Make it a column vector 
print(np.reshape(bmi,(500,1)))
print(np.reshape(bmi,(-1,1)))#لو معرفشي عدد العناصر 
print('---Q20----')
##20-Make it a row vector
print(bmi.reshape(1,500)) 
print(bmi.reshape(1,-1))  #لو معرفشي عدد العناصر 





