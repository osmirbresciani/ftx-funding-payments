from client.client_ftx import *
from utils.csv_lib import *
from utils.ftx_lib import *
from set_markets import *

if __name__ == "__main__":
    ftx = FtxClient()
    ts_init = float(1621471949)
    ts_now = float(time.time())
    for market in markets:
        response = ftx.get_funding_payment_history(market, None, None, ts_init, ts_now)
        sum_payment = sum_funding(response)
        print(
            f" ||| {market}  | Long received {float(sum_payment['long_payment']):.2f} | Short received {float(sum_payment['short_payment']):.2f} |||"
        )
        # formatted_statement = [{i: (str(j).replace('.', ',')) if (i=='payment' or i=='rate') else j for i,j in x.items()} for x in response]
        # statement_to_csv(formatted_statement, 'funding-payments', market)
