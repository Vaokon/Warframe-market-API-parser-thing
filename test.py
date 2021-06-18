import json
import requests
from requests.api import get
serverURL = "https://api.warframe.market/v1"
def get_item_info(item, URL):
    response = requests.get(URL+"/items/"+item)
    return json.loads(response.text)



#iteminfo = get_item_info(serverURL, "axi_l5_relic")["payload"]["item"]["items_in_set"]
print(get_item_info("cleanse_corrupted", serverURL))

