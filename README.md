# Cryptocurrencies exchange markets arbitrage

This progam computes the arbitrage percentage between exchanges

### Usage

```shell
python percentage.py [cryptocurrency] [marketIn] [marketOut] [options]
```

### Supported Markets and Cryptocurrencies

#### Markets:

- Europe/NA:
	- gdax

- Asia:
	- coinone
	- korbit

#### Cryptocurrencies:

- BCH
- BTC
- ETH
- LTC

#### Options

- --html | Output in html for easy usage in webapps.
- --loop | Enter loop mode, the program will repeat checking every few seconds.
