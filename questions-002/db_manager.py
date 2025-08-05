# db_manager.py
import sqlite3
import pandas as pd
import os

DB_NAME = 'stock_data.db'
TABLE_NAME = 'daily_price'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            code TEXT,
            日期 TEXT,
            开盘 REAL,
            收盘 REAL,
            最高 REAL,
            最低 REAL,
            成交量 REAL,
            成交额 REAL,
            振幅 REAL,
            涨跌幅 REAL,
            涨跌额 REAL,
            换手率 REAL,
            PRIMARY KEY(code, 日期)
        )
    ''')
    conn.commit()
    conn.close()

def save_data_to_db(df: pd.DataFrame):
    conn = sqlite3.connect(DB_NAME)
    df.to_sql(TABLE_NAME, conn, if_exists='append', index=False)
    conn.close()

def read_all_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql(f"SELECT * FROM {TABLE_NAME}", conn)
    conn.close()
    return df

def get_last_date():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT MAX(日期) FROM {TABLE_NAME}")
    last_date = cursor.fetchone()[0]
    conn.close()
    return last_date
