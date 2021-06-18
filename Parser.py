import requests
import json
import time

serverURL = "https://api.warframe.market/v1"

#stats :Path: /items/<url_name>/statistics

#Requests a list of all items from the server and returns it as python data structures.
def get_all_items(URL):
    response = requests.get(URL+"/items")
    itemlist = json.loads(response.text)["payload"]["items"]
    return itemlist

#Requests the information about an item to the server and returns it as python data structures.
def get_item_info(URL, item):
    response = requests.get(URL+"/items/"+item)
    return json.loads(response.text)

#Creates or overwrites a file containing the list of all items known to the server.
def item_list_to_file(filename, URL):
    file = open(filename +".json", "w")
    file.write(get_all_items(URL+"/items"))
    file.close

#Creates or overwrites a file containing the information provided by the server about the provided item.
def item_info_to_file(item, filename, URL):
    file = open(filename +".json", "w")
    file.write(get_item_info(URL, item))
    file.close

reliclist = []
itemlist = get_all_items(serverURL)
lenght = len(itemlist)
currentitemno = 1
with open("log.txt", "a") as log:
    for i in itemlist:
        time.sleep(0.3)
        itemname = i["url_name"]
        log.writelines("Checking " + str(itemname) + ", " + str(currentitemno) + "/" + str(lenght))
        print("Checking " + str(itemname) + ", " + str(currentitemno) + "/" + str(lenght))
        iteminfo = get_item_info(serverURL, itemname)["payload"]["item"]["items_in_set"][0]
        #if len(iteminfo) > 1:
        #    print("Set found : " + itemname)
        for j in iteminfo["tags"]:
            print("test")
            if j == "relic":
                reliclist.append(itemname)
                print("Relic found : " + str(itemname))
            if j == "mod":
                modlist.append(itemname)
                print("")
            
        currentitemno +=1

    log.writelines(str(reliclist))

