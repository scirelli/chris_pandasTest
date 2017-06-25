#!/usr/local/bin/python3
import pandas as pd
import numpy as np

##Call File
xlsx = pd.ExcelFile('./Claims Data Test File.xlsx')

#Print sheet names so that you can reference them in your code
#print(xlsx.sheet_names)

#Call File and pre name sheets that you want to work with.  
claims = pd.DataFrame(pd.read_excel(xlsx, sheetname = 'Claims'))
policies = pd.DataFrame(pd.read_excel(xlsx, sheetname = 'Policies'))

#print(claims.head())
# print(claims['Production Office'][2])
# print(policies['Production Office'][36])
# if claims['Production Office'][2] == policies['Production Office'][36]:
# 	print('code worked')
# print('Type of ', type(policies['Production Office']))
#print(claims['Production Office'][2]);
# count = 0
# for x in policies['Production Office']:
# 	if claims['Production Office'][2] == x:
# 		count += 1
# print('There are ', count, claims['Production Office'][2], ' in the Policies sheet')
# if claims['Production Office'][2] in policies['Production Office']:
# 	print('code worked')

print(policies[ policies['Production Office'] == claims['Production Office'][2] ].head(5))
