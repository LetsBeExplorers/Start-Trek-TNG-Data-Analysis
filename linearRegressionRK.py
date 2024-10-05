# this is linear regression as implemented by myself
def linearRegressionRK(data):
    
    # sum of all data
    # dependent variables
    sumData = sum(data)
    
    # array for item indices: 1-based
    # independent variables
    numData = list(range(1, len(data)+1))

    # sums of squares of indices
    sumSqrdIndex = sumSquared(numData)

    # sum of independent variables
    sumIndexNums = sum(numData)

    # create array of independent times dependent variables
    dataTimesIndex = [a * b for a, b in zip(numData, data)]

    # sum of multiplied data
    sumMultiplied = sum(dataTimesIndex)

    # calulcate means of data
    meanData = calculateMean(sumData, len(numData))
    meanIndex = calculateMean(sumIndexNums, len(numData))

    # calculate linear regression line and display information
    slope = calculateSlope(sumIndexNums, sumData, len(numData), sumSqrdIndex, sumMultiplied)
    intercept = calculateIntercept(meanIndex, meanData, slope)
    print("Linear Regression Coefficient:", slope)
    print("Linear Regression Intercept:", intercept)

    # calculate an array of predicted values for the dependent variable
    predict = []
    for num in numData:
        predict.append(slope*num + intercept)

    # get and print R-Squared statistic
    rSquared = calculateRSquared(data, predict, meanData)
    print("R-Squared for Linear Regression Model:", rSquared)
    print(f"R-Squared Accuracy by %: {rSquared*100:.2f}")

    return predict

# sum numbers in an array and return sum
def sum(array):
    sum = 0

    # add each number to the sum
    for x in array:
        sum += x
    return sum

# square numbers in an array and return sum
def sumSquared(array):
    sum = 0

    # add each number to the sum
    for x in array:
        sum += x**2
    return sum

# calculates the slope of a linear regression line   
def calculateSlope(x, y, n, x2, xy):
    top = (n*xy - x*y)
    bottom = (n*x2 - x**2)
    return top/bottom

# calculates the intercept of a linear regression line
def calculateIntercept(meanX, meanY, b):
    return (meanY - b*meanX)

# calulates the mean
def calculateMean(sum, n):
    return sum/n

# calculates R-Squared for a given linear regression model
def calculateRSquared(y, predY, meanY):
    # array of the differences between the y values and the predicted y values
    diffYPred = [a - b for a, b in zip(predY, y)]
   
    # array of the differences between the y values and the mean y value
    diffYMean = [meanY - a for a in y]

    # setup variables to hold the sums
    predSum = 0
    meanSum = 0

    # get sum of squares of differences
    for num in diffYPred:
        predSum += num**2

    for num in diffYMean:
        meanSum += num**2

    return (meanSum-predSum)/meanSum
    

