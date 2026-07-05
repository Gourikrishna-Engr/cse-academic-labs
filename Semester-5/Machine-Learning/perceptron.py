# Training

# Load the data
x = [[1, 1], [2, 2], [5, 5], [1, 4]]
y = ["chem", "phy", "chem", "phy"]

# Load the model
from sklearn.linear_model import Perceptron

r = Perceptron()

# Fit data into model
r.fit(x, y)

# Testing
op = r.predict([[2, 8]])

print(op)