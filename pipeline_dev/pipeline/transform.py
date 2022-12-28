# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre
def cost_check(cost):
    if cost > 20:
        return 'expensive'
    elif cost > 15:
        return 'middle'
    else:
        return 'cheap'

first_try = []
# replacement_cost
def data_trans(table_name, pdf):
    if table_name == 'actor':
        print('helloworld')
        print(pdf)
        print(type(pdf))
        first_try = pdf['first_name'].apply(lambda x : x+'_')
        print(first_try)
        first_try += pdf['last_name'].apply(lambda x : x)
        print(first_try)
        pdf['complete_name'] = '0'
        for i in range(len(pdf)):
            pdf['complete_name'][i] = first_try[i]

        print(pdf)
        return pdf


    elif table_name == 'film':
        print(pdf['replacement_cost'].max())
        print(pdf['replacement_cost'].min())
        print(pdf['replacement_cost'].median())
        print(type(pdf['replacement_cost'][1]))
        # 5 > cheap
        # 5 < < 20 middle
        # 20 >
        pdf['replacement_cost'] = pdf['replacement_cost'].apply(lambda x: cost_check(x))
        print(pdf['replacement_cost'])
        return pdf




# def pandas_loader(db_connector, table_name, data):
#     data.to_sql(table_name+'_back3', db_connector, if_exists = 'append', index = False)
#     print(f'insert > {table_name}')

# queries = {
#     'create': {
#         'actor': '''
#             INSERT INTO actor_back3 VALUES (%s, %s, %s, %s, %s)
#             ;
#         ''',
#         'film': '''
#             INSERT INTO film_back3 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             ;
#         '''
# 		}
#     }