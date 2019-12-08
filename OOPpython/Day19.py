# nations.csv파일(39mb)을 이용하여 파이썬으로 사용합니다.

# Future 동시성
# 비동기 작업 실행
 
# 퓨처(asyncio.Future)는 미래에 할 일을 표현하는 클래스인데 할 일을 취소하거나 상태 확인, 완료 및 결과 설정에 사용합니다
# 태스크(asyncio.Task)는 asyncio.Future의 파생 클래스이며 asyncio.Future의 기능과 실행할 코루틴의 객체를 포함하고 있습니다. 태스크는 코루틴의 실행을 취소하거나 상태 확인, 완료 및 결과 설정에
# 데이터가 크고 적합한 작업일 경우 압도적인 성능 향상

# 만약 나라의 파일이 있다는 데이터를 가져와서 나라별로 저장을 하고 싶다면 어떨가요?

# 순차 실행으로 진행해 보겠습니다.

# 폴더 경로 설정
import os   # 폴더 경로
import sys  # 시스템 접근
import csv  # csv파일 오픈
import time # 시간 성능추천

# 가져올 국가 정보 구하기
COUNTRY      = ('Korea Japan Israel').split()

# 초기 csv 위치
LOCATION_CSV = '/home/ryu/repython/resources'

# 저장 폴더 위치
SAVE_CSV     = '/home/ryu/repython/csvs'

# csv 컬럼 정보 저장
COLUMNS      = []'Region','Country','Item Type','Sales Channel','Order Priority','Order Date','Order ID','Ship Date','Units Sold','Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']

def main(all_of_meta):
    # 시작 시간
    start_tm   = time.time()
    # 결과 건수
    result_cnt = seperate_many(COUNTRY)
    # 종료 시간


#실행
if __name__ == '__main__':
    main()


# concurrent.futures 방법1

# concurrent.futures 방법2
