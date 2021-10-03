# coding=utf-8

import requests
import json
import os

def LoadData():
    dataBaseName = "dataBase.json"
    readfile = open(dataBaseName, "r", encoding="utf8")
    dataBase = json.load(readfile)
    readfile.close()
    return dataBase

def toList(array):
    list = []
    for key in array:
        item = array[key]
        item['id'] = int(key)
        del item['img']
        del item["category"]
        del item["family"]
        list.append(item)
    return list

def toListN(array):
    list = []
    for key in array:
        item = {            
            "value" : key,
            "label" : array[key]['zh']
        }
        list.append(item)
    return list     

def PrepareList():
    dataBase = LoadData()
    output = {}
    output["list"] = toList(dataBase["list"])
    output["mechanic"] = toListN(dataBase["mechanic"])

    listFile = open("../src/assets/gameList.js", "w", encoding="utf8")
    listFile.write("const list = ")
    json.dump(output, listFile, indent=4, ensure_ascii=False)
    listFile.write("\n\n")
    listFile.write("export default list")
    listFile.close

def PrepareRouter():
    return

def PrepareImg():
    dataBase = LoadData()
    array = dataBase["list"]
    for key in array:
        item = array[key]
        imgFile = "../public/img/" + key + ".jpg"
        if not os.path.isfile(imgFile):
            print("downloading ", key, end="")
            open(imgFile, "wb").write(requests.get(item['img']).content)
            print(" finish")

def PrepareAll():
    PrepareImg()
    PrepareList()
    PrepareRouter()

if __name__ == '__main__':
   PrepareAll()





#dataBase["list"] = toList(dataBase["list"])
##dataBase["category"] = toListN(dataBase["category"])
#del dataBase["category"]
##dataBase["family"] = toListN(dataBase["family"])
#del dataBase["family"]
#dataBase["mechanic"] = toListN(dataBase["mechanic"])
#
#listFile = open("gameData.js", "w", encoding="utf8")
#listFile.write("const data = ")
#json.dump(dataBase, listFile, indent=4, ensure_ascii=False)
#listFile.write("\n\n")
#listFile.write("export default data")
#listFile.close

