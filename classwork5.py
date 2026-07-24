import numpy as np
import pandas as pd

#some mathematical functions of pandas
# print(np.sqrt(a))
# print(np.abs(a))
# print(np.exp(a))
# print(np.log(a))
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))

# print(np.random.randint(1,100,(2,2)))
# print(np.random.randint(1,70,50)

#data of employees using pandas
# salary= np.random.randint(20000,200000,50)
# print("salary in sorted way(before increment):",np.sort(salary))
# print("------------------------------------------------------")
# a=np.max(salary)
# b=np.min(salary)
# c=np.mean(salary)
# diff=a-b
# inc=salary+ 0.1
# print("\nmaximum salary is:",a)
# print("------------------------------------------------------")
# print("\nminimum salary is:",b)
# print("------------------------------------------------------")
# print("\naverage of salary is:",c)
# print("------------------------------------------------------")
# print("\ndiff between max and min:",diff)
# print("------------------------------------------------------")
# print("\nsalary after increment:",np.sort(inc))
# print("------------------------------------------------------")
# d=np.max(inc)
# e=np.min(inc)
# dif=d-e
# print("\n",dif)
# print("------------------------------------------------------")


#creating data frames using csv files
# data = {
#     'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Math': [85, 90, 78, 92, 88],
#     'Science': [88, 85, 90, 87, 91],
#     'English': [90, 88, 85, 90, 89],
#     'History': [85, 90, 88, 85, 90],
#     'Geography': [90, 85, 90, 88, 87]
# }
# df = pd.DataFrame(data)
# print("Student Marks:")
# print(df)
# print("\nMaximum marks in each subject:")
# print(df[['Math', 'Science', 'English', 'History', 'Geography']].max())
# print("\nAverage marks in each subject:")
# print(df[['Math', 'Science', 'English', 'History', 'Geography']].mean())

# se=pd.Series([1,2,3,4,5,6],index=["q","w","e","r","t","y"])
# print(se)
df=pd.read_csv("employees_50.csv")
print(df)
print("------------------------------------------------------------------------------------------")

students={
    "name:":["a","b","c"],
    "roll:":[21,22,23],
     "age:":[23,18,19],
     "marks:":[23,45,67]
}
df= pd.DataFrame(students)
print(df)
df.to_csv("save.csv", index=True)

# print(df.head(2)) 
# print("------------------------------------------------------------------------------------------")
# print(df.tail(2)) 
# print("------------------------------------------------------------------------------------------")
# print(df.shape) 
# print("------------------------------------------------------------------------------------------")
# print(df.columns) 
# print("------------------------------------------------------------------------------------------")
# print(df.index) 
# print("------------------------------------------------------------------------------------------")
# print(df.info()) 
# print("------------------------------------------------------------------------------------------")
# print(df.describe())
# print("------------------------------------------------------------------------------------------")

# df=pd.read_excel("employees_50.xlsx")
# print(df)
