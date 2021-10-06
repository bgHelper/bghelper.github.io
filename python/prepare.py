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

def toList(dataBase, array):
    list = []
    for key in array:
        item = array[key]
        item['id'] = int(key)
        ml = []
        for m in item["mechanic"]:
            ml.append(dataBase["mechanic"][m]["zh"])
        item["mechanic"] = ml

        rl = []
        for r in item["ranks"]:
            rl.append({
                "val" : item["ranks"][r],
                "label" : dataBase["ranks"][r]["zh"]
            })
        item["ranks"] = rl
        del item['img']
        del item["category"]
        del item["family"]
        list.append(item)
    return list

def toListN(array):
    list = []
    for key in array:
        list.append(array[key]['zh'])
    return list     

def PrepareList():
    dataBase = LoadData()
    output = {}
    output["list"] = toList(dataBase, dataBase["list"])
    output["mechanic"] = toListN(dataBase["mechanic"])
    output["update"] = dataBase["update"]

    listFile = open("../src/assets/gameList.js", "w", encoding="utf8")
    listFile.write("const list = ")
    json.dump(output, listFile, indent=4, ensure_ascii=False)
    listFile.write("\n\n")
    listFile.write("export default list")
    listFile.close

def PrepareRouter():
    readfile = open("routes.json", "r", encoding="utf8")
    routes = json.load(readfile)
    readfile.close()
    dataBase = LoadData()
    array = dataBase["list"]
    for key in array:
        item = array[key]
        for idx in item["pages"]:
            newR = {
                "path": "/%s/%s" % (key, idx["to"]),
                "name" : "%s_%s" % (key, idx["to"]),
                "component": "pages/%s.vue" % idx["to"],                
            }
            routes.insert(-1, newR)
    print(routes)

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

def PreparePages():
    dataBase = LoadData()
    array = dataBase["list"]
    for key in array:
        output = array[key]
        dirPath = "../src/assets/%s/" % key
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        
        rulePath = dirPath + "Rule.js"
        if not os.path.isfile(rulePath):
            firstNode = {
                "title" : "基础信息",
                "text" : output["zh"]
            }
            output["list"] = [firstNode]
            print(rulePath, end="")            
            listFile = open(rulePath, "w", encoding="utf8")
            listFile.write("const list = ")
            json.dump(output, listFile, indent=4, ensure_ascii=False)
            listFile.write("\n\n")
            listFile.write("export default list")
            listFile.close
            print(" finish")

def PrepareAll():
    PrepareImg()
    PrepareList()
    #PreparePages()

if __name__ == '__main__':
   PrepareAll()


