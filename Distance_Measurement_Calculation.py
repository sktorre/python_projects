# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Distance Measurement Calculation.py: This file uses the Mahalanobis Distance distance-based   #
#            matching technique to match donors and recipients                                  #
#                                                                                               #
# Author:    Sarah Torrence                                                                     #
#                                                                                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

xls = pd.ExcelFile('')

# Read in recipients and filter 
r = pd.read_excel(xls, 'file_name_recipients')
r = pd.DataFrame(r)
recipients = list(r['respondentid'])

# Read in donors and filter for 
d = pd.read_excel(xls, 'file_name_donors')
d = pd.DataFrame(d)
donors = list(d['respondentid'])

#Read in importance and filter for 
importance = pd.read_excel(xls, 'file_name_importance')
imp = pd.DataFrame(importance)
imp = imp.sort_values('demo')

#Create diagonal matrix of importance (I)
I = pd.DataFrame.as_matrix(imp["importance"])
I = np.diag(I) 
np.savetxt("I_matrix.csv", I, delimiter=",") 

#Create X matrix using only variables in I
X = pd.DataFrame()
demo = list(imp["demo"])
demo = [i.lower() for i in demo]
for col in range(len(r.columns)):
    if r.columns[col] in demo:
        X = X.append(r[r.columns[col]])
X = X.sort_index()
X_matrix = np.array(X)
X_matrix = np.transpose(X_matrix)
np.savetxt("X_matrix.csv", X_matrix, delimiter=",")        
        
#Create Y matrix using only variables in I
Y = pd.DataFrame()
for col in range(len(d.columns)):
    if d.columns[col] in demo:
        Y = Y.append(d[d.columns[col]])
Y = Y.sort_index()
Y_matrix = np.array(Y)
Y_matrix = np.transpose(Y_matrix)
np.savetxt("Y_matrix.csv", Y_matrix, delimiter=",")

#Create the inverse of the covariance matrix (C^-1)
C = np.cov(np.vstack([X_matrix, Y_matrix]).T)
Cinv = np.linalg.inv(C).T    # C will be inverse of covariance matrix
np.savetxt("C_-1.csv", Y_matrix, delimiter=",")

#Calculate the Mahalanobis Distance
X_dot_I = np.dot(X_matrix, I)
Y_dot_I = np.dot(Y_matrix, I)
D = cdist(X_dot_I, Y_dot_I, 'mahalanobis', VI=Cinv)

#Format the Distance output file
Distance = pd.DataFrame(D,recipients,donors)
avg = list(Distance.mean(1))
Distance['avg_distance'] = avg
Distance.to_csv('Distance_Recalculation.csv')
