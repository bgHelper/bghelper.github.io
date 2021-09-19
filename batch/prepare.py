# coding=utf-8

import requests
import json
import os

dataBaseName = "dataBase.json"

readfile = open(dataBaseName, "r", encoding="utf8")
dataBase = json.load(readfile)
readfile.close()

def toList(array):
    list = []
    for key in array:
        item = array[key]
        item['id'] = int(key)
        imgFile = "./img/" + key + ".jpg"
        if not os.path.isfile(imgFile):
            print("downloading ", key, end="")
            open(imgFile, "wb").write(requests.get(item['img']).content)
            print(" finish")
        del item['img']
        list.append(item)
    return list

dataBase["list"] = toList(dataBase["list"])

listFile = open("gameData.js", "w", encoding="utf8")
listFile.write("const data = ")
json.dump(dataBase, listFile, indent=4, ensure_ascii=False)
listFile.write("\n\n")
listFile.write("export default data")
listFile.close

