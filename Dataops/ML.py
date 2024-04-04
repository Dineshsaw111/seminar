import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score
# from sklearn.preprocessing import PolynomialFeatures
 
 
print("------ START --------- ")
dataFrame = pd.read_csv("./youtube_data.csv")
print('\n\n\n',dataFrame.head())
print('\n\n\n Continue ')
print('\n\n\n',dataFrame.describe())
print('\n\n\n Continue ')
 
x1 = dataFrame[['Likes']]
y1 = dataFrame[['Views']]
plt.plot(x1,y1)
plt.show()
 
x1_train,x1_test,y1_train,y1_test = train_test_split(x1,y1,test_size=0.33,random_state=20)
 
regression=linear_model.LinearRegression()
regression.fit(x1_train,y1_train)
print("\n\n Coefficient :\n\n\t",regression.coef_,"\n\t",regression.intercept_)
 
testing = regression.predict(x1_test)
meanSquare = np.mean((testing-y1_test)**2)
print("\n\n Mean Square Error is {0}",format(meanSquare))
r2_score = r2_score(testing,y1_test)
print("\n\nR2 Score is : {0}",format(r2_score))
print("\n\n\n-------- END ----------")
n=int(input('enter no. of likes: '))
new_likes = np.array([[n]]) 
expected_views = regression.predict(new_likes)

print("Expected views for likes:")
for i in range(len(new_likes)):
    print(f"Likes: {new_likes[i][0]}, Expected Views: {int(expected_views[i][0])}")