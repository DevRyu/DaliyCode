# 파이썬 참조

# 파이썬 객체 참조 다양한 특징
# Copy
# Deepcopy
# 매개변수 전달시 주의할점



# 현재 파일에 대한 상태, 속성값를 보여준다.
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(__name__) # __main__


# 서로 비슷해 보이는 변수의 id를 __eq__ 로 증명해보자

# 얕은 복사 Copy

x = {'name': 'ryu', 'age' : 20} # 140465038699488 140465038699488
y = x

print( id(x), id(y)) # 140465038699488 140465038699488
print( x == y ) # True  값 비교
print( x is y) # True 아이디 비교
print( x , y)  # {'name': 'ryu', 'age': 20} {'name': 'ryu', 'age': 20}

x['class'] = 10
print( x,y) # {'name': 'ryu', 'age': 20, 'class': 10} {'name': 'ryu', 'age': 20, 'class': 10}
# 모든 아이디,값이 같다. 심볼릭 링크와 비슷한 개념

z =  {'name': 'ryu', 'age': 20, 'class': 10}

print(x is z)
print( id(x), id (x)) # 아이디 값만 다르고 값은 다 같다

# 객체 생성 후 완전 불변 -> 즉 id는 객체 주소(정체성)비교, ==(eq)는 값비교 
# 그래서 같은 것인지 비교하고 싶을때 id를 비교하는 is를 먼저 쓰는 것을 파이썬에서 공식적으로 추천한다.

# 튜플 비교

tu1 = (10,12,13)
tu2 = (10,12,13)
print(id(tu1),id(tu2)) # 튜플 또한 마찬가지 이다.

# Deepcopy

# 리스트를 예를 들어보자

list1 = [10, 20, 30]
list2 = list1
list3 = list(list1)

print(list3) # [10, 20, 30]

print(list1 == list2) # T
print(list1 is list2) # T
print(list1 == list3) # T
print(list1 is list3) # F  왜냐하면 리스트 생성자(list())로 복사했기 때문에 된다. 
print(id(list1), id(list2), id(list3)) # 140013498581552 140013498581552 140013497224880