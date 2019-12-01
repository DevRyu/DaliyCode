# 파이썬의 데이터 모델
# 네임드 튜플
# 네임드 튜플 attr
# 네임드 튜플 method
# 리스트 컴프리헨션
# 구조화된 모델 설명

# Insight 



# 파이썬의 중요한 핵심 프레임워크는 시퀀스(seq),반복(iter),함수(fun),클래스(cla) 라고 해도 과언이 아닙니다.
# 여기서 시퀀스
# 시퀀스의 예제는 리스트 구조입니다.
# 반복(iter)의 예는 for i in 리스트 처럼 반복이 되는 구조입니다.

# 객체란 파이썬의 데이터를 추상화 한 것 예) a ='apple' # a는 사과야~ 파이썬아~
# 모든 객체는 id,type,value를 가진다.

# 일반적인 튜플과 네임스페이스의 차이
# 튜플: 속성이 처음 생성 이후 수정이 되지 않는 것
# 키가 없어서 인덱스 슬라이싱으로 접근 된다.
# 두점 사이의 거리를 구하는 공식

a1 = (1.0, 5.0)
a2 = (2.0, 8.0)

from math import sqrt

line = sqrt((a2[0]-a1[0]) ** 2 + (a2[1] - a1[1]) ** 2)

print('line : ', line) # line :  3.1622776601683795

# 위의 단점은 x,y축을 알아보기 힘들고 다른 사람들이 보기에 가독성이 떨어진다. 

# 네임드 튜플 사용시
# 튜플의 값에 이름을 주는 것 이다.

from collections import namedtuple

# 첫번째 인자는 객체의 오브젝트의 가짜 이름이고 
# 두번째인자는 실제로 튜플의 개수에 맞춰 받을 파라미터를 정의하는 것이다.
Point = namedtuple('Point', 'x y')

p1 = Point(1.0, 5.0)
p2 = Point(2.0, 8.0)

# X,Y가 명시가 되어 구분하기가 편해 진다.
line2 = sqrt((p2.x-p1.x) ** 2 + (p2.y - p1.y)**2)

print('line2 : ', line2) # line2 :  3.1622776601683795

# 값을 비교하면 어떨까?
# 당연히 True로 리턴이 된다.
print('line_compare : ', line == line2) # True

# 네임드 튜플을 선언하는 법 4가지

# 리스트로 파라미터를 넣어줄수도 있고
Point1 = namedtuple('Point', ['x', 'y'])

# 문자열 내에서 콤마로 구분 지어 줄수도 있고
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')

# 파라미터 명이 중복되면 rename으로 구분되게 재사용 할수 있게 해준다. 
# class는 저장된 예약어 인데? 어떻게 될까?
Point4 = namedtuple('Point', 'x y x class', rename = True) # 리네임은 디폴트가 False

# 출력 해보자
print('named tuple methods', Point1, Point2, Point3, Point4) #  named tuple methods <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>

# 인자를 넣는 여러가지 방법
# 객체를 생성후 출력 해보자

# x y를 명시해줘도 된다
p1 = Point1(x = 10, y = 35)

# 갑많 넣어줘도
p2 = Point2(20, 40)

# y를 명시해줘도
p3 = Point3(45, y = 20)

# 중복되는 x는 _2로 예약어인 class는 _3으로 자동으로 치환해서 만들어준다 
p4 = Point4(10, 20, 30, 40) # Point(x=10, y=20, _2=30, _3=40) 
print('objected namedtuple', p1, p2, p3, p4) # objected namedtuple Point(x=10, y=35) Point(x=20, y=40) Point(x=45, y=20) Point(x=10, y=20, _2=30, _3=40)

# 딕셔너리를 언패킹하여 네임드스페이스에 넣어 줄 수도 있다.
temp_dict = {'x': 70, 'y': 35}
p5 = Point3(**temp_dict)

print('unpacked_dict_namedtuple : ', p5) # unpacked_dict_namedtuple :  Point(x=70, y=35)

# 네임드 튜플은 인덱스로도 접근이 된다.
# 이렇게 쓸거면 네임드 튜플을 쓸 이유는 없긴 하다.
print('index work? :', p1[0] + p2[1]) # index work? : 50

#네임드 튜플 답게 쓰기
print('namedtuple work? :', p1.x + p2.y) # index work? : 50

# 네임드 튜플을 언패킹을 하게되면 어떻게 될까?
# 각자의 값으로 (int,str) 반환 된다.
x, y = p1
print(type(x)) # <class 'int'>
print(x,y) # 10 35

# 네임드 튜플에 메소드는 어떤것이 있을까?



# make() : 새로운 객체를 생성하는 메서드
t = [52, 38]
# t라는 리스트 값을 집어 넣어준다. 리스트는 시퀀스,이터러블등 대체로 모든 기능을 가진 데이터 구조 
pp1 = Point1._make(t)
# 그냥 언패킹 할 때와 차이는 무엇일까? 
pp2 = Point1(*t)
# 차이는 없고 알아서 들어간다.
print(pp1, pp2) # Point(x=52, y=38) Point(x=52, y=38)
print("pp1, pp2 values are same?", pp1 == pp2 ) # True


# _fields : 네임드 튜플의 필드네임(키) 확인하는 메서드
print(p1._fields, p2._fields) # ('x', 'y') ('x', 'y')

# _asdict() : OrderedDict(정렬된딕셔너리)를 반환하는 메서드 

print(p1._asdict)  # <bound method Point._asdict of Point(x=10, y=35)>
# 반환되는 값은 메서드이지 딕셔너리가 아니다!!
print(type(p1._asdict)) # <class 'method'>

# 딕셔너리 형태로 또 바꾸어줘야한다.
print(dict(p1._asdict())) # <class 'dict'> 

# _replace() : 수정된 새로운 객체를 반환한다. 
# 이 메서드의 존재 이유는 튜플이 바뀌는 속성이 없어서 사용되어 진다!
print('replaced_namedtuple :', p2._replace(y=999)) # replaced_namedtuple Point(x=20, y=999)
