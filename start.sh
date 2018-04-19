while true
do
  # writing on .new file so it doesn't remove altcoins while waiting for the
  # request to come
  python3 percentage.py btc > prices.new
  python3 percentage.py eth >> prices.new
  python3 percentage.py bch >> prices.new
  python3 percentage.py ltc >> prices.new
  cat prices.new > prices
  sleep 30
done;
