from google.cloud import storage
import os
import requests
import json


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Inf551-bba93adac10f.json'

url = 'https://inf551-64842.firebaseio.com'

def create_bucket(bucket_name):
    """Creates a new bucket."""
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print('Bucket {} created'.format(bucket.name))

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def download_blob():
    """Downloads a blob from the bucket."""
    r1 = requests.get(url + '/dog.json')
    dicta = r1.json()
    dictb = {}
    for i in range(len(dicta)):
        try:
            dictb[dicta[i]['category']].append(dicta[i]['name'])
        except KeyError:
            dictb[dicta[i]['category']] = []
    jdata = json.dumps(dictb)
    response = requests.put(url + '/category.json', jdata)

if __name__ == '__main__' :
    upload = 0
    download = 1
    bucket_name = "inf551-64842.appspot.com"

    if upload == 1:
        rootdir = 'image'
        list1 = os.listdir(rootdir)
        for image_path in list1:
            blob = "dataset/"+image_path
            source_file_name = "image/"+image_path

            upload_blob(bucket_name, source_file_name, blob)

    if download == 1:
        download_blob()
