from steampy.client import SteamClient
from steampy.utils import GameOptions
import json
import time
import os
import re
a=os.listdir("./steamguard")
usingaccounts={}
for i in a:
	name=(os.path.splitext(i)[0])
	f=open("./steamguard/"+i)
	data=json.load(f)
	usingaccounts=[name]= data
total={}
for x,y in usingaccounts=.items():
	steam_client = SteamClient("some-api-key")
	steam_client.was_login_executed = True
	try:
		inventory = steam_client.get_partner_inventory(str(y["steamid"]), GameOptions.RUST)
	except:
		inventory={}
	item_amounts={}
	for item in inventory.values():
		#if not re.search("stockholm",item):
			if item["market_name"] in item_amounts:
				item_amounts[item['market_name']] += int(item[
				"amount"])
			else:
				item_amounts[item['market_name']] = int(item["amount"])
	for i,j in item_amounts.items():
		if i in total:
			total[i] += int(j)
		else:
			total[i] = int(j)
	print(x,item_amounts)
	time.sleep(5)
print(total)
