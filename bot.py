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
    # get the data from the API
    coin_market = cg.get_coins_markets(vs_currency='usd')
    coin_values = cg.get_exchange_rates()
    #fill the array
    for i in range(len(coin_market)):
        name.append(coin_market[i]['id'])
        price.append(coin_market[i]['current_price'])
        print(coin_values['rates'])
        # rate = float(coin_values[i]['value'])
        # roc.append(float(1/rate))
        volume.append(coin_market[i]['total_volume'])
        mcap.append(coin_market[i]['market_cap'])
        fdv.append(coin_market[i]['fully_diluted_valuation'])
    data = {'Name': name, 'Price': price, 'Volume': volume, 'Circ mcap': mcap, 'FDV': fdv}
    # Create DataFrame  
    df = pd.DataFrame(data)  
    df.to_csv('coin.csv')

get_coin_data()