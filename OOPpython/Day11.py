# 불변형 딕셔너리(immutable Dict)
# MappingProxyType : 읽기 전용 딕셔너리 python 3.3이상 부터 사용가능 합니다.
# 수정/삭제를 원할시 직접 객체를 복사하여 수정해야합니다.
# 변경되지 않는 딕셔너리를 사용하고 싶을 때 사용합니다.
from types import MappingProxyType

a = {'a': 'b'}

m_p_t = MappingProxyType(a)

print(a, id(a)) # {'a': 'b'} 139807377881760
print(m_p_t, id(m_p_t)) # {'a': 'b'} 139807377195856
print('id equal:', a is m_p_t,'values equal:', a == m_p_t) # id equal: False values equal: True

# MappingProxyType는 수정 불가하지만 원래 딕셔너리는 수정 가능합니다.

a['c'] = 'd'

print(a) # {'a': 'b', 'c': 'd'}


# 불변형 set(immutable set)
# frozenset으로 read만 가능 합니다.

# 셋 선언 방식 4가지 (중복은 알아서 제거됨)
s1 = {'a', 'b', 'c', 'd', 'a'}
s2 = set(['a', 'b', 'c', 'd', 'a'])
s3 = {'a'}
s4 = set() 
# frozenset 선언방식
s5 = frozenset({'a', 'b', 'c', 'd', 'a'})

# 일반적인  set에서는 추가가 가능합니다.
s1.add('f')
print(s1,type(s1)) # {'a', 'd', 'b', 'f', 'c'} <class 'set'>
# frozenset은 추가 불가
# s5.add('Melon')

print('s1', s1,'type:', type(s1))
print('s2', s2,'type:', type(s2))
print('s3', s3,'type:', type(s3))
print('s4', s4,'type:', type(s4))
print('s5', s5,'type:', type(s5))

# s1 {'a', 'd', 'b', 'f', 'c'} type: <class 'set'>
# s2 {'b', 'c', 'd', 'a'} type: <class 'set'>
# s3 {'a'} type: <class 'set'>
# s4 set() type: <class 'set'>
# s5 frozenset({'b', 'c', 'd', 'a'}) type: <class 'frozenset'>

# 어떠한 자료형이든 선언할 시 자료형 함수를 쓰는 것 보다
# 자료형의 괄호를 써주는게 더 빠릅니다.
# 어셈블리로 비교해 봅시다.

from dis import dis

print(dis('{1}'))
#   1           0 LOAD_CONST               0 (1)
#               2 BUILD_SET                1
#               4 RETURN_VALUE
# None
print(dis('set([1])'))
#   1           0 LOAD_NAME                0 (set)
#               2 LOAD_CONST               0 (1)
#               4 BUILD_LIST               1
#               6 CALL_FUNCTION            1
#               8 RETURN_VALUE
# None

# 셋 컴프리 헨션(Set Comprehension)
# 지능형 집합의 구조 { i || 반복문 || 조건문}입니다.


q = { i for i in range(10)}
print(type(q)) # <class 'set'>
print(q)       # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}