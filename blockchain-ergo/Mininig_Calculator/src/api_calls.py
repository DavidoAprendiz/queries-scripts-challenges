import json
import requests

API_TOKENJAY: str = "https://api.tokenjay.app/tokens/prices/03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04"
API_WHATTOMINE: str = "https://whattomine.com/coins.json"


def test_api() -> list | bool:
    test_req_coin: requests.Response = requests.get(API_WHATTOMINE)
    test_req_price: requests.Response = requests.get(API_TOKENJAY)
    if not test_req_coin.raise_for_status():
        if not test_req_price.raise_for_status():
            with open("./data/MinersData/WhatToMine.json", "w") as file:
                json.dump(test_req_coin.json()["coins"]["Ergo"], file, indent=4)
            with open("./data/MinersData/Ergo-SigUSD.json", "w") as file:
                json.dump(test_req_price.json(), file, indent=4)
            return [test_req_coin.json()["coins"]["Ergo"], test_req_price.json()]
    return False
