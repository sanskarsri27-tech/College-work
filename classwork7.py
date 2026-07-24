# Import the Linear Regression model from scikit-learn
from sklearn.linear_model import LinearRegression


import numpy as np


#  Linear Regression 

# Training data (House size in square feet)
# X = [[1000], [1200], [1500], [1800]]

# Target values (House prices in lakhs)
# y = [40, 50, 65, 80]

# Create a Linear Regression model
# model = LinearRegression()


# model.fit(X, y)

# Predict the price of a house with area 1600 sq. ft.
# prediction = model.predict([[1600]])

# Display the predicted price
# print("Predicted price:", prediction[0], "lakh")


#  K-Means Clustering 

# Import the KMeans clustering algorithm
from sklearn.cluster import KMeans

# Create a dataset 2D array
data = np.array([
    [2, 3],
    [3, 4],
    [10, 12],
    [11, 13]
])

#  KMeans model with 2 clusters
# random_state ensures the same result every time the program runs
model = KMeans(n_clusters=2, random_state=42)


model.fit(data)

# Display the cluster assigned to each data point
print("Cluster Labels:")
print(model.labels_)