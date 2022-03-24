import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

glob_metrics=pd.read_csv('../Streamlit/ML_global_metrics.csv').drop('Unnamed: 0',axis=1)
st.header("Machine Learning: Regression Metrics")

st.table(glob_metrics)
st.write("(LR stands for Linear Regression, SVR stands for Supported Vector Regression)")

st.subheader("Scores")
fig_1, ax_1 = plt.subplots()
ax_1.bar(x=glob_metrics['model'], height=glob_metrics['score'])
st.pyplot(fig_1)

st.write("The two best performing models were those that used the accumulated data.")

st.subheader("Other metrics")
good_models=glob_metrics.loc[[1, 3]].drop(['score','mean_squared_error'],axis=1)
idx = np.asarray([i for i in range(len(good_models['model']))])
width=0.4
fig_2 = plt.figure(figsize = (5,4))
ax_2 = fig_2.add_axes([0,0,1,1])
ax_2.bar(idx, good_models['mean_absolute_error'],width = width)
ax_2.bar(idx+width, good_models['RMSE'],width = width)
ax_2.set_xticks(idx+width/2)
ax_2.set_xticklabels(good_models['model'])#, rotation=65)
st.pyplot(fig_2)

st.write("Considering the scores, but also the other two metrics, the best model to predict COVID deaths based on accumulated data is a SVR.")