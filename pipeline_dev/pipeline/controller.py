# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

from sys import displayhook
from db.connector import DBConnector
# from pipeline.extractor import cursor_extractor, pandas_extractor
from pipeline import extractor, load, transform
from settings import DB_SETTINGS
# from pipeline import extract, transform, load
import pandas as pd
from sqlalchemy import create_engine


source_engine = \
    create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'\
        .format(\
            user = "postgres"
            , password = "0328"
            , host = "127.0.0.1"
            , port = "5432"
            , database = "dvdrental")
            )
target_engine = \
    create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'\
        .format(\
            user = "postgres"
            , password = "0328"
            , host = "127.0.0.1"
            , port = "5432"
            , database = "sample")
            )

source_db = DBConnector(**DB_SETTINGS['source_db_localhost'])
target_db = DBConnector(**DB_SETTINGS['target_db_localhost'])

TABLE_LIST = ['actor', 'film']


# def etl(batch_month):
#     with source_db as source_connected:
#         for table in TABLE_LIST:
#             read_query = source_connected.get_query('read', table, {'batch_month': batch_month})
#             print(read_query)
            
#             with source_connected.conn.cursor() as source_cur:
#                 source_cur.execute(read_query)
#                 result_all = source_cur.fetchall()

#             return print(result_all[:1])

# curcor, pandas
def etl(batch_month, read_option = 'pandas'):
    # for table in TABLE_LIST:
    #     _temp = extractor(db_connector=source_db, table_name = table, batch_month=batch_month, read_option=read_option)
    for table in TABLE_LIST:
        if read_option == 'cursor':
            _temp = extractor.cursor_extractor(db_connector=source_db, table_name = table, batch_month=batch_month)

        elif read_option == 'pandas':
            _temp = extractor.pandas_extractor(db_connector=source_db, table_name = table, batch_month=batch_month)
            _temp2 = transform.data_trans(table, _temp)
            # _temp = extractor.pandas_extractor(db_connector=source_db, table_name = table, batch_month=batch_month)
        
        print(_temp2[:2])

        if read_option == 'cursor':
            load.cursor_loader(db_connector = target_db, table_name = table, data = _temp2)

        elif read_option == 'pandas':
            load.pandas_loader(db_connector = target_engine, table_name = table, data = _temp2)

        # with target_db as target_connected:
        #     create_query = target_connected.get_query('create', table)
        #     print(create_query)
        #     with target_connected.conn.cursor() as target_cur:
        #         target_cur.executemany(create_query, result_all)
        #         target_connected.conn.commit()

# loop문을 짤 때는 중간에 shut down이 와도 지금껏 했던 데이터는 저장이 될 수 있도록 항상 장치를 해놔야 함!