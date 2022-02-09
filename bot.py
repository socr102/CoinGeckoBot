from pycoingecko import CoinGeckoAPI
import pandas as pd 
cg = CoinGeckoAPI()

def get_coin_data():
    # set the list to save necessary data
    name = []
    price = []
    roc = []
    volume = []
    mcap = []
    fdv = []
    tvl=[]
    platform=[]
    # get the data from the API
    coin_market = cg.get_coins_markets(vs_currency='usd')
    #fill the array
    for i in range(len(coin_market)):
        name.append(coin_market[i]['id'])
        price.append(coin_market[i]['current_price'])
        roc.append(float(coin_market[i]['current_price']/coin_market[0]['current_price']))
        volume.append(coin_market[i]['total_volume'])
        mcap.append(coin_market[i]['market_cap'])
        fdv.append(coin_market[i]['fully_diluted_valuation'])
        coin_by_id = cg.get_coin_by_id(coin_market[i]['id'])
        tvl.append(coin_by_id['market_data']['total_value_locked'])
        platform.append(coin_by_id['asset_platform_id'])

    data = {'Name': name, 'Price': price, 'Roc': roc, 'Volume': volume, 'Circ mcap': mcap, 'FDV': fdv, 'TVL': tvl, 'Platform': platform}
    # Create DataFrame  
    df = pd.DataFrame(data)  
    df.to_csv('coin.csv')

get_coin_data()