from pycoingecko import CoinGeckoAPI
import pandas as pd 
cg = CoinGeckoAPI()
def get_price():
    coin_market = cg.get_coins_markets(vs_currency='usd')
    df_market = pd.DataFrame(coin_market,columns=['id','current_price','market_cap','total_volume','fully_diluted_valuation'])
    coinexcel = pd.ExcelWriter('Coin.xlsx')
    # write DataFrame to excel
    cars_data.to_excel(coinexcel)
    # save the excel
    coinexcel.save()
    print('DataFrame is written to Excel File successfully.')
get_price()