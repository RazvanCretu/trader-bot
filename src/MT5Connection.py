import MetaTrader5 as mt5
from pandas import DataFrame, to_datetime

class Connection:

    def __init__(self, account: int, password: str, server: str = "") -> None:
        
        try:
    
            assert isinstance(account,int), "Account should be an `int`."
            assert isinstance(password,str), "Password should be a `str`."
            assert isinstance(server,str), "Password should be a `str`."

            if not server:
                raise ValueError("Server should not be empty!")

            if not mt5.initialize("C:\\Program Files\\MetaTrader5\\terminal64.exe",login=account,password=password,server=server,timeout=180000,portable=True):
                raise Exception(mt5.last_error())
            
            self.server = server

        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, exc_tb):

        mt5.shutdown()

        if exc_type or exc_value or exc_tb:
            print(exc_type, exc_value, exc_tb)
        else: pass

    def get_rates(self,symbol,timeframe,start,end) -> DataFrame:
        """
        Returns rates for a specified symbol given a timerange in a DataFrame format.
        """
        # rates = mt5.copy_rates_from(symbol,timeframe,start,10000)
        rates = mt5.copy_rates_range(symbol,timeframe,start,end)
        df=DataFrame(rates)
        df['time']=to_datetime(df['time'], unit='s')
        print(df)
        print(mt5.last_error())
        pass


# Connection(123, password="123")
