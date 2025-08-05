# verify_data.py
import os
from db_manager import read_all_data, init_db, save_data_to_db
from fetch_data import get_all_stock_data
from datetime import datetime, timedelta

def verify_and_restore():
    init_db()
    try:
        df = read_all_data()
        if df.empty or len(df) < 100000:  # 容错条件
            print("数据库数据异常或丢失，开始恢复...")
            start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")
            end_date = datetime.today().strftime("%Y%m%d")
            df_all = get_all_stock_data(start_date, end_date)
            save_data_to_db(df_all)
            print("数据恢复成功")
        else:
            print("数据校验通过，无需恢复")
    except Exception as e:
        print(f"校验出错：{e}")

if __name__ == "__main__":
    verify_and_restore()
