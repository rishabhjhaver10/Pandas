import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

#Creating a Data Frame with training data using read_csv to read a csv file.
df_train = pd.read_csv('train.csv')

#Printing the head and tail to see the first and last five values in the Data Frame.
df_train.head()
df_train.tail()

#Getting the mean of all the values column wise.
df_train.mean()

#Getting the summary of statistics using the describe() function.
df_train.describe()

#Now we will visualize all the data by plotting graphs for each variable.

#For Survival variable, 1 = survived and 0 = did not survive
survived = df_train['Survived'].value_counts()
print 'The number of people survived: ' + str(survived[1])
print 'The number of people did not survive: ' + str(survived[0])
#Plotting the results.
plt.figure() 
survived.plot.bar(title = 'Survival Count')
plt.show()

#For Passenger class, there are three value 1, 2, and 3
passenger_class = df_train['Pclass'].value_counts()
print 'The number of people belonging to first class: ' + str(passenger_class[1])
print 'The number of people belonging to second class: ' + str(passenger_class[2])
print 'The number of people belonging to third class: ' + str(passenger_class[3])
#Plotting the results
plt.figure()
passenger_class.plot.bar(title = 'Passenger Class')
plt.show()

#For Sex, there are two values male and female
#For data analytics we will convert male = 1 and female = 0
#sex = df_train['Sex'].value_counts()
df_train['Gender'] = df_train['Sex'].map({'female': 0, 'male' : 1}).astype(int)
gender = df_train['Gender'].value_counts()
print 'The number of males: ' + str(gender[1])
print 'The number of females: ' + str(gender[0])
#print 'The number of males: ' + str(sex[0])
#print 'The number of females: ' + str(sex[1])
#Plotting the results
plt.figure()
gender.plot.bar(title = 'Gender')
plt.show()

#For Embarked, there are three values, C = Cherbourg; Q = Queenstown; S = Southampton
df_train['Embarked'] = df_train['Embarked'].fillna('Zero')
df_train['Embarked 1'] = df_train['Embarked'].map({'Zero' : 0, 'C' : 1, 'Q' : 2, 'S' : 3}).astype(int)
embarked = df_train['Embarked'].value_counts()
embarked1 = df_train['Embarked 1'].value_counts()
print 'The number of people embarked from Southampton: ' + str(embarked[0])
print 'The number of people embarked from Queenstown: ' + str(embarked[1])
print 'The number of people embarked from Cherbourg: ' + str(embarked[2])
#Plotting the results
plt.figure()
embarked1.plot.bar(title = 'Port of Embarkment')
plt.show()

#For Age, minimum age is a few months and maximum age is 80.
fill_value = df_train['Age'].median()
#For missing values of age we will use the median of age
df_train['Age'] = df_train['Age'].fillna(fill_value)
#Plotting the results
plt.figure()
plt.axis([0, 80, 0, 350])
df_train['Age'].plot.hist(title = 'Histogram for Age')