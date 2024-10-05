import numpy as np
from sklearn.linear_model import LinearRegression

# This is linear regression implemented using the Scikit-Learn library
# uses linear regression to predict values, returns an array
def linearRegressionSKL(data):
    # linear regression variables for episodes
    x = np.array(range(1, len(data)+1)).reshape(-1, 1) # dependent variables
    y = np.array(data).reshape(-1, 1) # independent variables

    regr = LinearRegression()

    # fit a linear regression model to the data
    regr.fit(x, y)

    # display information about the model
    displayInfo(x, y, regr)

    # create an array of dependent variables predicted by the model
    # used for graphing the linear regression line later
    return regr.predict(x)

# displays linear regression information
def displayInfo(x, y, regr):
    print("Linear Regression Coefficients:", regr.coef_)
    print("Linear Regression Intercept:", regr.intercept_)
    print("R-Squared for Linear Regression Model:", regr.score(x, y)) 
    print(f"R-Squared Accuracy by %: {regr.score(x, y)*100:.2f}")