#!/usr/bin/env python3

import sys
import time
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
        return gdax(currency)
    if market == 'coinone':
        return coinone(currency)
    if market == 'korbit':
        korbit = Korbit()
        return korbit.get_rate(currency)
    if market == 'bittrex':
        return bittrex(currency)
    return False
    # else:
    #     return float(cryptonator(currency, market))


def loop(currency):
    print("\r\nEntering loop mode. Press ctrl + c to exit")
    while True:
        try:
            display(currency, False)
            time.sleep(60)
        except KeyboardInterrupt:
            print("\r\nQuitting...")
            sys.exit()


def main():
    currency, market_in, market_out = verify_args(sys.argv)
    return display(currency, market_in, market_out)


if __name__ == '__main__':
    main()
