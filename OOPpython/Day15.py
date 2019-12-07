# 5-4 파이썬 클래스 관련 특별 메소드 심화 활용 및 상속

# Private 속성 실습
# __slot__ 예제
# 객체 슬라이싱, 인덱싱
# ABC, 상속, 오버라이딩


# 파이썬 언더스코어 사용하는 이유 
# 1. 인터프리터에서 마지막 값을 저장
# 10
# _*10 
# _/10
# 2. 값을 무시하고 싶을때
# i,_,j = 1,2,3
# i # 1
# j # 3
# a = 1
# for _ in range(5):
#    print(a)

# 3. 변수나 함수명에 특별한 의미를 부여하고 싶을때
# 1) 폴더안에 __init__.py 파일 존재시 폴더를 패키지로 사용가능
# 2-1) _변수    : 외부(module)에서 사용이 불가하고 파일내에서만 직접 접근가능
# 2-2) __변수   : 완전 private 직접접근 불가,
#                 맹글링(변수나 함수명을 일정한 규칙으로 변형)하기 위해서이다.
#                 하지만 인스턴스._클래스(객체명)__변수명 으로 접근이 가능하다 
#                 어렵게 접근하게 함으로 직접접근 또는 외부에서의 값 변경을 막기위한 용도이다.
# 3-1) _메소드  : 외부(module)에서 사용이 불가하고 파일내에서만 직접 접근가능
# 3-2) __메소드 : 매직 매소드 이거나 

# 4. 숫자 리터럴 값의 자릿수 구분을 하고 싶을때 
# print(1_000)
# print(1_000_000)

# 5. 변수 표기법(snake_case 표기법)




# 객체지향프로그래밍의 특징 : 추상화,캡슐화,은닉화,상속성(재사용성),다형성

# 객체지향 개발 5대 원칙 : SOLID (나중에 따로 포스팅 할 예정)
# 1.SRP(Single Responsibility Principle)     : 단일 책임의 원칙
# 2.OCP(Open Close Principle)                : 개방폐쇄의 원칙
# 3.LSP(The Liskov Substitution Principle)   : 리스코브 치환의 원칙
# 4.ISP(Interface Segregation Principle)     : 인터페이스 분리의 원칙
# 5.DIP(Dependency Inversion Principle)      : 의존성 역전의 원칙

# 실수형 x,y를 받고 값을 읽거나 수정하되 객체지향의 특징인 추상화 , 캡슐화, 은닉화, 상속성의 개념을 적용하여
# 클래스를 작성을 하라

# class 선언 object(메타 클래스, 기본적으로 상속 받음)

# 객체 지향적이지 못하게 짠 코드 예시 1

class VetorProj(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    
    # 반복 메서드(이터레이터)
    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # 증감 메서드(제너레이터)

# 객체 선언
v = VetorProj(20,40)

# '인스턴스.__변수(맹글링)'에 직접 접근하면 어떻게 될가?
# 당연히 접근을 하지 못하게 된다.
# print(v.__x, v.__y) # AttributeError: 'VetorProj' object has no attribute '__x'



# 객체 지향적이지 못하게 짠 코드 예시 2

# class 선언 object(메타 클래스, 기본적으로 상속 받음)
class VetorProj2(object):
    def __init__(self, x, y):
        self._x = float(x)

        # y값을 10이하만 되도록 고쳐보자
        if y > 10:
            raise ValueError('y must be under 10')
        self._y = float(y)
    
    # 반복 메서드(이터레이터)
    def __iter__(self):
        return (i for i in (self._x, self._y)) # 증감 메서드(제너레이터)

# 객체 선언 
# 인스턴스 생성시 if 조건문 y 10미만만 됨
v2 = VetorProj2(20,5)
 
print(v2._x, v2._y)  # 20.0 5.0

# 하지만 v2._y 직접 접근시 위의 if문 값을 체크하지 않고 바뀐다.
v2._y = 15

# 심지어 float타입 조차도 int 타입으로 자료형까지 바뀐다.
print(v2._x, v2._y) # 20.0 15

# iter확인
for i in v2: # 20.0 15
    print(i) 

# 위의 코드는 객체지향의 캡슐화, 정보 은닉에 위배가 된다.
# 그래서 일반적인 메서드 내에서 if else 로직으로 문제를 해결할려고 하는 것은 좋지 못하다.

# 객체 지향적에 가까운 클래스
# Getter(read), Setter(write)를 사용하는 property 데코레이터로 코딩으로 해주는게 좋다.

class VetorProj3(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    
    def __iter__(self):
        return (i for i in (self._x, self._y)) # 증감 메서드(제너레이터)

    # __private 변수의 경우 클래스내 로직을 property로 선언과 리턴함수 선언시 값의 직접 접근 가능해짐,
    # 또한 인스턴스 변수 은닉화 시켜준다
    # 이것이 getter임 
    
    @property
    def x(self):
        print('getter')
        return self.__x

    # setter를 사용하기 전에 getter(위의 함수)를 먼저 선언 해 주어야 한다.
    
    @x.setter
    def x(self, v):
        print('setter')
        
        # 어떠한 값이 들어와도 float 자료형의 일관성을 지키기 위해 float() 
        self.__x = float(v) 

    @property
    def y(self):
        print('getter')
        return self.__y
    
    # 위에서 잘못된 예시에서의 if문으로의 y변수 제약을  여기서 사용할 수 있다.
    @x.setter
    def y(self, v):
        print('setter')
        if v > 10:
            raise ValueError('y must be under 10')

        # 어떠한 값이 들어와도 float 자료형의 일관성을 지키기 위해 float() 
        self.__y = float(v) 

v3 = VetorProj3(20, 5)

# dir() 함수로  언더스코어로 은닉되었다는  '_VetorProj3__x', '_VetorProj3__y'가 안에 있는것을 확인할수 있다
# v._VetorProj3__x 이런식으로 접근을 할 수 있다.
print(dir(v3)) # ['_VetorProj3__x', '_VetorProj3__y', ' 'x', 'y'] @프로퍼티때문에 x,y가 다시 존재한다.
print(v3.__dict__) # 딕셔너리 형태로 확인 가능하다. {'_VetorProj__x': 20.0, '_VetorProj__y': 40.0}
print(v3._VetorProj3__x)

print(v3.x) # 20.0 # getter 다시 .x를 접근을 가능해지고
v3.x = 10.0 # setter 직접 접근하면
print(v3.x) # 10.0 # getter 수정 된 것이 확인 가능하다 . (하지만 직접 접근)

print(v3.y) # 5 # getter
# 에러코드 호출 됨으로 직접 접근시 값이 조건을 무시한체 수정되는 것을 막을 수 있다.
# v3.y = 20 # ValueError: y must be under 10 # setter

# 위에서 확인 했 듯 실수형 x,y를 받고 값을 읽거나 수정하되 객체지향의 특징인 추상화 , 캡슐화, 은닉화, 상속성의 개념을 적용하여
# 클래스를 작성을 완료 하였다. 




# __slot__ 메서드
# 파이썬 인터프리터에게 통보하는 메서드
# 런타임중 해당 클래스가 가지는 속성을 제한한다.

# 파이썬의 모든 클래스들의 속성은 위에서 보았 듯 딕셔너리(__dict__) 형태로 관리 되어진다. 
# 딕셔너리는 해쉬 테이블을 사용하므로 많은 메모리(램문제)를 잡아 먹는다.
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용량이 높아짐

# 클래스의 인스턴스 속성 관리에서는 딕셔너리 대신 
# __slot__ 메서드를 사용하여 set처럼 중복을 피한 값들을 튜플 자료형 관리 하면
#  메모리  사용량을 줄일 수 있다.

class Test1(object):
    # 튜플 자료형으로 관리하고 set처럼 중복을 피하자
    # 필요한 값이 있으면 그때 그때 __slots__에 넣으면 된다.
    __slots__ = ('a',)

class Test2(object):
    pass

use_slot = Test1()
no_slot  = Test2()

print(use_slot) # <__main__.Test1 object at 0x7fc2ed7a1c10>
print(type(use_slot.__slots__)) # ('a',) 로 값을 출력할 수 있다.
# print(use_slot.__dict__) # set 형태 이므로 dict이 사용되어 지지 못한다.
print(no_slot) # <__main__.Test2 object at 0x7fb970145c50>
print(no_slot.__dict__) # {}

# __slot__, dict 형태간의  클래스  메모리 사용량 비교
import timeit

# 측정을 위한 클로저 함수 
def outer_(obj):
    def inner_():
        obj.a = 'test'
        del obj.a
    return inner_

# repeat() : 함수를 내가 지정한 만큼 실행하고 실행을 반환하는 함수
# mint()   : 제일 적게걸린 시간

# use_slot 함수 실행시 백만번 돌릴때 최소 시간 0.09497848899991368
print('백만번 돌릴때 최소 시간', min(timeit.repeat(outer_(use_slot), number=1_000_000))) 

# no_slot 함수 실행시 백만번 돌릴때 최소 시간 0.12683089399979508
print('백만번 돌릴때 최소 시간', min(timeit.repeat(outer_(no_slot), number=1_000_000))) 




