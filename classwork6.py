# Import the required libraries
import matplotlib.pyplot as plt   # Used for creating graphs and charts
import pandas as pd             
import numpy as np               


#  Reading and Filtering Data

# Read the CSV file
# df = pd.read_csv("null.csv")

# Display the complete dataset
# print(df)

# Filter employees whose salary is greater than 40000 and department is HR
# print("--------------------------------Filtering Data------------------------------------------")
# print(df[(df["Salary"] > 40000) & (df["Department"] == "HR")])

# Sort the data by Salary in descending order
# print("--------------------------Sorting Data------------------------------------------------")
# print(df.sort_values("Salary", ascending=False))

#  Employee_ID 

# print(df.rename(columns={"Employee_ID": "ID"}))

# Display statistical summary of the dataset
# print(df.describe())


# DataFrame Operations

# Read employee dataset
# df = pd.read_csv("employee_data_20_rows.csv")

# Display the complete dataset
# print(df)

# Display the first 3 rows
# print("--------------------------------------------------------------------------")
# print(df.head(3))

# Display the last 3 rows
# print("--------------------------------------------------------------------------")
# print(df.tail(3))

# Display the number of rows and columns
# print("--------------------------------------------------------------------------")
# print(df.shape)

# Display column names
# print("--------------------------------------------------------------------------")
# print(df.columns)

# Display row indexes
# print("--------------------------------------------------------------------------")
# print(df.index)

# Display dataset information 
# print("--------------------------------------------------------------------------")
# print(df.info())


# print("--------------------------------------------------------------------------")
# print(df.describe())

# Sort data by ID in descending order
# print("--------------------------------------------------------------------------")
# print(df.sort_values("ID", ascending=False))

# Calculate total salary 
# print("--------------------------------------------------------------------------")
# total = df.groupby("Department")["Salary"].sum()
# print(total)



# Read dataset containing missing values
# df = pd.read_csv("null.csv")

# Display the dataset
# print(df)


# print("--------------------------------------------------------------------------")
# print(df.isnull())

# Count missing values in each column
# print("--------------------------------------------------------------------------")
# print(df.isnull().sum())

# Replace missing values with 0
# print("--------------------------------------------------------------------------")
# print(df.fillna(0))

# Replace missing values with the string "Unknown"
# print("--------------------------------------------------------------------------")
# print(df.fillna("Unknown"))

# Replace missing values in Salary column with the column's mean
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df)


# ----------------------------- Reading Another Dataset -----------------------------

# Read a dataset containing 1000 people's records
# df = pd.read_csv("1000_people.csv")

# Display the dataset
# print(df)


# ----------------------------- Simple Line Graph -----------------------------

# x-axis values
# x = [1, 3]

# y-axis values
# y = [10, 15]

# Plot the line graph
# plt.plot(x, y)

# Display the graph
# plt.show()


#  Different Types of Charts 

# Employee names
# emp = ["Ram", "Shyam", "Geeta", "Seeta"]

# Employee salaries
# sal = [160000, 250000, 470000, 300000]

# Smaller salary values (for testing)
# sal = [16000, 25000, 47000, 30000]

# Create a 3×5 NumPy array for image display
# data = np.array([
#     [10, 21, 45, 67, 89],
#     [21, 54, 87, 98, 54],
#     [34, 29, 58, 71, 99]
# ])

# Draw a line graph
# plt.plot(emp, sal, linewidth=2, linestyle="-.", color="black",
#          marker="x", label="A")

# Draw another line graph with a different label
# plt.plot(emp, sal, linewidth=2, linestyle="-.", color="black",
#          marker="x", label="B")

# Draw a vertical bar chart
# plt.bar(emp, sal, color="orange")

# Draw a horizontal bar chart
# plt.barh(emp, sal, color="orange")

# Draw a pie chart
# plt.pie(sal, labels=emp)

# Draw a scatter plot
# plt.scatter(emp, sal)

# Draw a histogram
# plt.hist(emp)

# Display the NumPy array as an image
# plt.imshow(data)

# Display color scale for the image
# plt.colorbar()

# Label the x-axis
# plt.xlabel("Employees names")

# Label the y-axis
# plt.ylabel("Salary")

# Add a title to the graph
# plt.title("Yearly salary")

# Display the legend
# plt.legend()

# Show the final graph
# plt.show()