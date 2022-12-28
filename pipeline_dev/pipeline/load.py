# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

def cursor_loader(db_connector, table_name, data):
    with db_connector as connected:
        create_query = connected.get_query('create', table_name)
        with connected.conn.cursor() as cur:
            cur.executemany(create_query, data)
            connected.conn.commit()
            print(f'insert > {table_name}')

def pandas_loader(db_connector, table_name, data):
    data.to_sql(table_name+'_back', db_connector, if_exists = 'append', index = False)
    print(f'insert > {table_name}')


    # with target_db as target_connected:
        #     create_query = target_connected.get_query('create', table)
        #     print(create_query)
        #     with target_connected.conn.cursor() as target_cur:
        #         target_cur.executemany(create_query, result_all)
        #         target_connected.conn.commit()


# sql table을 pandas dataframe으로 read 할 때, 주의해야 하는 dtype
# _dtype = pd.read_sql_query("""SELECT column_name, data_type FROM information_schema."columns" WHERE table_name = 'film';""", db_source._postgre_connect())
# _dtype

# _bool = _dtype[_dtype.data_type.str.contains('bit', regex = True)].copy()
# _bool['data_type'] = 'float64' # bit type을 True/False 값이 아닌 float 으로 초기 선언 (0.0, 1.0, null)
# # bool 선언시 null == False, int64 선언시 null 허용하지 않아 오류 남, Int64 선언시 bit type의 값이 True/False의 string으로 read 되어 integertype 으로 converting 불가

# _int = _dtype[_dtype.data_type.str.contains('tinyint|smallint|int|bigint|NUMBER', regex = True)].copy()
# _int['data_type'] = 'float64' # int type을 null 허용하는 float 으로 초기 선언 (float, null)
# # int64 선언시 null 허용하지 않아 오류 남, Int64 선언해도 되지만 안전성을 위해 float으로 초기값 선언

# _float = _dtype[_dtype.data_type.str.contains('float|real', regex = True)].copy()
# _float['data_type'] = 'float64'

# _datetime = _dtype[_dtype.data_type.str.contains('date|datetime|datetime2|DATE', regex = True)].copy()
# _datetime['data_type'] = 'datetime64'

# _dtype = pd.concat([_bool, _int, _float, _datetime])

# _pandas_df = pd.read_sql_query(_query, connected.conn, dtype = dict(_dtype.values))

# _pandas_df[_bool.COLUMN_NAME] = _pandas_df[_bool.COLUMN_NAME].astype(pd.Int64Dtype()) # float 으로 선언된 bool type을 null 허용하는 pd.Int64Dtype()으로 변환, np.int64 사용하면 null 허용하지 않아 오류 남
# _pandas_df[_int.COLUMN_NAME] = _pandas_df[_int.COLUMN_NAME].astype(pd.Int64Dtype()) # float 으로 선언된 int type을 null 허용하는 pd.Int64Dtype()으로 변환, np.int64 사용하면 null 허용하지 않아 오류 남
            
# for col in _pandas_df.select_dtypes('object').columns:
#     _pandas_df[col] = _pandas_df[col].astype(str)