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

# 딕셔너리의 setdefault 사용하기

# 딕셔너리(immutable)는 키가 hashable해야 함으로 중복이 허용이 안된다.
# 하지만 값만 중복을 허용하도록 저장하고 싶다면?
# 일단 튜플내 튜플형태로 중복되는 자료형을 만든다. 
source = (  ('key_1', 'value1'),
            ('key_1', 'value2'),
            ('key_1', 'value1'),
            ('key_2', 'value3'),
            ('key_2', 'value4'),
            ('key_2', 'value5'),
            ('key_3', 'value5')
            )

empty_dict = {}

# 딕셔너리의 setdefault 미 사용시의 해결 법
# values를 리스트 형태로 해결 (json형태)
for k, v in source:
    # 키가 이미 있다면 리스트로 만들어줄 append 메서드 사용
    if k in empty_dict:
        empty_dict[k].append(v)
        # 없으면 그냥 리스트로 추가
    else:
        empty_dict[k] = [v]

print(empty_dict) # {'key_1': ['value1', 'value2'], 'key_2': ['value3', 'value4', 'value5'], 'key_3': ['value5']}

# 딕셔너리의 setdefault 사용시
# 구조 : 딕셔너리.setdefault(키,벨류받을 자료형 형식).append(벨류)
empty_dict2 = {}

for k, v in source:
    empty_dict2.setdefault(k,[]).append(v)
print(empty_dict2) # {'key_1': ['value1', 'value2'], 'key_2': ['value3', 'value4', 'value5'], 'key_3': ['value5']}

# 데이터양이 많은 json타입의 데이터 처리시
# setdefault에서의 분기문을 안쓰고 성능을 올릴 수 있다.

# 사용자 정의 딕셔너리(dict 상속 받기)만들기
# 실제 딕셔너리가 어떻게 동작하는지 알아 보자
class PrivateDict(dict):
    # 참조 
    # https://docs.python.org/3/library/stdtypes.html#dict
    # https://docs.python.org/3/library/collections.html#collections.defaultdict
    # __missing__은 딕셔너리의 서브클래스고 키가 없을시 키 에러를 발생 시키고 
    # 키가 있으면 str(key)로 감싸서 리턴해준다.
    # 사용자 정의 딕셔너리를 만들기 위해 꼭 선언해 주어야 한다.  

    def __missing__(self, key):
        print('__missing__ is working')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # __getitem__과 같은 역할 get을 사용할때
    def get(self, key, default=None):
        print('__getitem__ is working')
        try:
            return self[key]
        except KeyError:
            return default
    # in(연결연산자)연산자 사용시 포함이 되어 있는지 확인하는 메서드
    def __contains__(self, key):
        print('__contains__ is working')
        return key in self.keys() or str(key) in self.keys()

private_dict1 = PrivateDict(one=1, two=2) # 값을 할당해도 됨
private_dict2 = PrivateDict({'one': 1, 'two': 2}) # 딕셔너리 형태로 인자를 넣어도 됨
private_dict3 = PrivateDict([('one',1),('two',2)]) # 튜플 형태로 분리해서 넣어줘도 됨

# 출력
print(private_dict1, private_dict2, private_dict3) #{'one': 1, 'two': 2} {'one': 1, 'two': 2} {'one': 1, 'two': 2}
print('private_dict2.get', private_dict2.get('two'))

# 클래스내 get()으로 실행합니다.
# __getitem__ is working
# private_dict2.get 2

print('one in private_dict3', 'one' in private_dict3)
# in은  __contains__을 실행합니다.
# __contains__ is working
# one in private_dict3 True

print('private_dict3.get', private_dict3.get('three'))
# 일단 get을 실행합니다.
# __getitem__ is working
# 키가 없으므로  파이썬 내부적으로 __missing__(오버라이딩된)을 실행합니다.
# __missing__ is working
# 키값의 형태를 보고 return self[str(key)]이 실행됩니다.
# private_dict3.get None

print('three in private_dict3', 'three' in private_dict3)
# __contains__ is working
# three in private_dict3 False


# print(private_dict3['three'])
# 키에러가 발생
# __missing__ is working
#     raise KeyError(key)
# KeyError: 'three'




# 여기서 중요한 것은 
# 1. get('키')메서드 사용시 값이 있으면 값 리턴 없으면 None 리턴하지만
#    a['b']키 인덱스로 접근시 없으면 KeyError를 발생시키고

# 2. 오버라이딩으로 사용자가 재정의 하여 딕셔너리의 구조를 변경 시켜서 본인의 프로젝트에
#    맞게 수정이 가능 하다는 것 이다.




