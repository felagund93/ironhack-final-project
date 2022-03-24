#Linear Regression Model of the CoVid Data
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')

from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler, Normalizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

import streamlit as st

data = pd.read_csv('../ML_models/data_for_ML.csv').drop('Unnamed: 0',axis=1)

data['year']=data['year'].astype(str)
data['week']=data['week'].astype(str)

ncd=['year','week','geoId','cmltve_cases','cmltve_first_dose','cmltve_second_dose','cmltve_deaths']
data_accum=data[ncd]

data_accum.drop('cmltve_second_dose', axis=1, inplace=True)

#Preprocessing
# X-y Split
y = data_accum['cmltve_deaths']
X = data_accum.drop(['cmltve_deaths'], axis=1)

# Separate numerical and categorical values
X_num = X.select_dtypes(include='number')
X_cat = X.select_dtypes(exclude='number')

# One Hot Encoding categorical variables
encoder = OneHotEncoder(handle_unknown='error', drop='first') #drop one column for efficiency. It can be deduced
X_cat_encoded = encoder.fit_transform(X_cat).toarray()

# Concat DataFrames

column_names = list(X_num.columns) # get list of numerical column names
column_names.extend(list(encoder.get_feature_names())) # add list of dummified categorical column names
X_numcat = np.concatenate([X_num, X_cat_encoded], axis=1)
X_ready = pd.DataFrame(data=X_numcat, index=X.index, columns=column_names)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_ready, y, test_size=0.3, random_state=42)

#Scaling data
scaler=StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform (X_test)
scaler_y = StandardScaler().fit(y_train.to_numpy().reshape(-1, 1))

#Fit Model
model = LinearRegression()
model.fit(X_train, y_train)

#Evaluation
predictions_norm = model.predict(X_test)
R2 = r2_score(y_test, predictions_norm)

predictions = scaler_y.inverse_transform(predictions_norm.reshape(-1, 1))

MAE = mean_absolute_error(y_test, predictions)
MSE = mean_squared_error(y_test, predictions, squared=True)
RMSE = mean_squared_error(y_test, predictions, squared=False)

import math

results = pd.DataFrame()
results['true'] = y_test
results['pred'] = predictions
results['resid'] = results.apply(lambda x: abs(x['true'] - x['pred']), axis=1)
results=results.sort_values('resid', ascending=False)

#st.table(results.head(5))

fig, ax = plt.subplots()
ax.boxplot(x=results['resid'],vert=False,)
st.pyplot(fig)