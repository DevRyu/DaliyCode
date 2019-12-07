# 객체(클래스) 인덱스 슬라이싱

# 파이썬에서 미리 만들어 놓은 메소드들을 활용 한다.
class Test3:
    # 속성 메서드
    def __init__(self):
        self._numbers = [n for n in range(1,1000,3)]
    
    # 길이 메서드
    def __len__(self):
        print('__len__ was called')
        return len(self._numbers)

    # 인덱스로 아이템을 가져오는 메서드
    def __getitem__(self, idx):
        print('__getitem__ was called')
        return self._numbers[idx]

a = Test3()

print(a)
print(a.__dict__)

# 위의 길이 메서드가 있어서 len(인스턴스)만 있어도  클래스 자체의 __len__을 실행한다.
# 이를 통해 len() == 던더 안의  __len__은 같은 기능을 하고 볼수 있다.

print(len(a)) # __len__ was called # 333

# 물론 아래와 같이 속성에 직접 접근하여서 __len__메서드를 사용하지않고 len을 적용 할 수도 있다.
print(len(a._numbers)) # 333

# __getitem__ 메서드의 선언으로 인스턴스 자체를 리스트 처럼 출력할 수도 있다.
print(a[1:10]) # [4, 7, 10, 13, 16, 19, 22, 25, 28]



# 추상클래스(Abstract Base Class) 사용시 https://docs.python.org/3/library/collections.abc.html에 들어가면 ABC의 특징별로 사용할 수 있다.

# 추상클래스의 역할은 개발과 관련된 공통된 내용(필드, 메서드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것입니다.
# 추상클래스는 자체적으로 객체 생성 불가합니다.
# 추상클래스는 상속을 통해서 자식 클래스에서의 인스턴스를 생성해야 합니다.
# 추상클래스는 네이밍을 통일화 시킵니다.
# 부모의 메서드 들을 오버라이딩의 개념으로 사용할 수 있습니다.

# 부모 ABC를 받는 자식 클래스에게 만약 강제성을 부여 해야 한다는 전제 하에(이런 일이 자주 있음) 클래스를 생성해 보겠습니다.





# Sequence(순차, 순열) 추상 클래스를 상속 받지 않았지만, 파이썬에서 자동으로 기능이 작동해주는 클래스

# https://docs.python.org/3/library/collections.abc.html에 들어가 Sequence를 보자

# 파이썬 공식  Docs에서는 이렇게 분류 하였다.
# ABC                : Sequence                                               # 추상클래스
# Inherits from      : Reversible, Collection                                 # 현재 추상클래스의 상위 클래스
# Abstract Methods   : __getitem__, __len__                                   # 사용시 기본적으로 정의 되어야 작동하는 매직메서드 
# Mixin Methods      : __contains__, __iter__, __reversed__, index, and count # 다중 상속된 추가적인(optianal) 메서드나 속성


# 아래의 클래스는 엄밀히 따지면 __iter__,__contain__이 존재해야 실행이 가능하다. 
# 하지만 파이썬에서 자동으로 지원해준다. => 시퀀스 프로토콜
class IterClass1():

    def __getitem__(self, idx):
        print('__getitem__')
        return range(1, 50, 2)[idx] 

a = IterClass1()

print(a[1]) #__getitem__ #11

# __iter__가 정의 되어 있지 않아도 리스트 슬라이싱 구현이 되는가?
print(a[1:10]) # __getitem__ range(3, 21, 2) /// # __iter__가 없어도 자동으로 [:] 의 기능이 된다.

# __iter__, __contain__ 이 정의 되어 있지 않아도 리스트 슬라이싱, 컨테인이 되는가?
print(5 in a[1:10]) # __getitem__ True /// 5가 a[1:10]안에  __contain__이 되어 있는지도 확인이된다.
print([i for i in a]) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]






# FM으로 추상 클래스를 구현해 보자
# Sequence(순차, 순열) 추상클래스를 상속을 받아 요구 사항들인 추상 메소드를을 모두 구현해야 동작하는 클래스

from collections.abc import Sequence

class IterClass2(Sequence):
    def __getitem__(self, idx):
        print('__getitem__ was called')
        return range(1, 50, 2)[idx]  

# 위 처럼 def __getitem__(self, idx): 하나만 선언하면 에레 메세지를 반환한다
# b = IterClass2() # TypeError: Can't instantiate abstract class IterClass2 with abstract methods __len__ 

# 위의 결과로 Abstract Methods   : __getitem__, __len__를 필수로 클래스 내에 선언 후 인스턴스화를 진행 해야 함을 알 수 있다.
# def __len__(self, idx): 을 다시 선언 해 보자
class IterClass2(Sequence):
    def __getitem__(self, idx):
        print('__getitem__ was called')
        return range(1, 50, 2)[idx]  

    def __len__(self, idx):
        print('__len__ was called')
        return len(range(1, 50, 2)[idx])

b = IterClass2() 

# 출력이 잘 되어진다.
print(b[4]) # 9
print(b[1:10]) # range(3, 21, 2)
print(5 in b[1:10]) # True



# abc를 더 활용해보자
# 추상 메타 클래스를 상속 받는 난수_번호_생성_엔진 부모 클래스와 
# 부모 클래스를 상속 받는 번호_뽑기_기계 자식 클래스를 생성해 보자

import abc

# 추상메타클래스 전체를 상속 받아보자
class RandomNum(abc.ABC):

    # 추상 메소드 사용시 데코레이터를 쓰자
    @abc.abstractmethod
    def load(self, iterobject):
        print('RandomNum load')
        '''반복 가능한 항목 메서드(비어 있음)'''

    @abc.abstractmethod
    def pick(self,iterobject):
        print('RandomNum pick')
        '''뽑는 메서드(비어있음)'''
        
    # 뽑은 아이템을 추가하는 메서드
    def inspect(self):
        print('RandomNum inspect')
        items = [] 
        
        while True:

            try:
                items.append(self.pick())
            # 더이상 값이 없을때 멈추기
            except LookupError:
                break

            return tuple(sorted(items))


# 위의 RandomNum 클래스를 상속 해보자
import random

class PickingMachine(RandomNum):
    
    def __init__(self, items):
        # 시스템에서 랜덤 변수 생성
        print('PickingMachine __init__')
        self._randomizer = random.SystemRandom()
        self._items      = []
        self.load(items)
    
    # @abc.abstractmethod로 상위메서드에서 선언 되어 있고 자식 클래스는 다시 재선언와 구현을 해야한다.
    # 1.재선언와 2.구현을 해야하는 이유는 위에 함수에 '''''' 밖에 들어있지 않아서 기능이 실제로 없이 선언만 되어 있기 때문이다. 
    # 선언을 해주지 않는다면 TypeError: Can't instantiate abstract class PickingMachine with abstract methods pick 와 같은 에러가 호출된다.

    def load(self, items):
        print('PickingMachine load')
        self._items.extend(items) # item을 넣을때마다 item의 리스트를 확장하는 메서드
        # _randomizer == def __init__ 안의 random.SystemRandom() 클로저이다.
        self._randomizer.shuffle(self._items) # 섞는 메서드 사용
    
    def pick(self):
        try:
            print('PickingMachine pick')
            return self._items.pop()

        # 빈 print(a.__call__)스트일 경우 에러 호출
        except IndexError:
            raise LookupError('Empty List')

    def __call__(self): # 클래스 인스턴스만 함수처럼 그냥 실행할 할수 있는 메서드
        print('PickingMachine __call__')
        return self.pick() 

# 서브 클래스(부모자식)인지 확인하기
# issubclass(자식, 부모)로 boolean으로 return
print(issubclass(PickingMachine, RandomNum))  # True

# 상속 구조 확인 
# 클래스.__mro__ 로 볼수 있다.
# 오른쪽으로 갈수록 상위 부모이다
print(PickingMachine.__mro__) # (<class '__main__.PickingMachine'>, <class '__main__.RandomNum'>, <class 'abc.ABC'>, <class 'object'>)

c = PickingMachine(range(1,50)) 

print(c._items) 
# print(c._items) 실행과정

# PickingMachine __init__ 함수에 먼저 접근하여
# _items = [] 생성후
# load(_items) 메서드로 넘기고

# PickingMachine load 함수에 가서
# extend(items)로 _items의 []의 사이즈를 확장 및 range(1,50)을 넣은 다음
# self._randomizer.shuffle(self._items) _randomizer[클로저].shuffle(self._items[리스트])[메서드]  셔플된 값을 _items 로 return, 리스트에 다시 담는다.

# 그리고 출력print()한다. [45, 11, 43, 1, 46, 8, 49, 33, 28, 19, 10, 3, 32, 26, 40, 17, 30 ...

# 뽑는 함수 출력
print(c.pick()) # PickingMachine pick .pop()함수 출력됨// 22 

# callable하게 인스턴스 자체를 print 할수 있게 하는가? 
print(c()) # PickingMachine __call__함수 실행 후 # PickingMachine pick  // 2

#부모의 RandomNum inspect가 실행이 되는가?
print(c.inspect())  # # (13,)

# 실행 순서
# RandomNum inspect 가 실행되고
# c는 리스트의 값이 있으므로
# try: items.append(self.pick())이 실행되는데 

# PickingMachine pick, 바로 자식 클래스에서 명시한 메서드가 실행되고 (부모의 pick이 아니다! 왜냐하면 지금 자식의 클래스 인스턴스에서 출력을 건거다!)
# 다시 RandomNum inspect로 돌아와  return tuple(sorted(items)) 튜플 형식으로 출력하여 준다.
# (13,)