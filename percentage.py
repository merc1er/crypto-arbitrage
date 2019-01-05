#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "merc1er"
__email__ = "corentin@mercier.link"


################################################################################
import sys
import time
from src.fetcher import *
################################################################################



# Default Global Variables
marketIn = ['gdax']
marketOut = ['korbit']

MARKETS = [ 'korbit',
            'gdax',
            'coinbase',
            'coinone',
            'bitfinex',
            'cexio',
            'exmo',
            'kraken',
            'livecoin',
            'wexnz']

accepted_currencies = ['bch', 'btc', 'eth', 'ltc', 'etc']


##################
####  display ####
##################

def display(currency, html):
    # print("Buy from", marketIn[0], "- Sell to", marketOut[0])
    buy = fetch(marketIn[0], currency)
    sell = fetch(marketOut[0], currency)
    premium = (sell / buy - 1) * 100
    if html:
        info = "<small>buy: " + str('%.2f'%buy) + " - sell: " \
        							+ str('%.2f'%sell) + "</small>"
        print("<p class='text-center'>" + currency.upper() + ": " \
        						+ str('%.2f'%premium) + "% " + info + "</p>")
    else:
        info = "buy: " + str('%.2f'%buy) + " - sell: " +\
                                                    str('%.2f'%sell)
        print(currency.upper() + ": " + str('%.2f'%premium) + "% " + info)

##############
### checks ###
##############

def verifyArgs():
    if len(sys.argv) < 2:
        print("Usage:\npython percentage.py cryptocurrency [marketIn] " +
                                                        "[marketOut] [options]")
        sys.exit()
    # checking length
    if len(sys.argv) > 3:
        marketIn[0] = sys.argv[2].lower()
        marketOut[0] = sys.argv[3].lower()
    # checking argument 1
    currency = sys.argv[1].lower()
    if currency not in accepted_currencies:
        if currency in ['-h', 'help', '--help']:
            print("Usage:\npython percentage.py [cryptocurrency]")
            sys.exit()
        if currency in ['market', 'markets', 'exchange', 'exchanges']:
            print("Supported exchanges: " + ', '.join(MARKETS))
            sys.exit()
        print("Invalid argument")
        print("Supported currencies are:", accepted_currencies)
        sys.exit()
    # and now the rest
    if marketIn[0] not in MARKETS or marketOut[0] not in MARKETS:
        print("Invalid market name")
        print("Here is the list of supported MARKETS:")
        print(MARKETS)
        sys.exit()
    return currency

#############
### FETCH ###
#############

def fetch(market, currency):
    if market == "gdax":
        return gdax(currency)
    if market == "coinone":
        return coinone(currency)
    if market == "korbit":
        return korbit(currency)
    else:
        return float(cryptonator(currency, market))

#################
### Loop mode ###
#################

def loop(currency):
    print("\r\nEntering loop mode. Press ctrl + c to exit");
    while True:
        try:
            display(currency, False);
            time.sleep(2)
        except KeyboardInterrupt:
            print("\r\nQuitting...")
            sys.exit()


################################################################################
# main

def main():
    currency = verifyArgs()
    if len(sys.argv) > 2 and sys.argv[-1] in ['--html']:
        display(currency, True);
    elif len(sys.argv) > 2 and sys.argv[-1] in ['--loop']:
        loop(currency)
    else:
        display(currency, False)

if __name__ == '__main__':
    main()
