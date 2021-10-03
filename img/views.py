from django.shortcuts import render
import requests
access_token=""
repo=""

def getImgList():
    headers={"Accept": "application/vnd.github.v3+json","Authorization": f"token {access_token}"}
    r=requests.get(f"https://api.github.com/repos/{repo}/contents",headers=headers)
    imglist=[]
    for index,i in enumerate(r.json()):
        imgurl=i['html_url'].replace("https://github.com/","https://cdn.jsdelivr.net/gh/").replace("/blob/","@")
        imgdata={"id":index,"url":imgurl}
        imglist.append(imgdata)
    return imglist


def index(request):
    context={"imglist":getImgList()}
    return render(request,'img/index.html',context)