while true
do
python3 percentage.py btc > prices
python3 percentage.py eth >> prices
python3 percentage.py bch >> prices
# python3 percentage.py ltc >> prices
sleep 30
done;
