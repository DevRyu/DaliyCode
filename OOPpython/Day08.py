#    Chapter 02. Data model - 07. Special Method(2) - 3

# init에 분기되는 x,y를 담는 속성과 과 repr로 출력하는 매직메서드를
# 오버라이딩 하는 함수를 선언 해 보겠습니다. 
# 추가로 파이썬의 object를 상속하는 함수를 만들어 보겠습니다.

class XY(object):
    
    def __init__(self, *args):
        '''init function, put XY(x,y) or empty XY()'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else :
            self._x, self._y =  args
    
    def __repr__(self):
        return 'Vactor(%r, %r)' % (self._x, self._y)


v1 = XY(10, 20)
v2 = XY(20, 40)
v3 = XY()

print(XY.__init__.__doc__) # init function, put XY(x,y) or empty XY()
print(v1, v2, v3) # Vactor(10, 20) Vactor(20, 40) Vactor(0, 0) 로 출력이 된다.

print(dir(v3)) 
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_x', '_y']

# directory()내에 없으므로 *연산자(__mul__) 사용하지 못한다.
# print(v1 * v2) # TypeError: unsupported operand type(s) for *: 'XY' and 'XY'
# def __mul__(self,x,y): 이런식으로 선언이 필요하다.

# 신기한건 __bool__ 내장메서드는  없는데 bool() 돌아간다.
# v3라는 객체가 존재하는지 아닌지를 판별하는 것 같다.
print(bool(v3)) # True
# print(v3.__bool__()) 당연히 매직 메서드로 접근하려고 하면  attribute '__bool__' 이 없다고 한다 
# 상당히 tricky한 거 같다.

# 실제 __bool__내장 매직 메서드를 가지는 객체를 만들고 __bool__과 __doc__을 확인해 보겠다.
a = True
print(a.__bool__()) #True
print(a.__bool__.__doc__) # self != 0