# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

# batch_month = '201305'
queries = {
    'create': {
        'actor': '''
            INSERT INTO actor_back VALUES (%s, %s, %s, %s, %s)
            ;
        ''',
        'film': '''
            INSERT INTO film_back VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ;
        '''
		}
    }