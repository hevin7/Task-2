
import pandas as pd
dataframe = pd.read_csv('student.csv')
print(dataframe.head())

column = dataframe['first_name']
columns = dataframe[['gender', 'status']]
filtered_dataframe = dataframe[dataframe['entry_age'] > 30]
print(filtered_dataframe)
dataframe = dataframe.drop(['ethnicity', 'act_composite'], axis=1)
grouped = dataframe.groupby('entry_age').sum()
dataframe_dropna = dataframe.dropna()
dataframe_no_duplicates = dataframe.drop_duplicates()
filtered_dataframe = dataframe[dataframe['entry_age'] > 30]
sorted_dataframe = dataframe.sort_values(by='entry_age')
grouped_dataframe = dataframe.groupby('gender')['entry_age'].mean()

