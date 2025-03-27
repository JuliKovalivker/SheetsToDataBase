import gspread
import pandas as pd
import requests

client = gspread.service_account(filename = 'credentials.json')
sh = client.open('BLCK_CAP') 

sh_ = sh.get_worksheet(1)
sh_ = pd.DataFrame(sh_.get_all_values())
lon = sh_.shape[0]
obj = dict()

url = 'https://app.kbinvesting.ai/' 

for i in range(3, lon-1):
    obj[sh_[0][i]] = sh_[1][i]
    print(sh_[0][i], obj[sh_[0][i]])
    #x = requests.post(url, json = obj)