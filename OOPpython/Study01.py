from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)



# str.format()메서드
# format(42, 'b') # 101010
# format(2/3, '.1%') # 66.7%

from datetime import datetime 
now = datetime.now()
format(now, '%H %M %S') # 예약어를 잘 인식한다.

v1 = Vector()
print(dir(v1))

# 객체를 숫자로 변환하는 메서드, 바이트로 변환하고 해시할수 있게 해주는 메서드 hash, p349
# hash메서드()
# xor구현 ^ dustkswk tkdyd

# 프로퍼티 구현  객체속성 보호 할 필요없음
# def __hash__():
#     return self.x ^ self.y

# 불변형(immutable)으로 만들려면
# __hash__(self): 를 사용하여 값이 해쉬셋이 mutable하지 않도록 하게 하고 변경되지 않게 해야한다. 

# ^를 사용함으로
# x y
# 0 1
# 1 0

# 기본적으로 파이썬은 속성을 __dict__라는 딕셔너리 형에 저장
# __slot__ 메서드 -> 수만,수십만 개이상의 아주 많은 객체만 다룰 때 유용하다.

# __slot__메서드를 사용할 경우 필요없는 내장 매직 메서드르르 사용하지 않기때문에
# 파이썬 인터프리터에게 통보하는 메서드
# 런타임중 해당 클래스가 가지는 속성을 제한한다.


class Test1(object):
    __slots__ = ('a','b',)

class B(object):
    b = ('a','b',)

a = Test1()
b = B()
print(dir(a))
print(dir(b))

# 단순히 __slot__에서  두가지만 빠졌는데 성능이 반이상 줄어든다.
print(set(sorted(dir(b))) - set(sorted(dir(a))))
# {'__weakref__', '__dict__'}


print(set(sorted(dir(a))) - set(sorted(dir(b))))
# {'__slots__', 'a'}

# 클래스 속성은 공개 되어 있고 서브클래스가 상속하므로
# 클래스 데이터 속성을 커스터마이즈 할때는 상속하는 것이 일반적인 상식이다.

# self.typecode 등의 객체 속성을 이용해서 클래스 속성을 오버라이드 가증하다