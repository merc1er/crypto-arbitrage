import requests


def krw_rate():
    """ Converts 1 EUR to KRW"""
    endpoint = 'https://api.exchangeratesapi.io/latest'
    r = requests.get(endpoint)
    r.raise_for_status()
    krw_string = r.json()['rates']['KRW']
    krw = float(krw_string)
    return krw
