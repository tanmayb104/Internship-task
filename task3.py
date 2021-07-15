'''
Write a function to change the datetime format to format='%d%b%Y' in pandas DataFrame.
Input- Dates= {'dates': ['05Sep2009','13Sep2011','21Sep2010']}
Output- { ‘dates’: [2019-09-02,2019-09-13,2019-09-21]}
'''

import pandas as pd

# Initializing the dataframe
df = pd.DataFrame({'dates': ['05Sep2009','13Sep2011','21Sep2010']})
# Converting date to the desired format
df['dates'] = pd.to_datetime(df.dates)
print(df)