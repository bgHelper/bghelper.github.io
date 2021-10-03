# coding=utf-8

import requests
from xml.etree import ElementTree
import time

def isChinse(s):
    for c in s:
        if u'\u4e00' <= c <= u'\u9fa5':
            return True
    return False

def isTChinse(s):
    try:
        s.encode('gb2312')
        return True
    except:
        return False

def putInClass(item, cat, link):
    id = link.attrib['id']
    value = link.attrib['value']
    if not id in cat:
        cat[id] = { "en" : value, "zh" : value}
    elif cat[id]["en"] != value:
        print ("Error %d %d %s %s", id, id, cat[id]["en"], value)
    item.append(id)        

def update(dataBase, gameId):
    url = "https://www.boardgamegeek.com/xmlapi2/thing?stats=1&id=%d" % gameId
    
    xml = requests.get(url)
    tree = ElementTree.fromstring(xml.content)

    item = tree.find("item")
    id = item.attrib['id']    
    if not id in dataBase["list"]:
        dataBase["list"][id] = {}
    dataItem = dataBase["list"][id]
    dataItem["img"] = item.find("image").text
    if not "description" in dataItem:
        dataItem["description"] = ""
    for name in item.findall("name"):
        nameStr = name.attrib["value"]
        if name.attrib["type"] == "primary":
            dataItem["en"] = nameStr
        
        if isChinse(nameStr):
            if isTChinse(nameStr):
                dataItem["zh"] = nameStr
            else:
                if not "zh" in dataItem:
                    dataItem["zh"] = nameStr
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
    if not "pages" in dataItem:
        dataItem["pages"] = {}
    for link in item.findall("link"):
        if link.attrib["type"] == "boardgamecategory":
            putInClass(dataItem["category"], dataBase["category"], link)
        elif link.attrib["type"] == "boardgamefamily":
            putInClass(dataItem["family"], dataBase["family"], link)
        elif link.attrib["type"] == "boardgamemechanic":
            putInClass(dataItem["mechanic"], dataBase["mechanic"], link)
    rating = item.find("statistics").find("ratings")
    dataItem["rates"] = float(rating.find("average").attrib["value"])
    dataItem["weight"] = float(rating.find("averageweight").attrib["value"])
    dataItem["ranks"] = {}
    for rank in rating.find("ranks").findall("rank"):
        if rank.attrib['value'] == 'Not Ranked':
            continue
        rid = rank.attrib['id']
        rankname = rank.attrib['friendlyname']
        if not rid in dataBase["ranks"]:
            dataBase["ranks"][rid] = { "en" : rankname, "zh" : rankname}
        elif dataBase["ranks"][rid]["en"] != rankname:
            print ("Error %d %d %s %s", rid, rid, dataBase["ranks"][rid]["en"], rankname)
        dataItem["ranks"][rid] = int(rank.attrib['value'])

    dataBase["update"] = time.strftime("%Y.%m.%d", time.localtime())