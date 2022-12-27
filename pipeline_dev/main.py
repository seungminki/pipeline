# 작성자 : 기승민
# 작성일 : 2022-12-26
# 내용 : localhost_postgre

# 실행하는 법 : python main.py
# 결과창 : 
# (py38) PS C:\Users\user\Documents\smkim\pipeline\pipeline_dev> python main.py
# start_batch > batch_month :  202211

import sys
import click
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
import settings
from pipeline import controller



# @click.option('--upload-only', is_flag=True, help='업로드만진행할경우')
# @click.option('-dm', '--custom-delete-month', type = click.STRING, default='', help='삭제작업연월')

@click.command()
@click.option('-m', '--custom-batch-month', type = click.STRING, default='', help='배치작업연월')
def start_batch(custom_batch_month):
    batch_month = _get_batch_month(custom_batch_month)
    print('start_batch > batch_month : ', batch_month)
    if not batch_month:
        sys.exit(1)
    try:
        controller.etl(batch_month)
    except Exception as e:
        print(e)
        sys.exit(1)
    sys.exit(0)

def _get_batch_month(custom_batch_month):
    if custom_batch_month:
        print('custom_batch > batch_month : ', custom_batch_month)
        return _check_valid_month(custom_batch_month)

    first_day = datetime.today().replace(day = 1) # Day를 1로 변경
    batch_month = first_day - timedelta(days = 1) # Day를 1 더 뺌
    return batch_month.strftime('%Y%m')
    

# def _get_delete_month(custom_batch_month):
#     if custom_batch_month:
#         return _check_valid_month(custom_batch_month)

#     first_day = datetime.today().replace(day = 1)
#     delete_month = first_day + relativedelta(months = -13)
#     return delete_month.strftime('%Y%m')

def _check_valid_month(str_yyyymm):
    try:
        print(str_yyyymm)
        datetime.strptime(str_yyyymm, '%Y%m')
        return str_yyyymm
    except Exception as e:
        return None   


# 터미널에서 이름을 선언했을 때 메인함수가 실행되게함
if __name__ == '__main__':
    # print('hello') : 오 신기
    start_batch()

# 터미널에 clear라고 치면 결과값이 사라짐
# custom_batch_month를 넣으면 배치값이 따로 뜨고
# if문을 넣어서 custom_batch_month가 없으면 현재 datetime 값을 넣어서 결과값이 뜨게함.
