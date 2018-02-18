"""
"""
__author__ = "merc1er"
__version__ = "0.1"
__email__ = "corentin@mercier.link"

################################################################################
import requests
import json
################################################################################

req = requests.get("https://api.coinone.co.kr/ticker/")
print(req.status_code)
btc = json.loads(req.text)

print(btc['last'])