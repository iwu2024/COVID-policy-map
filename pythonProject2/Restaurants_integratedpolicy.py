import pandas as pd
from datetime import datetime
from datetime import timedelta


reader=pd.read_csv("Restaurants.csv", converters={"FIPSCounty": '{:0>5}'.format})
county=reader["FIPSCounty"]
county=sorted(list(set(county)))

reader_fips=pd.read_csv("US_FIPS_Codes.csv")#
allcounty=reader_fips['FIPS']
allcounty=sorted(list(set(allcounty)))
allcounty=pd.to_numeric(allcounty)

for m in allcounty:
    if m <= 99:
        for i in range(1000*m, 1000*m+999):
            if i in allcounty:
                reader=reader.append(reader[reader["FIPSCounty"]==str(m).zfill(5)].replace(str(m).zfill(5),str(i).zfill(5)))
date0=reader["StartDate"]

date=[]
for x in date0:
    date.append(datetime.strptime(x, '%Y-%m-%d'))

Startweek=[]
for i in date:
    Startweek.append( (i - timedelta(days=i.isoweekday() % 7)))#.strftime('%Y-%m-%d'))

reader["Startweek"]=Startweek

reader=reader.sort_values(by=["StartDate","FIPSCounty"])

reader=reader.drop_duplicates(subset=["FIPSCounty", "Startweek"], keep='last')
reader.to_csv("Restaurants_integrated.csv")