from pycoingecko import CoinGeckoAPI
import pandas as pd 

cg = CoinGeckoAPI()
data = []
def get_price():
    coin_market = cg.get_coins_markets(vs_currency='usd')
    # df_market = pd.DataFrame(coin_market,columns=['id','current_price','market_cap','total_volume','fully_diluted_valuation'])
    # df_market.set_index('id',inplace=True)
    # df_market
    coin_length = len(coin_market)

    for i in range(0, coin_length):
        tmp = {}
        tmp['id'] = coin_market[i]['id']
        tmp['current_price'] = coin_market[i]['current_price']
        tmp['market_cap'] = coin_market[i]['market_cap']
        tmp['total_volume'] = coin_market[i]['total_volume']
        data.append(tmp)
        print(tmp)

get_price()