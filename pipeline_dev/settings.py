# 작성자 : 기승민(fsjki0328@naver.com)
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

DB_SETTINGS = {
    'localhost_postgre_query' : {
        # 'location' : 'localhost',
        # 'engine' : 'postgre',
        'host' : "127.0.0.1",
        'port' : "5432",
        'user' : "postgres",
        'password' : "0328",
        'database' : "dvdrental"
    },
    'source_db_localhost' : {
        'location' : 'localhost_source',
        'host' : "127.0.0.1",
        'port' : "5432",
        'user' : "postgres",
        'password' : "0328",
        'database' : "dvdrental",
        'engine' : 'postgre'
    },
    'target_db_localhost' : {
        'location' : 'localhost_target',
        'host' : "127.0.0.1",
        'port' : "5432",
        'user' : "postgres",
        'password' : "0328",
        'database' : "sample",
        'engine' : 'postgre'
    }
}
