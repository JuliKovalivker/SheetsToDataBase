import gspread
import pandas as pd
import requests

def str_to_float(s):
    return float(s.replace(',', ''))

client = gspread.service_account(filename = 'credentials.json')
sh = client.open('BLCK_CAP') 

sh_ = sh.get_worksheet(1)
sh_ = pd.DataFrame(sh_.get_all_values())
lon = sh_.shape[0]
obj = {"assets" : [],
       "fundId": int(sh_[6][3])}

url = 'http://localhost:3000/api/update-nav-value' 
# url_ = 'http://localhost:3000/api/get-assets?fundId=2' 

for i in range(3, lon-1):
    obj["assets"].append([sh_[0][i], str_to_float(sh_[1][i])])

x = requests.post(url, json=obj)