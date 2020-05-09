# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:00:40 2020

@author: CSL
"""

import pandas as pd
from statsmodels.formula.api import ols


data = pd.read_excel('tm.xlsx', sheet_name='Sheet4', index_col=0)
x = data['市场风险溢价'].tolist()
x_square = list(map(lambda x: x**2, x)) #不能直接对列表进行平方，必须先用map函数，再转换成list

res = []
data_out = data.T
for c in data.columns.tolist()[2:]:
    y = data[c].tolist()
    
    temp = pd.DataFrame({'x':x, 'x_square':x_square, 'y':y})
    model = ols('y~x+x_square', temp).fit()
    
    model.rsquared
    model.fvalue
    model.tvalues
    model.params
    model.pvalues
    model.conf_int()
    model.f_pvalue
    
    data_out.loc[c, 'Alpha'] = model.params['Intercept']
    data_out.loc[c, 'Alpha-t'] = model.tvalues['Intercept']
    data_out.loc[c, 'Alpha-p'] = model.pvalues['Intercept']
    data_out.loc[c, 'Beta1'] = model.params['x']
    data_out.loc[c, 'Beta1-t'] = model.tvalues['x']
    data_out.loc[c, 'Beta1-p'] = model.pvalues['x']
    data_out.loc[c, 'Beta2'] = model.params['x_square']
    data_out.loc[c, 'Beta2-t'] = model.tvalues['x_square']
    data_out.loc[c, 'Beta2-p'] = model.pvalues['x_square']
    data_out.loc[c, 'R^2'] = model.rsquared
    data_out.loc[c, 'F'] = model.fvalue
    data_out.loc[c, 'F-p'] =  model.f_pvalue
    

data_out.T.to_excel('tm_result2.xlsx', index=True)
