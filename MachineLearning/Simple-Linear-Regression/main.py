import pandas
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Read the dataset in
dataset = pandas.read_csv("Machine Learning A-Z (Codes and Datasets)/Part 2 - Regression/Section 4 - Simple Linear Regression/Python/Salary_Data.csv")


# Split into feature and dependent dataset  (Columns and rows)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# Split the dataset into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


# Make a prediction
regressor = LinearRegression()      # Create the Linear_Regression object
regressor.fit(x_train, y_train)     # Train the regressor with the training data
y_pred = regressor.predict(x_test)  # Make a prediction with the x_test dataset for y_test


# Create a linear regression of the training set
plt.scatter(x_train, y_train, color = "red")      # Draw the points of the training set  (x_train as x-coord and y_train as y-coord)
plt.plot(x_train, regressor.predict(x_train), color = "green")   # Create the predicted regression line
plt.title("True value vs Predicted (Training set)")     # Set the windows title
plt.xlabel("Years of experience")      # Set the x-axis label
plt.ylabel("Salary")        # Set the y-axis label
plt.show()         #show the window


# Create a linear regression of the test set
plt.scatter(x_test, y_test, color = "red")
plt.plot(x_test, regressor.predict(x_test), color = "green")
plt.title("True value vs Predicted (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
