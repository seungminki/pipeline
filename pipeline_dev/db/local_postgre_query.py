# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

# batch_month = '201305'
# queries = {
#     'read': {
#         'actor': f'''
#             SELECT * 
#             FROM actor 
#             WHERE TO_CHAR(CAST(last_update AS DATE), 'YYYYMM') = '{batch_month}'
#             ;
#         ''',
#         'film': f'''
#             SELECT * 
#             FROM film 
#             WHERE TO_CHAR(CAST(last_update AS DATE), 'YYYYMM') = '{batch_month}'
#             ;
#         '''},
#     'insert': {
#         'actor': '''
#             INSERT INTO ~~~
#         ''',
#         'film': '''
#             INSERT INTO ~~~
#         '''},
#     }