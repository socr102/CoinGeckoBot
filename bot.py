from pycoingecko import CoinGeckoAPI
import pandas as pd 

cg = CoinGeckoAPI()
ids='bitcoin'
def get_price():
    coin_market = cg.get_coins_markets(vs_currency='usd'))
    df_market = pd.DataFrame(coin_market,columns=['id','current_price','market_cap','total_volume','fully_diluted_valuation'])
    df_market.set_index('id',inplace=True)
    df_market
get_price()