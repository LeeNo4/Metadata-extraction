import os
from google.cloud import storage
import io
import json
from PIL import Image
from firebase_admin import storage
import firebase_admin
from firebase_admin import credentials


# Configure this environment variable via app.yaml
bucket_name = "inf551-64842.appspot.com"
cred = credentials.Certificate("inf551-64842-firebase-adminsdk-mxwaf-0a6f6f8fda.json")
app = firebase_admin.initialize_app(cred,{'storageBucket': bucket_name, }, name='storage')
#CLOUD_STORAGE_BUCKET = "inf551-64842.appspot.com"

# [end config]


def get_url(name):

        bucket = storage.bucket(app=app)
        blob = bucket.blob("dataset/"+name)
        blob.make_public()
        # Create a Cloud Storage client.

        return(blob.public_url)
dog_list = []
dict = {'dog':dog_list}
rootdir = 'imagedata'
list1 = os.listdir(rootdir)
address = ['Pekinese', 'Blenheim_spaniel', 'basset', 'Japanese_spaniel', 'chihuaua', 'Maltese', 'chow', 'toy_terrier', 'bluetick', 'redbone']

for j in range(0,len(address)):
        dir = rootdir+'/'+address[j]
        list = os.listdir(dir)
        print(list)
        for i in range(0,len(list)):
                if 'metadata' in list[i]:
                        continue
                path = os.path.join(dir,list[i])
                print(path)
                #'''
                try:
                        im = Image.open(path)
                except IOError, OSError:
                        continue
                print(im.format, im.size, im.mode)
                one_dog={}
                one_dog ={'name':list[i], 'category':address[j], 'format':im.format, 'size':im.size, 'mode':im.mode,'url':get_url(list[i])}
                dict['dog'].append(one_dog)
        #'''
#print(dict)

with open("./dog1.json",'w') as json_file:
                json.dump(dict,json_file,ensure_ascii=False)