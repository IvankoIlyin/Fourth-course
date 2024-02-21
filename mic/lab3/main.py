import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('archive/NationalNames.csv')

popular_names_by_year = df.groupby(['Year', 'Name']).agg({'Count': 'sum'})
most_popular_names_by_year = popular_names_by_year.groupby('Year').idxmax()
print(most_popular_names_by_year)






