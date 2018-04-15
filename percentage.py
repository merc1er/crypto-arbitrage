#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "merc1er"
__version__ = "0.5"
__email__ = "corentin@mercier.link"


################################################################################
import sys
from fetcher import *
################################################################################



# Default Global Variable
marketIn = ["gdax"]
marketOut = ["korbit"]
markets = ['korbit', 'dgax', 'coinone']


##################
####  display ####
##################
def errorHandler(errors):
    print('Error: ' + errors)
    sys.exit();

def display(currency, html):
    print("Buy from", marketIn[0], "- Sell to", marketOut[0])
    premium = (korbit(currency)/gdax(currency) - 1) * 100 # quick mafs
    if html:
        info = "<small>buy: €" + str(gdax(currency)) + " - sell: €" \
        							+ str('%.2f'%korbit(currency)) + "</small>"
        print("<p class='text-center'>" + currency.upper() + ": " \
        						+ str('%.2f'%premium) + "% " + info + "</p>")
    else:
        info = "buy: " + str(gdax(currency)) + " - sell: " +\
                                                    str('%.2f'%korbit(currency))
        print( currency.upper() + ": " + str('%.2f'%premium) + "% " + info)

def verifyArgs():
    # checking arguments
    if len(sys.argv) < 2:
        print("Usage:\npython percentage.py cryptocurrency [marketIn] " +
                                                        "[marketOut] [options]")
        sys.exit()
    currency = sys.argv[1].lower()
    if len(sys.argv) > 3:
        marketIn[0] = sys.argv[2].lower()
        marketOut[0] = sys.argv[3].lower()

    if currency not in ['btc', 'bch', 'eth', 'ltc']:
        if currency in ['-h', 'help', '--help']:
            print("Usage:\npython percentage.py [cryptocurrency]")
            sys.exit()
        print("Invalid argument")
        sys.exit()
    return currency

################################################################################
# main

def main():
    currency = verifyArgs()
    if len(sys.argv) > 2 and sys.argv[-1] in ['--html']:
        display(currency, True);
    else:
        display(currency, False)

if __name__ == '__main__':
    main()
