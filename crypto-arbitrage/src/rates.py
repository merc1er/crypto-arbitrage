import sys
import requests
from .secret import FIXER_API_KEY


def krw_rate():
    """ Converts 1 EUR to KRW"""
    if FIXER_API_KEY == '':
        print('Input your fixer.io API key in secrets.py')
        sys.exit()

    endpoint = 'http://data.fixer.io/api/latest?access_key='
    req = requests.get(endpoint + FIXER_API_KEY)
    req.raise_for_status()
    krw_string = req.json()['rates']['KRW']
    krw = float(krw_string)
    return krw
