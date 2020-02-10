# Cryptocurrency exchange arbitrage software

This progam calculates the arbitrage percentage between exchanges

### Usage

```shell
python crypto-arbitrage/percentage.py _cryptocurrency_ [marketIn] [marketOut] [options]
```

#### Examples

```shell
python crypto-arbitrage/percentage.py bch bitkub coinbase
> Buy from bitkub - Sell to coinbase
> BCH: 0.10% buy: EUR 335.64 - sell: EUR 335.98
```

```shell
python crypto-arbitrage/percentage.py eth bittrex korbit
> Buy from bittrex - Sell to korbit
> ETH: -3.01% buy: EUR 161.25 - sell: EUR 156.39
```

### Supported Markets and Cryptocurrencies

#### Markets:

- Europe/NA:
	- Coinbase [*(processing time*)](https://help.coinbase.com/en/coinbase/trading-and-funding/sending-or-receiving-cryptocurrency/why-is-my-transaction-pending.html)
    - Bittrex
    - Kraken [*(processing time*)](https://support.kraken.com/hc/en-us/articles/203325283-Cryptocurrency-deposit-processing-times)

- Asia:
    - 🇰🇷 Korea:
        - Bithumb
    	- Coinone
    	- Korbit
    - 🇹🇭 Thailand:
        - Bitkub

#### Cryptocurrencies:

- BCH
- BTC
- ETH
- LTC
- ETC
