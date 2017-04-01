Poetry generated using [X except its Y](../X_except_its_Y.py) on permutations of [the lyrics from the first 4 Nine Inch Nails albums](nin.txt):

* [nin1](nin1.txt) is generated with `./X_except_its_Y.py nin.txt <(tac nin.txt)`

* [nin2](nin2.txt) is generated with `./X_except_its_Y.py <(tac nin.txt) nin.txt`

* [nin3](nin3.txt) is generated with `./X_except_its_Y.py nin.txt <(tail -n +5 nin.txt ; head -n 5 nin.txt)`

* [nin4](nin4.txt) is generated with `./X_except_its_Y.py nin.txt <(tail -n +7 nin.txt ; head -n 7 nin.txt)`

* [nin5](nin5.txt) is generated with `./X_except_its_Y.py nin.txt <(tail -n +13 nin.txt ; head -n 13 nin.txt)`

* [nin6](nin6.txt) is generated with `./X_except_its_Y.py nin.txt <(tail -n +23 nin.txt ; head -n 23 nin.txt)`

