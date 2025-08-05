# fetch_data.py
import akshare as ak
import pandas as pd
from datetime import datetime, timedelta

def get_all_a_stocks():
    stock_list = ak.stock_info_a_code_name()
    return stock_list['code'].tolist()

def get_stock_daily(code, start_date, end_date):
    try:
        df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=start_date, end_date=end_date, adjust="qfq")
        df['code'] = code
        return df
    except Exception as e:
        print(f"[{code}] 获取失败：{e}")
        return pd.DataFrame()

def get_all_stock_data(start_date, end_date):
    all_codes = get_all_a_stocks()
    result = []
    for code in all_codes:
        df = get_stock_daily(code, start_date, end_date)
        if not df.empty:
            result.append(df)
    return pd.concat(result, ignore_index=True)
