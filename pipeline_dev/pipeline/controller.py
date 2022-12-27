# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

from sys import displayhook
from db.connector import DBConnector
from settings import DB_SETTINGS
# from pipeline import extract, transform, load
import pandas as pd

source_db = DBConnector(**DB_SETTINGS['source_db_localhost'])
target_db = DBConnector(**DB_SETTINGS['target_db_localhost'])

TABLE_LIST = ['actor', 'film']


def etl(batch_month):
    with source_db as source_connected:
        for table in TABLE_LIST:
            read_query = source_connected.get_query('read', table, {'batch_month': batch_month})
            print(read_query)
            
            with source_connected.conn.cursor() as source_cur:
                source_cur.execute(read_query)
                result_all = source_cur.fetchall()
                print(result_all[:1])

            with target_db as target_connected:
                create_query = target_connected.get_query('create', table)
                print(create_query)
                with target_connected.conn.cursor() as target_cur:
                    target_cur.executemany(create_query, result_all)
                    target_connected.conn.commit()