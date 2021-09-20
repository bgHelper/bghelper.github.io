# coding=utf-8

import requests
import json
from xml.etree import ElementTree
import time

def isChinse(s):
    for c in s:
        if u'\u4e00' <= c <= u'\u9fa5':
            return True
    return False

def putInClass(item, cat, link):
    id = link.attrib['id']
    if not id in cat:
        cat[id] = { "en" : link.attrib['value'], "zh" : link.attrib['value']}
    elif cat[id]["en"] != link.attrib['value']:
        print ("Error %d %d %s %s", id, id, cat[id]["en"], link.attrib['value'])
    item.append(id)

url = "https://www.boardgamegeek.com/xmlapi2/thing?stats=1&id="
idList = (289230,239464,822,2266,251658,245487,265736,245654)

for id in idList:
    url += "%d," % id

xml = requests.get(url)
#print(xml.content)
tree = ElementTree.fromstring(xml.content)

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

for item in tree.findall("item"):
    id = item.attrib['id']    
    if not id in dataBase["list"]:
        dataBase["list"][id] = {}
    dataItem = dataBase["list"][id]
    dataItem["img"] = item.find("image").text
    if not "description" in dataItem:
        dataItem["description"] = ""
    for name in item.findall("name"):
        if name.attrib["type"] == "primary":
            dataItem["en"] = name.attrib["value"]
        if isChinse(name.attrib["value"]):
            try:
                name.attrib["value"].encode('gb2312')
                dataItem["zh"] = name.attrib["value"]
            except:
                if not "zh" in dataItem:
                    dataItem["zh"] = name.attrib["value"]
    if not "zh" in dataItem:
        dataItem["zh"] = dataItem["en"]
    
    dataItem["year"] = int(item.find("yearpublished").attrib["value"])
    dataItem["minplayers"] = int(item.find("minplayers").attrib["value"])
    dataItem["maxplayers"] = int(item.find("maxplayers").attrib["value"])
    dataItem["minplaytime"] = int(item.find("minplaytime").attrib["value"])
    dataItem["maxplaytime"] = int(item.find("maxplaytime").attrib["value"])
    dataItem["minage"] = int(item.find("minage").attrib["value"])
    dataItem["category"] = []
    dataItem["family"] = []
    dataItem["mechanic"] = []
    for link in item.findall("link"):
        if link.attrib["type"] == "boardgamecategory":
            putInClass(dataItem["category"], dataBase["category"], link)
        elif link.attrib["type"] == "boardgamefamily":
            putInClass(dataItem["family"], dataBase["family"], link)
        elif link.attrib["type"] == "boardgamemechanic":
            putInClass(dataItem
            ["mechanic"], dataBase["mechanic"], link)
    rating = item.find("statistics").find("ratings")
    dataItem["rates"] = float(rating.find("average").attrib["value"])
    dataItem["weight"] = float(rating.find("averageweight").attrib["value"])
    dataItem["ranks"] = {}
    for rank in rating.find("ranks").findall("rank"):
        if rank.attrib['value'] == 'Not Ranked':
            continue
        rid = rank.attrib['id']        
        if not rid in dataBase["ranks"]:
            dataBase["ranks"][rid] = { "en" : rank.attrib['friendlyname'], "zh" : rank.attrib['friendlyname']}
        elif dataBase["ranks"][rid]["en"] != rank.attrib['friendlyname']:
            print ("Error %d %d %s %s", rid, rid, dataBase["ranks"][rid]["en"], rank.attrib['friendlyname'])
        dataItem["ranks"][rid] = int(rank.attrib['value'])

dataBase["update"] = time.strftime("%Y.%m.%d", time.localtime())

json.dump(dataBase, open(dataBaseName, "w", encoding="utf8"), indent=4, ensure_ascii=False)