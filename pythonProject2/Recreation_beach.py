import pandas as pd

reader=pd.read_csv("cleaned_COVIDDataPull.csv", converters={"FIPSCounty": '{:0>5}'.format})

filtered=reader[reader["CategoryName"].str.contains("Recreation")]
filtered=filtered[filtered["PolicyName"].str.contains('Beach')]

for i in filtered["StartDate"]:
    i = pd.to_datetime(i)

#Then sort by datetime
filtered=filtered.sort_values(by=["StartDate", "FIPSCounty"])


filtered.to_csv("Recreation_beach.csv")