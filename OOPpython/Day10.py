# Chapter03-2
# 파이썬 심화


# 시퀀스형
# 파이썬의 핵심엔진은 딕셔너리 형태로 이루어져 있다.
# 파이썬은 이 딕셔너리의 해시테이블(hashtable)을 사용 -> 해시 태이블내 해시값(숫자)로 같은지 아닌지 판별
# -> 적은 리소스로 많은 데이터를 효율적으로 관리 -> 색인기능, 고성능
# Dict자료형 -> Key만 중복 허용 하지 않는다 
# Set -> 중복 허용하지 않는다.
# 함수형들도 거의 대부분 딕셔너리(Dict) 구조 이다.
# print(__builtins__.__dict__) # 로 확인 할수 있다.

# Hash 값 확인
t1 = (10, 20, (30, 40, 50)) # 튜플안의 튜플
t2 = (10, 20, [30, 40, 50]) # 튜플안에 리스트

# 튜플안의 리스트는 리스트값이 항상 변함으로(중복을 허용함으로(mutable)) 해쉬 값이 존재하지 않음
# 해쉬값은 중복을 허용하지 않는다.
# hash() 해쉬값이 있는지 없는지 해쉬값 함수

print('hash : ',  hash(t1)) # hash :  5737367089334957572
# print(hash(t2)) # 에러난다 mutable한 리스트가 있으므로

# 딕셔너리 컴프리핸션

# 리스트안의  튜플구조로 있으면
ex_list = [('Afghanistan','AF'),('Åland Islands','AX'),('Albania','AL')]
tuple_  = { c: code for c, code in ex_list} 
# 지
print(tuple_) # {'Afghanistan': 'AF', 'Åland Islands': 'AX', 'Albania': 'AL'}

# 딕셔너리 setdefault 사용하기
source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))
 ㅠ