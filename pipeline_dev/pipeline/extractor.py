# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

import pandas as pd

def cursor_extractor(db_connector, table_name, batch_month):

    with db_connector as connected:
            read_query = connected.get_query('read', table_name, {'batch_month' : batch_month})
            with connected.conn.cursor() as cur:
                cur.execute(read_query)
                result_all = cur.fetchall()
                return result_all

def pandas_extractor(db_connector, table_name, batch_month):

    with db_connector as connected:
            read_query = connected.get_query('read', table_name, {'batch_month' : batch_month})
            with connected.conn as conn:
                pdf = pd.read_sql(read_query, conn)
                return pdf


# 방식이 다른 두가지 extractor...

# def extractor(db_connector, table_name, batch_month, read_option):
#     if read_option == 'cursor':
#         with db_connector as connected:
#             read_query = connected.get_query('read', table_name, {'batch_month' : batch_month})
#             with connected.conn.cursor() as cur:
#                 cur.execute(read_query)
#                 result_all = cur.fetchall()
#                 return print(result_all[:2])

#     elif read_option == 'pandas':
#         with db_connector as connected:
#             read_query = connected.get_query('read', table_name, {'batch_month' : batch_month})
#             with connected.conn as conn:
#                 pdf = pd.read_sql(read_query, conn)
#                 return print(pdf[:2])


# def extractor(db_connector, table_name, batch_month):

#     with db_connector as connected:
#             read_query = connected.get_query('read', table_name, {'batch_month' : batch_month})
#             with connected.conn.cursor() as cur:
#                 cur.execute(read_query)
#                 result_all = cur.fetchall()

# insert into 하는 부분
#             with target_db as target_connected:
#                 create_query = target_connected.get_query('create', table)
#                 print(create_query)
#                 with target_connected.conn.cursor() as target_cur:
#                     target_cur.executemany(create_query, result_all)
#                     target_connected.conn.commit()