  
# Importing essential libraries


import pickle
from pandas import read_excel


df = read_excel('Ran.xlsx')
df.set_index('Date', inplace = True)
print(df.head(15))

df = df.drop(columns = ['AT', 'Temp', 'RH', 'SR', 'Toluene', 'NH3', 'Ozone', 'SO2', 'CO', 'WD', 'Xylene'])

x=df.iloc[:,:-1] #independent features
y=df.iloc[:,-1]   #dependent features

from sklearn.ensemble import ExtraTreesRegressor

model=ExtraTreesRegressor()
model.fit(x,y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor()
regressor.fit(x_train,y_train)

prediction=regressor.predict(x_test)



# Creating a pickle file for the classifier
filename = 'regressor.pkl'
#pickle.dump(regressor, open(filename, 'wb'))
pickle.dump(regressor, open(filename, 'wb'))