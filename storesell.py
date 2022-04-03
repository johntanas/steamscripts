#accept tradeoffers for the account and sells items
#keep account details in account folder and steamguard details in steamguard folder
from steampy.client import SteamClient, TradeOfferState
from steampy.models import GameOptions
import enum
import time
import math
import parse_price as *
name=input("name of account? ")
module=__import__("account."+name,fromlist=(account))
cred=module.module
path="./steamguard/"+name+".txt"
class Currency(enum.IntEnum):
	JPY = 8
	SGD = 13
def is_donation(offer: dict) -> bool:
	return offer.get('items_to_receive') \
		and not offer.get('items_to_give') \
		and offer['trade_offer_state'] == TradeOfferState.Active \
		and not offer['is_our_offer']

steam_client = SteamClient(cred["apikey"])
steam_client.login(cred["login"], cred["password"],path)
print(steam_client.is_session_alive())
wallet_balance = steam_client.get_wallet_balance()
print("wallet="+str(wallet_balance))
offers = steam_client.get_trade_offers()['response']['trade_offers_received']
for offer in offers:
	if is_donation(offer):
		offer_id = offer['tradeofferid']
		num_accepted_items = len(offer['items_to_receive'])
		steam_client.accept_trade_offer(offer_id)
		print('Accepted trade offer {}. Got {} items'.format(offer_id, num_accepted_items))
inventory=steam_client.get_my_inventory(GameOptions.RUST)
item_amounts={}
for item in inventory.values():
	if item['marketable']:
		if item['market_hash_name'] in item_amounts:
			item_amounts[item['market_hash_name']] += 1
		else:
			item_amounts[item['market_hash_name']] = 1
price={}
for name in item_amounts.keys():
	price[name]=steam_client.market.fetch_price(name,GameOptions.RUST,Currency.JPY)
	time.sleep(3.3)
total=wallet_balance*100
for item,value in inventory.items():
	if not value['marketable']:
		continue
	lowest_price=parse_price(price[value['market_hash_name']]['lowest_price'])
	if 'median_price' in price[value['market_hash_name']]:
		median_price=parse_price(price[value['market_hash_name']]['median_price'])
		if median_price>lowest_price:
			lowest_price=median_price
	intprice=math.floor(lowest_price*100/1.15)
	total+=intprice
	sellingprice=str(intprice)
	sell_response =steam_client.market.create_sell_order(item, GameOptions.RUST, sellingprice)
	print(sell_response,value['market_hash_name'],sellingprice,"wallet="+str(total))
	time.sleep(1)
steam_client.logout()
