import requests
import os

url = 'https://inf551-64842.firebaseio.com/categories/'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Inf551-bba93adac10f.json'

category = 'basset'

response = requests.get(url+category+'.json')
if(response.json()==None):
    print(category+' not found')
#list.append(response.json())
print(response.json())