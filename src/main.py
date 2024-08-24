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
    from_date=datetime(2000,1,1)
    to_date=datetime.now()

    con.get_rates("[SP500]",mt5.TIMEFRAME_D1,from_date,to_date)

# establish connection to the MetaTrader 5 terminal
if mt5.initialize("C:\\Program Files\\MetaTrader5\\terminal64.exe",login=int(os.environ['ADMIRALS_ACCOUNT']),password=os.environ['ADMIRALS_PASS'],server='acs50.admiralmarkets.com',timeout=180000,portable=True):
    # time.sleep(15)

    from_date=datetime(2020,1,1)
    to_date=datetime.now()

    positions=mt5.positions_get()
    deals=mt5.history_deals_get(from_date, to_date)
    orders=mt5.history_orders_get(from_date, to_date)

    print(mt5.DEAL_TYPE_CREDIT)

    pd.DataFrame(deals, columns=deals[0]._asdict().keys()).to_csv("S:\\deals.csv",index=False)
    pd.DataFrame(orders, columns=orders[0]._asdict().keys()).to_csv("S:\\orders.csv",index=False)
    pd.DataFrame(positions, columns=positions[0]._asdict().keys()).to_csv("S:\\positions.csv",index=False)

    mt5.shutdown()
else:
    print("Err")
    print("initialize() failed, error code =",mt5.last_error())
    # quit()

# get the number of deals in history
