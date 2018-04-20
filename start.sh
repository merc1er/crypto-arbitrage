while true
do
  # writing on .new file so it doesn't remove altcoins while waiting for the
  # request to come
  python3 percentage.py btc --html > prices.new
  python3 percentage.py eth --html >> prices.new
  python3 percentage.py bch --html >> prices.new
  python3 percentage.py ltc --html >> prices.new
  cat prices.new > prices
  sleep 30
done;
