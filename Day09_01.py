#    Chapter 03. Sequence - 02. Advanced List & Tuple - 2


# 튜플 컴프리헨션(지능형 튜플)을 만들어 보자

tuple_ = (i for i in range(10))
print(type(tuple_)) # <class 'generator'> 제너레이터가 나온다?
print(tuple_)       # <generator object <genexpr> at 0x7f59a067ead0>
# Generator : 한 번에 한 개의 항목을 생성하므로 메모리에서 데이터를 유지하지 않아도 됨
# 이미 메모리에 변수를  올려 놓은 다른 자료 형보다 빠르다.
print(next(tuple_)) # 0
print(next(tuple_)) # 1
print(next(tuple_)) # 2



# 이와 같이 그냥 제너레이터 가 나오므로 
# 아래처럼 tuple의 경우 tuple()로 감싸 주어야 한다.
tuple_real = tuple(i for i in range(10))
print(type(tuple_real))
print(tuple_real)   # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)



# 어레이 컴프리헨션 (지능형 어레이)을 써보자.
# 한개의 자료형을 사용할 때는 컨테이인 튜플,리스트보다  플랫형인 어레이가 더 좋다.
import array
# array('타입코드(예약어자료 형:b, B, u, h, H, i, I, l, L, q, Q, f or d)',  (어레이 컴프리헨션 ))
array_ = array.array('I', (i for i in range(10)))
print(array_)        # array('I', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(array))   # <class 'module'>
print(array_.tolist) # 어레이를 리스트로 자료형 변환 # <built-in method tolist of array.array object at 0x7f58fdca6e30>

# List, Array사이 에서 적합한 자료형을 사용하는 방법

# 리스트의 사용할 때 고려사항 : 컨테이너형(융통성, 다양한 자료형, 범용적 사용)
# 어레이의 사용할 때 고려사항 : 플랫형(숫자만 사용시) (리스트의 거의 모든 연산 지원)



# 리스트컴프리핸션 시  주의할 점
# 아래의 두개는 같아 보일 수 있어도 다르다.
list_com = [['1'] * 3 for n in range(3)] # 내부 깊은 복사
list_mul = [['1'] * 3] * 3               # 내부 얕은 복사


print('first', list_com)  # first [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']]
print('second', list_mul) # second [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']]


# 수정하기
list_com[0][1] = 'X'
list_mul[0][1] = 'X'

print('first', list_com)  # first [['1', 'X', '1'], ['1', '1', '1'], ['1', '1', '1']]

# 원하지 않는 값이 변경되었다.
print('second', list_mul) # second [['1', 'X', '1'], ['1', 'X', '1'], ['1', 'X', '1']]

# 아이디값 확인
print('first', [id(i) for i in list_com]) # 새로운 자료 공간을 만들고 값을 넣는다. first [140177547086816, 140177547086736, 140177547086656]
print('second', [id(i) for i in list_mul]) # 기존의 자료 공간을 여러개로 복사한다 second [140177547086576, 140177547086576, 140177547086576]


# 튜플에서의 패킹 언패킹
# 패킹은 여러개의 객체를 묶어서 자료형으로 선언 해 주는 것이고
# 언패킹은 여려개의 객체가 들어 간 자료 형을 *로 풀어주는 것이다. (가변 파라미터 *,키워드 파라미터 ** 의 개념과 같다)
# divmod(a,b) a를 b로 나누는 함수이고 결과는 몫과 나머지로 return한다.

# a,b를 넣어줘도 되고
print(divmod(100, 6))    # (16, 4)
# 튜플자체를 씌운 자료형을 *를 붙여줌으로 언패킹을한다.   
print(divmod(*(100, 6))) # (16, 4)

# 이런식으로도 사용가능하다.
i, j, *k = range(10)

# 함수에서 가변 파라미터는 리스트와 튜플을 받을수 있지만.
# 기본형으로 k는 리스트로 반환한다.
print(i, j , k) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9] 

# 일단 받고 튜플로 k를 바꾸어 주어도 된다.
i, j, *k = range(10)
print(i, j , tuple(k)) # 0 1 (2, 3, 4, 5, 6, 7, 8, 9)


# 파이썬에서의 Mutable(가변) vs Immutable(불변)
# 기본적으로 Mutable은 같은 주소(id)에서 값이 변경 가능하므로 얕은 복사가 진행 될 수도 있다..
# Immutable은 내부의 값들이 변경이 불가능하 므로 자료 공간을 재배정함으로 얕은 복사가 일어 나지 않는다.(무조건 깊은 복사가 일어난다)
# 나무위키
# 파이썬의 객체는 변경 불가능한 객체(Immutable Object)와 변경 가능한 객체(Mutable Object)로 나뉘며, 변경 불가능한 객체에는 상수, 문자열, 그리고 튜플[5]이 있다. 이 세 가지를 제외한 나머지 객체는 모두 변경 가능한 객체이며, 값을 수정할 수 있다. 변경 불가능한 객체의 값을 수정할 때는 바뀐 값이 저장된 새로운 객체를 생성하고 해당 객체를 참조한다. 이와 같은 특징 때문에 파이썬은 순수 객체지향 언어라고 한다.
# 함수의 매개변수로 Immutable 객체를 넘겼냐 Mutable 객체를 넘겼냐에 따라서 함수 바깥에 있는 인자의 값도 수정할 수 있는지 없는지가 달라진다. Immutable 객체를 넘겼으면 값의 복사만 일어나고 함수 바깥에는 영향을 주지 못하므로[6] '값에 의한 호출(Call by Value)'이 될 것이며, Mutable 객체를 넘겼으면 함수 바깥에까지 영향을 줄 수 있으므로 '참조에 의한 호출(Call by Reference)'이 될 것이다. 파이썬 공식 문서에서는 파이썬의 인자 전달 방식을 '할당에 의한 호출(Call by Assignment)', 또는 '객체 참조에 의한 호출(Call by Object Reference)'
# python 3내부적으로 모든 문자열을 유니코드
tuple_ = (10, 15, 20)
list_ = [10, 15, 20]

print('tuple', tuple_, id(tuple_)) # tuple (10, 15, 20) 140312517195888
print('list', list_, id(list_))  # list [10, 15, 20] 140312516811664


tuple_ = tuple_ * 2
# 일반 대입 산술 연산자시 깊은 복사
list_ = list_ * 2

print('tuple', tuple_, id(tuple_)) # tuple (10, 15, 20, 10, 15, 20) 140312517351584
print('list', list_, id(list_))  # list [10, 15, 20, 10, 15, 20] 140312516811104


tuple_ *= 2
# 할당 연산자 (+= *=) 사용시 얕은 복사가가 일어난다.  
list_ *= 2

print('tuple', tuple_, id(tuple_)) # tuple (10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20) 140312517714640
print('list', list_, id(list_))  # list [10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20] 140312516811104

# 그러므로 사용자의 의도에 맞게 가변형 자료형(특히 리스트)을 사용할 때는 주의를 해야한다.




# sort() vs sorted() 파이썬 함수의 차이
# sort   : 정렬 후 객체 직접 변경
# sorted : 정렬 후 새로운 객체(새로운 id) 반환
# 옵션 : reverse = True 거꾸로 값을 반환
#            key = 내장 함수 기준으로 정렬(len[길이별],lambda,str.upper등) 

# sorted : 정렬 후 새로운 객체 반환 (원본의 객체가 변환되지 않음)
# 깊은 복사의 개념
sorted_ = ['6','3','7','4','7','22','1','0','20']

print('sorted()', sorted(sorted_))              # sorted() ['0', '1', '20', '22', '3', '4', '6', '7', '7']
print('reverse', sorted(sorted_, reverse=True)) # reverse ['7', '7', '6', '4', '3', '22', '20', '1', '0']
print('key=len', sorted(sorted_, key=len))      # key=len ['6', '3', '7', '4', '7', '1', '0', '22', '20']
print('key=lambda', sorted(sorted_, key=lambda x: x[-1])) # key=lambda ['0', '20', '1', '22', '3', '4', '6', '7', '7']
print('key=lambda, reverse', sorted(sorted_, key=lambda x: x[-1], reverse=True)) # key=lambda, reverse ['7', '7', '6', '4', '3', '22', '1', '0', '20']
print('origin sorted_', sorted_) # origin sorted_ ['6', '3', '7', '4', '7', '22', '1', '0', '20']


# sort : 정렬 후 원래의 객체 변경 되어짐 
# sort()의 return은 None
# 얕은 복사의 개념
sort_ = ['6','3','7','4','7','22','1','0','20']

print('sort_.sort(), sort_', sort_.sort(), sort_)           # sort_.sort(), sort_ None ['0', '1', '20', '22', '3', '4', '6', '7', '7']
print('reverse=True', sort_.sort(reverse=True), sort_)      # reverse=True None ['7', '7', '6', '4', '3', '22', '20', '1', '0']
print('key=len', sort_.sort(key=len), sort_)                # key=len None ['7', '7', '6', '4', '3', '1', '0', '22', '20']
print('key=lambda', sort_.sort(key=lambda x: x[-1]), sort_) # key=lambda None ['0', '20', '1', '22', '3', '4', '6', '7', '7']
print('key=lambda, reverse', sort_.sort(key=lambda x: x[-1], reverse=True), sort_) # key=lambda, reverse None ['7', '7', '6', '4', '3', '22', '1', '0', '20']

