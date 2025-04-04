import numpy
from scipy import stats
import matplotlib.pyplot as plt
import pandas
from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import sys
import matplotlib
matplotlib.use("Agg")


"""
Data Types

three main categories:
* Numerical: numbers
    * Discrete: limited to integers
    * Continuous: any number
* Categorical: values that cannot be measured up against each other
* Ordinal: can be measured up against each other
"""

"""
* Mean - The average value
* Median - The mid point value
* Mode - the most common value
"""

#mean()
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

#median()
x = numpy.median(speed) # 87
print(x)
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed) # (86 + 87 / 2)
print(x)

#mode()
x = stats.mode(speed)
print(x)

#Standard Deviation std()
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)
speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)

#Variance
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

#Percentiles
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)
x = numpy.percentile(ages, 90)
print(x)

#Data Distribution
x = numpy.random.uniform(0.0, 5.0, 100000)
#plt.hist(x, 100)
#plt.show()

#Normal Data Distribution
x = numpy.random.normal(5.0, 1.0, 10000)
#plt.hist(x, 100)
#plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
#plt.scatter(x, y)
#plt.show()

#Linear regression
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
#plt.scatter(x,y)
#plt.plot(x, mymodel)
#predict
speed = myfunc(10)
print(speed)
#relationship range -1 to 1, where 0 means no relationship
print(r)
#plt.show()

#Polynomial Regression
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)

#relationship
print(r2_score(y, mymodel(x)))
#plt.scatter(x,y)
#plt.plot(myline, mymodel(myline))
#plt.show()

#Multiple Regression
df = pandas.read_csv("data.csv")
X = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedC02 = regr.predict([[2300, 1300]])
print(predictedC02)
print(regr.coef_)

#Scale
scale = StandardScaler()
scaledX = scale.fit_transform(X)
print(scaledX)

regr.fit(scaledX, y)
scaled = scale.transform([[2300, 1.3]])
predictedC02 = regr.predict([scaled[0]])
print(predictedC02)

#Train/Test
#Train the model means create the model
#Test the model means test the accuracy of the model
numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0,6,100)
r2 = r2_score(train_y, mymodel(train_x))
print(r2)
r2 = r2_score(test_y, mymodel(test_x))
print(r2)
print(mymodel(5)) #predict values
#plt.scatter(x, y)
#plt.scatter(train_x, train_y)
#plt.scatter(test_x, test_y)
#plt.plot(myline, mymodel(myline))
#plt.show()

#Decision Tree
df = pandas.read_csv("data2.csv")
print(df)
d = {'UK' : 0, 'USA':1,'N':2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES' : 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
tree.plot_tree(dtree, feature_names=features)

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()