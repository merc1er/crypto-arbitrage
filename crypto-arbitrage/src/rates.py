import requests


def eur_equivalent(currency):
    """ Converts 1 EUR to `currency`"""
    endpoint = 'https://api.exchangeratesapi.io/latest'
    r = requests.get(endpoint)
    r.raise_for_status()
    rate = float(r.json()['rates'][currency])
    return rate
