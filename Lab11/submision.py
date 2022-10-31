"""
@ Author : Anirudh Sathish 
@ Roll_No : CS20B1125 

"""

"""
Write a Python program (with pandas) to do the following on the
 data file “landslide_data2_miss.csv”.
a) Plot a graph of the attribute names (x-axis)
 with the number of missing values in them (y-axis).(separate python file)
b) Target attribute is “stationid”, 
Drop the tuples (rows) having missing values in the target attribute.
Print the total number of tuples deleted.
 Delete (drop) the tuples (rows) having equal to
or more than one third of attributes with missing values.
 Print the total number of tuples deleted.
c) After (b), count and print the number of missing values
 in each attributes. 
Also find and print the total number of missing values in the file
 (after the deletion of tuples)

2. Experiments on filling in missing values: 
a) Replace the missing values by mean of their respective attribute.
    Compute the mean, median, mode and standard deviation for 
    each attributes and compare the same with that of the original file.
    Calculate the root mean square error (RMSE) between the
    original and replaced values for each attribute.
    Compute RMSE given by the equation at the end of the question.
    Plot these RMSE with respect to the attributes. 
b) Replace the missing values in each attribute using the
   linear interpolation technique. Use df.interpolate() with
   suitable arguments.
   Compute the mean, median, mode and standard deviation 
   for each attributes and compare with that of the original file.
   Calculate the root mean square error (RMSE) between the original and replaced values for each attributes. (Get original values from the original file provided). Compute RMSE given by the equation at the end of the question. Plot this RMSE with respect to the attributes.
c) Outlier detection:
	i) After replacing the missing values by interpolation method,
	find and list the outliers in the attributes “temperature” and “rain”.
	Outliers are the values that do not satisfy the condition 
	(Q1 – (1.5 * IQR)) < x < (Q3 + (1.5 * IQR)),
 	where x is the value of the attribute, IQR is the interquartile range,
	Q1 and Q3 are the first and third quartiles.
 	Obtain the boxplot for these attributes.

ii) Replace these outliers with the median of the attribute.
 	Plot the boxplot again and observe the difference with that
 	of the boxplot from the previous box in 
 	(i). Do you still get outliers? Why?
"""

# Defining the neccesary header files 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import math
from statistics import median

# Opening the neccesary file 
missing_landslide_data = pd.read_csv("landslide_data3_miss.csv")
print(missing_landslide_data.info())

# (a) Plotting the missing values vs Attributes
missing_val = missing_landslide_data.isnull()
missingWithColumn = missing_val.sum()
fig = plt.figure(figsize = (10, 5))

values = missingWithColumn.to_list()

missingWithColumn = missingWithColumn.to_frame() 
# creating the bar plot
plt.bar(missingWithColumn.index ,values, color ='blue',
        width = 0.4)
 
plt.xlabel("Attributes")
plt.ylabel("Missing Value Count")
plt.title("Missing Values corresponding to attributes")
plt.show()

clean_targetAttribute  = missing_landslide_data[missing_landslide_data["stationid"].notnull()]
print(clean_targetAttribute.info())

# Initial number of tuples 
tuple_inital = missing_landslide_data.shape[0]

# Tuple after drop 
tuple_afterDrop = clean_targetAttribute.shape[0]

tuple_difference = tuple_inital - tuple_afterDrop
print("\n")
print("---------------------------------------------------------")
print("Rows Deleted after removing NAN values from :" , tuple_difference)
print("---------------------------------------------------------")
print("\n")

""" 
Removing values where the no of null values in a tuple is equal to
or more than third of the attributes
"""
update_clean_targetAttribute = clean_targetAttribute.dropna(thresh = 7 , axis = 0 )
print(update_clean_targetAttribute.info())

Final_update_tuple = update_clean_targetAttribute.shape[0]
new_diff = tuple_afterDrop - Final_update_tuple
print("\n")
print("---------------------------------------------------------")
print("Difference after Removing Tuples with too many NAN values : ",new_diff)
print("Total Tuples Deteleted : ",new_diff+tuple_difference)
print("---------------------------------------------------------")
print("\n")

# Answer to the C Part 
""" 
    TO FIND THE REMAINING MISSING VALUES AFTER ALL THE CLEANING 
 """
print("\n")
print("---------------------------------------------------------")
print("TO FIND THE REMAINING MISSING VALUES AFTER ALL THE CLEANING ")
Final_missing_val = update_clean_targetAttribute.isnull()
FinalMissingColumnWise = Final_missing_val.sum()
print("Column wise Missing Values :\n" ,FinalMissingColumnWise)
FinalMissing = FinalMissingColumnWise.sum()
print("Final Missing Values : " , FinalMissing)


""" 2. Experiments on filling in missing values: 
    a) Replace the missing values by mean of their respective attribute.
     (Use df.fillna() with suitable arguments.)"""
missing_landslide_data.info()
# Sinces dates and stationid are not of numerical type , let us ignore
# these values for now 

# Reading the file
missing_landslide_data = pd.read_csv("landslide_data3_miss.csv")

# Dropping all non numerical kind of data 
missing_landslide_data_numero = missing_landslide_data.drop(['dates','stationid'],axis =1)

# Filling the missing values in this data with thier means 
df_FilledWithMean = missing_landslide_data_numero.fillna(missing_landslide_data_numero.mean())

#Obtaining the statistics 
df_descrip_Mean_Fill = df_FilledWithMean.describe()

# Obtaining the neccesary statistics by dropping unnecessary values 
df_descrip_Mean_Fill = df_descrip_Mean_Fill.drop(['count','min','25%','50%','75%','max'],axis = 0)

# Obtaining the median 
df_descrip_median_fill = df_FilledWithMean.median()

# Converting into df
df_descrip_median_fill = df_descrip_median_fill.to_frame()

#Transposing it for better represenation 
df_descrip_median_fill = df_descrip_median_fill.transpose()

# Renaming 
df_descrip_median_fill = df_descrip_median_fill.rename(index={0:'Median'})

#Obtaining the mode 
df_descrip_mode_fill = df_FilledWithMean.mode()
df_descrip_mode_fill = df_descrip_mode_fill.rename(index={0:'Mode'})

# Concatenating all , to represent mean , median , mode and std together 
df_fromIncomplete_v1 = pd.concat([df_descrip_Mean_Fill,df_descrip_median_fill,df_descrip_mode_fill])
print(df_fromIncomplete_v1)

""" For the originial file  , with no missing values """
# Reading the file 
df_original = pd.read_csv("landslide_data3_original.csv")

# Dropping non numerical data 
df_original_data_numero = df_original.drop(['dates','stationid'],axis =1)

# Finding mean and std 
df_Originaldescrip_Mean_Fill = df_original_data_numero.describe()
df_Originaldescrip_Mean_Fill = df_Originaldescrip_Mean_Fill.drop(['count','min','25%','50%','75%','max'],axis = 0)

# Finding median 
df_Originaldescrip_median_fill = df_original_data_numero.median()
df_Originaldescrip_median_fill = df_Originaldescrip_median_fill.to_frame()
df_Originaldescrip_median_fill = df_Originaldescrip_median_fill.transpose()
df_Originaldescrip_median_fill = df_Originaldescrip_median_fill.rename(index={0:'Median'})

#Finding mode 
df_Originaldescrip_mode_fill = df_original_data_numero.mode()
df_Originaldescrip_mode_fill = df_Originaldescrip_mode_fill.rename(index={0:'Mode'})

# Concatenating All to represent them together 
df_fromComplete_v1 = pd.concat([df_Originaldescrip_Mean_Fill ,df_Originaldescrip_median_fill,df_Originaldescrip_mode_fill])
print(df_fromComplete_v1)

""" 
    TO LOOK AT DIFFERENCE BETWEEN MEAN , MEDIAN , MODE AND STD OF THE
    MEAN REPLACED VALUE WITH THE ORIGINAL FILE VALUES 
"""
print("\n")
print("--------------------------------------------------------")
print(""" 
    TO LOOK AT DIFFERENCE BETWEEN MEAN , MEDIAN , MODE AND STD OF THE
    MEAN REPLACED VALUE WITH THE ORIGINAL FILE VALUES 
""")
df_new_v1_diff = df_fromComplete_v1 - df_fromIncomplete_v1
print("Difference between values : ")
print(df_new_v1_diff)
print("--------------------------------------------------------")
print("\n")

""" Function to find RMSE 
    I : Mean , Dataframe , InstanceCount
    O : Dataframe Containg RMSE Value of Attributes
"""
def FindRMSE(df_original, df_replaced ,N ):
    sum = 0 
    for i in range(N):
        x_i = df_original.loc[i]
        x_hat_i = df_replaced.loc[i]
        val = x_i - x_hat_i
        squared_term = val*val
        sum =sum + squared_term

    sum = sum.to_frame()
    sum = sum.transpose()
    columns_list = list(sum.columns)

    RMSE_list = []
    for column in sum.columns:
        Req_Name = "RMSE_"+column
        RMSE_list.append(math.sqrt(sum[column]/N))
    
    RMSE = pd.DataFrame(RMSE_list)
    RMSE = RMSE.transpose()
    RMSE.columns = columns_list
    RMSE = RMSE.transpose()
    RMSE.columns = ['RMSE']

    return RMSE
    

# Do the RMSE Cacluations 

# To find the total instance count 
N = df_original_data_numero.shape[0]
print(N)

RMSE_V1 = FindRMSE(df_original_data_numero,df_FilledWithMean,N)
print(RMSE_V1)

# Plotting a bar graph 
fig = plt.figure(figsize = (10, 5))

RMSE_V1_calc = RMSE_V1.squeeze()

values_RMSE_V1 = RMSE_V1_calc.to_list()

plt.bar(RMSE_V1.index ,values_RMSE_V1, color ='blue',
        width = 0.4)
 
plt.xlabel("Attributes")
plt.ylabel("RMSE")
plt.title("RMSE Values of Attributes")
plt.show()


# Doing the neccesary using interpolate

# Performing linear interploation 
df_Interpolated_missing_landslide_data = missing_landslide_data_numero.interpolate(method="linear")

# Finding the mean and std 
df_describe_std_mean = df_Interpolated_missing_landslide_data.describe()
df_describe_std_mean = df_describe_std_mean.drop(['count','min','25%','50%','75%','max'],axis = 0)
df_median = df_Interpolated_missing_landslide_data.median()
df_median = df_median.to_frame()
df_median = df_median.transpose()
df_median = df_median.rename(index={0:'Median'})
df_mode = df_Interpolated_missing_landslide_data.mode()
df_mode = df_mode.rename(index={0:'Mode'})
df_fromInterpolate_v2 = pd.concat([df_describe_std_mean,df_median,df_mode])
print(df_fromInterpolate_v2)


"""
    Difference between the values after Linear interpolation
"""
df_fromComplete_v2 = df_fromComplete_v1
df_new_v2_diff = df_fromComplete_v2 - df_fromInterpolate_v2
print("\n")
print("--------------------------------------------------------------")
print("Difference between the values after Linear interpolation : \n")
print(df_new_v2_diff)
print("--------------------------------------------------------------")
print("\n")

# Finding the RMSE

RMSE_V2 = FindRMSE(df_original_data_numero,df_Interpolated_missing_landslide_data,N)
print(RMSE_V2)

# Bar graph plot
fig = plt.figure(figsize = (10, 5))

RMSE_V2_cal = RMSE_V2.squeeze()

values_RMSE_V1 = RMSE_V2_cal.to_list()

plt.bar(RMSE_V2.index ,values_RMSE_V1, color ='blue',
        width = 0.4)
 
plt.xlabel("Attributes")
plt.ylabel("RMSE")
plt.title("RMSE Values of Attributes")
plt.show()

""" 
    Plotting the box plot to identify outliers
"""
plt.figure(figsize=(10,6))
# Temperature boxplot
df_Interpolated_missing_landslide_data.boxplot("temperature")


plt.figure(figsize=(10,6))
# Rain box plot
df_Interpolated_missing_landslide_data.boxplot("rain")

"""
    To find IQR 
    Returns : LowerBound , UpperBound
    """
def iqrCalculation(df):
    Quantile1 = df.quantile(0.25)
    Quantile3 = df.quantile(0.75)

    # Finding the iqr 
    InterQuantileRange = Quantile3-Quantile1
    median_value = df.median()

    # Defining the upper and lower bounds
    upper_bound = Quantile3+(1.5*InterQuantileRange)
    lower_bound = Quantile1-(1.5*InterQuantileRange)

    return upper_bound,lower_bound,median_value

# Finding the upper and lower bounds pf the outliers for temperature
upper_bound ,lower_bound,median_temperature = iqrCalculation(df_Interpolated_missing_landslide_data["temperature"])
# Finding the outliers in temperature 
outliers_temperature = df_Interpolated_missing_landslide_data["temperature"][(df_Interpolated_missing_landslide_data["temperature"] <= lower_bound) | (df_Interpolated_missing_landslide_data["temperature"] >= upper_bound)]
print('Outliers in Temperature  :\nIndex Temperature \n{}'.format(outliers_temperature))
outliers_temperature_list = outliers_temperature.to_list()

# For Rain
# Finding the upper and lower bounds pf the outliers for temperature
upper_bound ,lower_bound ,median_rain = iqrCalculation(df_Interpolated_missing_landslide_data["rain"])

outliers_rain = df_Interpolated_missing_landslide_data["rain"][(df_Interpolated_missing_landslide_data["rain"] <= lower_bound) | (df_Interpolated_missing_landslide_data["rain"] >= upper_bound)]
print('Outliers in Rain  :\nIndex    Rain \n{}'.format(outliers_rain))
outliers_rain_list = outliers_rain.to_list()

# Replacing outliers in temperature with median
df_Interpolated_missing_landslide_data["temperature"].replace(outliers_temperature_list,median_temperature,inplace= True)

#Replacing outliers in rain with median
df_Interpolated_missing_landslide_data["rain"].replace(outliers_rain_list,median_rain,inplace= True)

# Now drawing the boxplot for temperature
plt.figure(figsize=(10,6))
df_Interpolated_missing_landslide_data.boxplot("temperature")

print(median_temperature,median_rain)

# Now drawing the boxplot for rain
plt.figure(figsize=(10,6))
df_Interpolated_missing_landslide_data.boxplot("rain") 

""" There is a change in the number of outliers , i.e ,
 initially the outliers in rain Ranged upto 8000 , but currently
 they have come down to ranges like 2500
 But they havent truly dissapeared , this is because median
 is not a true measure of data
 """