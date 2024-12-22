import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime
import time
import os
from dotenv import load_dotenv
from MT5Connection import Connection

load_dotenv()

print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

with Connection(int(os.environ['ADMIRALS_ACCOUNT']),os.environ['ADMIRALS_PASS'],server='acs50.admiralmarkets.com') as con:
    from_date=datetime(2024,1,1)
    to_date=datetime.now()

    print(con.get_rates("[SP500]",mt5.TIMEFRAME_D1,from_date,to_date))

    positions=con.positions_get()
    deals=con.history_deals_get(from_date, to_date)
    orders=con.history_orders_get(from_date, to_date)

    print(mt5.DEAL_TYPE_CREDIT)

    pd.DataFrame(deals, columns=deals[0]._asdict().keys()).to_csv("S:\\deals.csv",index=False)
    pd.DataFrame(orders, columns=orders[0]._asdict().keys()).to_csv("S:\\orders.csv",index=False)
    pd.DataFrame(positions, columns=positions[0]._asdict().keys()).to_csv("S:\\positions.csv",index=False)
