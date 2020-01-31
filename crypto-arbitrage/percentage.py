#!/usr/bin/env python3

import sys
from src.exchanges import *
from src.checks import verify_args


def display(currency, market_in, market_out):
    print("Buy from", market_in, "- Sell to", market_out)
    buy = fetch(market_in, currency)
    sell = fetch(market_out, currency)
    premium = (sell / buy - 1) * 100
    info = "buy: EUR " + str('%.2f' % buy) + " - sell: EUR " +\
        str('%.2f' % sell)
    print(currency.upper() + ": " + str('%.2f' % premium) + "% " + info)


def fetch(market, currency):
    if market == 'coinbase':
        exchange = CoinbasePro()
        return exchange.get_rate(currency)
    if market == 'coinone':
        exchange = Coinone()
        return exchange.get_rate(currency)
    if market == 'korbit':
        exchange = Korbit()
        return exchange.get_rate(currency)
    if market == 'bittrex':
        exchange = Bittrex()
        return exchange.get_rate(currency)
    if market == 'bitkub':
        exchange = Bitkub()
        return exchange.get_rate(currency)
    if market == 'kraken':
        exchange = Kraken()
        return exchange.get_rate(currency)
    raise TypeError
    # else:
    #     return float(cryptonator(currency, market))


def main():
    currency, market_in, market_out = verify_args(sys.argv)
    return display(currency, market_in, market_out)


if __name__ == '__main__':
    main()
