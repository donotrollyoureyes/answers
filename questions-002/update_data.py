# update_data.py
from datetime import datetime, timedelta
from fetch_data import get_all_stock_data
from db_manager import init_db, get_last_date, save_data_to_db

def update_daily_data():
    init_db()
    last_date = get_last_date()
    if last_date:
        start_date = (datetime.strptime(last_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y%m%d")
    else:
        start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")
    end_date = datetime.today().strftime("%Y%m%d")
    df = get_all_stock_data(start_date, end_date)
    if not df.empty:
        save_data_to_db(df)
        print(f"新增数据已保存：{start_date} ~ {end_date}")
    else:
        print("无新增数据")

if __name__ == "__main__":
    update_daily_data()
