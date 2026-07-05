import pandas as pd

# Load the Excel (CSV) file
file = pd.read_csv(r"C:\Users\Gouri Krishna\Downloads\irisexcel (1).csv")

# Input features
x = file[["sepal_length", "sepal_width", "petal_length", "petal_width"]]

# Output
y = file[["species"]]

# Load the model
from sklearn.linear_model import Perceptron

r = Perceptron()

# Train the model
r.fit(x, y.values.ravel())

# Testing
op = r.predict([[1.5, 2.5, 3.5, 4.5]])

print(op)