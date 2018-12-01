import json
from bottle import route, run, template, request, redirect
import requests
import os
data=[]

nums = len(data)
# category number
all_num = 100
Blenheim_spaniel_num = 10
bluetick_num = 10
chihuaua_num = 10
chow_num = 10
Japanese_spaniel_num = 10
Maltese_num = 10
Pekinese_num = 10
redbone_num = 10
toy_terrier_num = 10
basset_num = 10
# size number
Big_Size_num = 1
Medium_Size_num = 53
Small_Size_num = 46


def search(result,data):
    url = 'https://inf551-64842.firebaseio.com/'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Inf551-bba93adac10f.json'
    url_dog = url+'dog/'
    print('start search!!!')
    url_1 = url + result[1]+'/'
    print(url_1)
    response = requests.get(url_1+result[0]+'.json')
    if(response.json()==None):
        return (result[0]+' not found')
    #list.append(response.json())
    print(response.json())
    for index in response.json():
        response_dog = requests.get(url_dog + str(index) + '.json')
        data.append(response_dog.json())
    return data

@route('/', method="GET")
def test():
    #nums = len(data)
    size_selected = {"Big_Size": False, "Medium_Size": False, "Small_Size": False}
    cate_selected = {"All":["",all_num], "Blenheim_spaniel":["",Blenheim_spaniel_num],"bluetick": ["",bluetick_num], "chihuaua": ["",chihuaua_num],\
         "chow":["",chow_num], "Japanese_spaniel": ["",Japanese_spaniel_num], "Maltese": ["",Maltese_num], "Pekinese":["",Pekinese_num], \
         "redbone": ["",redbone_num], "toy_terrier": ["",toy_terrier_num], "basset": ["",basset_num]}
    #print(cate_selected)
    print(data)
    return template("index.html", data=data, cate_selected=cate_selected, size_selected=size_selected, nums=nums,\
                    Big_Size_num=Big_Size_num,Medium_Size_num=Medium_Size_num,Small_Size_num=Small_Size_num
                    )


@route('/category', method="POST")
def category():
    data = []
    result = []
    search_key=request.forms.get("category")
    size_selected = {"Big_Size": False, "Medium_Size": False, "Small_Size": False}
    cate_selected = {"All":["",all_num], "Blenheim_spaniel":["",Blenheim_spaniel_num],"bluetick": ["",bluetick_num], "chihuaua": ["",chihuaua_num],\
         "chow":["",chow_num], "Japanese_spaniel": ["",Japanese_spaniel_num], "Maltese": ["",Maltese_num], "Pekinese":["",Pekinese_num], \
         "redbone": ["",redbone_num], "toy_terrier": ["",toy_terrier_num], "basset": ["",basset_num]}
    result.append(search_key)
    result.append('categories')
    print(result)
    i=0
    for k in cate_selected:
        if k==search_key:
            cate_selected[k][0]="selected=true"
    #print(cate_selected)
    search(result,data)
    nums = len(data)
    return template("index.html", data=data, cate_selected=cate_selected, size_selected=size_selected, nums=nums,\
                    Big_Size_num = Big_Size_num, Medium_Size_num = Medium_Size_num, Small_Size_num = Small_Size_num
                    )



@route('/keyword', method="POST")
def keyword():
    data = []
    result = []
    size_selected = {"Big_Size": False, "Medium_Size": False, "Small_Size": False}
    cate_selected = {"All":["",all_num], "Blenheim_spaniel":["",Blenheim_spaniel_num],"bluetick": ["",bluetick_num], "chihuaua": ["",chihuaua_num],\
         "chow":["",chow_num], "Japanese_spaniel": ["",Japanese_spaniel_num], "Maltese": ["",Maltese_num], "Pekinese":["",Pekinese_num], \
         "redbone": ["",redbone_num], "toy_terrier": ["",toy_terrier_num], "basset": ["",basset_num]}
    keywords = request.forms.get("keywords")
    result.append(keywords)
    result.append('keywords')
    print(result)
    search(result,data)
    nums = len(data)
    return template("index.html", data=data, cate_selected=cate_selected, size_selected=size_selected, nums=nums, \
                    Big_Size_num=Big_Size_num, Medium_Size_num=Medium_Size_num, Small_Size_num=Small_Size_num
                    )
@route('/size', method="POST")



def size():
    data = []
    result = []
    size_selected = {"Big_Size":False, "Medium_Size": False,"Small_Size": False}
    size_search=request.forms.get("Size")
    cate_selected = {"All":["",all_num], "Blenheim_spaniel":["",Blenheim_spaniel_num],"bluetick": ["",bluetick_num], "chihuaua": ["",chihuaua_num],\
         "chow":["",chow_num], "Japanese_spaniel": ["",Japanese_spaniel_num], "Maltese": ["",Maltese_num], "Pekinese":["",Pekinese_num], \
         "redbone": ["",redbone_num], "toy_terrier": ["",toy_terrier_num], "basset": ["",basset_num]}
    result.append(size_search)
    result.append('size')
    print(result)
    for k in size_selected:
        if k==size_search:
            size_selected[k]=True
    print(size_selected)
    search(result,data)
    nums = len(data)
    return template("index.html", data=data, cate_selected=cate_selected, size_selected=size_selected,nums=nums, \
                    Big_Size_num=Big_Size_num, Medium_Size_num=Medium_Size_num, Small_Size_num=Small_Size_num
                    )

run(host='localhost', port=8080)


