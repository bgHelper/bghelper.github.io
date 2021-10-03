# coding=utf-8

import update
import json
import time

dataBaseName = "dataBase.json"

readfile = open(dataBaseName, "r", encoding="utf8")
dataBase = json.load(readfile)
readfile.close()

if not "list" in dataBase:
    dataBase["list"] = {}
if not "family" in dataBase:
    dataBase["family"] = {}
if not "category" in dataBase:
    dataBase["category"] = {}
if not "mechanic" in dataBase:
    dataBase["mechanic"] = {}
if not "ranks" in dataBase:
    dataBase["ranks"] = {} 

idList = (289230,239464,822,2266,251658,245487,265736,245654)

for id in idList:
    update.update(dataBase, id)

dataBase["update"] = time.strftime("%Y.%m.%d", time.localtime())

json.dump(dataBase, open(dataBaseName, "w", encoding="utf8"), indent=4, ensure_ascii=False)