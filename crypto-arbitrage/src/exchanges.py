#!/usr/bin/env python3

#
# fetches the market price from the exchanges
#

import requests
from .rates import eur_equivalent


class Exchange:
    base_endpoint = ''
    post_url = ''
    base_currency = ''
    json_rate_arg = ''  # e.g. 'ask' or 'last'
    params = False  # if request requires parameters

    def get_rate(self, crypto):
        if self.params:
            r = requests.get(self.base_endpoint, params={'currency': crypto})
        else:
            r = requests.get(self.base_endpoint +
                             crypto.lower() + self.post_url)
        r.raise_for_status()
        data = r.json()
        if type(self.json_rate_arg) is list:
            rate_base_currency = float(
                data[self.json_rate_arg[0]][self.json_rate_arg[1]])
        else:
            rate_base_currency = float(data[self.json_rate_arg])
        if self.base_currency.upper() != 'EUR':
            rate = rate_base_currency / eur_equivalent(self.base_currency)
        else:
            rate = rate_base_currency
        return rate


class Korbit(Exchange):
    base_endpoint = 'https://api.korbit.co.kr/v1/ticker?currency_pair='
    post_url = '_krw'
    base_currency = 'KRW'
    json_rate_arg = 'last'


class Coinone(Exchange):
    base_endpoint = 'https://api.coinone.co.kr/ticker/'
    base_currency = 'KRW'
    json_rate_arg = 'last'
    params = True


class CoinbasePro(Exchange):
    base_endpoint = 'https://api.pro.coinbase.com/products/'
    post_url = '-EUR/ticker'
    base_currency = 'EUR'
    json_rate_arg = 'ask'


class Bittrex(Exchange):
    base_endpoint = 'https://bittrex.com/api/v1.1/public/getticker?market=usd-'
    base_currency = 'USD'
    json_rate_arg = ['result', 'Last']


class Bitkub(Exchange):
    base_endpoint = 'https://api.bitkub.com/api/market/ticker'
    base_currency = 'THB'

    def get_rate(self, crypto):
        r = requests.get(self.base_endpoint)
        r.raise_for_status()
        rate_base_currency = r.json()['THB_' + crypto.upper()]['last']
        rate = rate_base_currency / eur_equivalent(self.base_currency)
        return rate


def cryptonator(currency_in, market):
    req = requests.get("https://api.cryptonator.com/api/full/" +
                       currency_in.lower() + "-eur")
    req.raise_for_status()
    callback = req.json()
    markets = callback['ticker']['markets']
    if market == 'bitfinex':
        return markets[0]['price']
    if market == 'cexio':
        return markets[1]['price']
    if market == 'exmo':
        return markets[2]['price']
    if market == 'kraken':
        return markets[3]['price']
    if market == 'livecoin':
        return markets[4]['price']
    if market == 'wexnz':
        return markets[5]['price']
    return False
