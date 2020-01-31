import sys


ACCEPTED_CURRENCIES = ['bch', 'btc', 'eth', 'ltc', 'etc']

MARKETS = [
    'korbit',
    'coinbase',
    'coinone',
    'bittrex',
    # 'bitfinex',
    # 'cexio',
    # 'exmo',
    # 'kraken',
    # 'livecoin',
    # 'wexnz'
]


def verify_args(args):
    if len(args) < 2:
        print('Usage:\npython percentage.py cryptocurrency [market_in] '
              '[market_out] [options]')
        sys.exit()
    # checking length
    if len(args) > 3:
        market_in = args[2].lower()
        market_out = args[3].lower()
    else:
        market_in = 'coinone'
        market_out = 'coinbase'
    # checking argument 1
    currency = args[1].lower()
    if currency not in ACCEPTED_CURRENCIES:
        if currency in ['-h', 'help', '--help']:
            print("Usage:\npython percentage.py [cryptocurrency]")
            sys.exit()
        if currency in ['market', 'markets', 'exchange', 'exchanges']:
            print("Supported exchanges: " + ', '.join(MARKETS))
            sys.exit()
        print("Invalid argument")
        print("Supported currencies are:", ACCEPTED_CURRENCIES)
        sys.exit()
    # and now the rest
    if market_in not in MARKETS or market_out not in MARKETS:
        print("Invalid market name")
        print("Here is the list of supported MARKETS:")
        print(MARKETS)
        sys.exit()
    return currency, market_in, market_out
