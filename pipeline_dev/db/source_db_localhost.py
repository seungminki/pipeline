# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

# batch_month = '201305'
queries = {
    'read': {
        'actor': '''
            SELECT '{batch_month}' AS YYYYMM, *
            FROM actor 
            WHERE TO_CHAR(CAST(last_update AS DATE), 'YYYYMM') = '{batch_month}'
            ;
        ''',
        'film': '''
            SELECT '{batch_month}' AS YYYYMM, *
            FROM film 
            WHERE TO_CHAR(CAST(last_update AS DATE), 'YYYYMM') = '{batch_month}'
            ;
        '''
        }
    }