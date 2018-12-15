# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 15:48:13 2018

@author: Zhang Yiming
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

Nasdaq = pd.read_csv(r'D:\AFPD\Projects\My code\9. presentation\data\IXIC.csv')
Google = pd.read_csv(r'D:\AFPD\Projects\My code\9. presentation\data\GOOG.csv')
interest_rate = pd.read_csv(r'D:\AFPD\Projects\My code\9. presentation\data\^TNX.csv')


Nas_AR = []
Goo_AR = []

for i in range(1,len(Google)):
    Nas_AR.append(Nasdaq['Close'][i]/Nasdaq['Close'][i-1]-1-interest_rate['Close'][i]/365)
    Goo_AR.append(Google['Close'][i]/Google['Close'][i-1]-1-interest_rate['Close'][i]/365)
    
model = sm.OLS(Goo_AR, Nas_AR)
#Model is a class so method could be used# 

results = model.fit()

results.params

results.tvalues

results.summary()


#Adding interception term#
interception_term = [1] * len(Goo_AR)

df_Nas_AR = pd.DataFrame({'Nas AR':Nas_AR,'Interception':interception_term})

model = sm.OLS(Goo_AR, df_Nas_AR)

results = model.fit()

results.params

results.tvalues

results.summary()