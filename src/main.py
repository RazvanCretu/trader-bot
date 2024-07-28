import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime
import time
import os

print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

# establish connection to the MetaTrader 5 terminal
if mt5.initialize("C:\\Program Files\\MT5\\terminal64.exe",login=int(os.environ['ADMIRALS_ACCOUNT']),password=os.environ['ADMIRALS_PASS'],server='acs50.admiralmarkets.com'):
    time.sleep(2)

    from_date=datetime(2024,1,1)
    to_date=datetime.now()

    deals=mt5.history_orders_get(from_date, to_date)

    print(pd.DataFrame(deals, columns=deals[0]._asdict().keys()))

    mt5.shutdown()
else:
    print("Err")
    print("initialize() failed, error code =",mt5.last_error())
    # quit()

# get the number of deals in history
