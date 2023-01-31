import requests
import json
import time
import pandas as pd

login = ...1
password = ...
download_path = '' # C:/Users/user/Desktop/
download_name = 'test.xlsx'

report_id = 'id'

target_date1 = '2022-12-01'
target_date2 = '2022-12-31'

x = requests.get('http://0.0.000.000:8080/')
payload = {"type":"Login","login":login,"password":password,"remember":'true'}
x = requests.post('http://10.2.144.177:8081/api/login', json = payload)
token = x.headers['X-Auth-Token']
print('Token: ' + token)

headers = {'X-Auth-Token': token}
params = {"p1":'',"target_date1":target_date1,"target_date2":target_date2,"p2":''}
payload = {"code":report_id,"format":"simple_xlsx","parameters":params}
x = requests.post('http://0.0.000.000:8080/api/export', json = payload, headers=headers)
print('Download request status: ' + str(x.status_code))
print(x.json()['fileName'])

json_object = json.loads(x.content)
file_id = str(json_object['id'])
print('File ID: ' + file_id)

download_link = 'http://0.0.000.000:8080/api/activity/content/'+file_id+'/'+download_name+'?X-Tenant-Id=default'
print('Link: ' + download_link)
time.sleep(10)
x = requests.get(download_link, headers=headers)
print('Content length: ' + str(len(x.content)))
open(download_path+download_name, "wb").write(x.content)
print('Success')

df = pd.read_excel('test.xlsx', sheet_name='Таблица 1', skiprows=2)
df.head(n=10)