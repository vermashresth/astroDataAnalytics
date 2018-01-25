# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

data=pd.read_csv("../input/exoTrain.csv")
print(data.shape)

#import keras
n=data.shape[1]
#import sklearn
dataxtrain=data.iloc[:int(n*.8),1:]
dataytrain=data.iloc[:int(n*.8),0]

dataxtest=data.iloc[int(n*.8):,1:]
dataytest=data.iloc[int(n*.8):,0]

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

regr = linear_model.LinearRegression()

regr.fit(dataxtrain,dataytrain)

dataypred=regr.pred(dataxtest)

print(mean_squared_error(dataytest, dataypred))



















# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


data=pd.read_csv("../input/exoTrain.csv")
datat=pd.read_csv("../input/exoTest.csv")
print(data.shape)
data.iloc[:,0]=data.iloc[:,0].apply(lambda x:(x%2+1)%2)
datat.iloc[:,0]=datat.iloc[:,0].apply(lambda x:(x%2+1)%2)
#import keras
n=data.shape[1]
#import sklearn
perc=.5
dataxtrain=data.iloc[:int(n*perc),1:]
dataytrain=data.iloc[:int(n*perc),0]
#dataxtrain=dataxtrain.div(dataxtrain.sum(axis=1), axis=0)
dataxtrain=scaler.fit_trainsform(scaler
print(dataxtrain)

dataxtest=data.iloc[int(n*perc):,1:]
dataytest=data.iloc[int(n*perc):,0]
#dataxtest=dataxtest.div(dataxtest.sum(axis=1), axis=0)


from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

regr = linear_model.LinearRegression()

regr.fit(dataxtrain,dataytrain)

dataypred=regr.predict(dataxtest)
dataypred=np.round(np.absolute(dataypred))
print(dataypred)
print(np.sum(dataytest==dataypred)/dataypred.shape[0])

dxt=datat.iloc[:,1:]
dyt=datat.iloc[:,0]
#dxt=dxt.div(dxt.sum(axis=1), axis=0)
dpt=regr.predict(dxt)
dpt=np.round(np.absolute(dpt))
print(np.sum(dpt==dyt)/dpt.shape[0])
