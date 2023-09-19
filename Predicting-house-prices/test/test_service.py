import pandas as pd
import requests

con = 'postgresql://radio:123456@localhost/first'
data = pd.read_sql_table('flats', con)

dict_data = data.sample(2).to_dict(orient='records')

BASE = "http://192.168.0.101:5000/"
response = requests.post(BASE + "predict", json=dict_data)

print(response.json())
