# 매직메소드 
# 데이터의 모든 자료형은 클래스이다!

print(int) #<class 'int'>
print(str) #<class 'str'>

# 더 이상 안쳐도 되겠지만  항상 class를 출력합니다.  
# 그래서 위의 말을 증명 할 수 있습니다.

# 모든 속성 및 메소드는 dir() 함수로 확인이 가능합니다. 
# dictionary라고 이 참에 같이 외웁시다 


class Wework:
    
    def __init__(self, name, year):
    
        self._name = name
        self._year = year
    
    def __str__(self):
        return 'student info: {}, {}'.format(self._name, self._year)
    
    # 기존 대상, 비교대상을 정의하고 grater equal 과 Less equal 매직 메서드를 사용해 보자
    def __ge__(self, x):
    
        print('>=')
    
        if self._year >= x._year :
            return True
        else :
            return False
    
    def __le__(self, x):
    
        print('<=')
    
        if self._year <= x._year :
            return True
        else :
            return False
    
    def __sub__(self, x):
        
        print('__sub__')

        return self._year - x._year
    
# 회사 인스턴스를 만들어 주자

co1 = Wework('Wecode', 2019)
co2 = Wework('Aeine', 2018)

# 클래스끼리 더하기와 같은 연산이 가능할가?
# print(co1 + co2) # TypeError: unsupported operand type(s) for +: 'Wework' and 'Wework'

# 당연히 에러가 난다. 하지만 비교 연산자 매직 메서드는 어떨가?

# 아래에 '>='는 __ge__를 의미한다
# 클래스 내에 __ge__ 함수의 파라미터 왼쪽 self는 왼쪽 co1이 들어가고 
# 오른쪽 x는 오른쪽 co2로 들어간다

print(co1 >= co2) # true

# 위의 __sub__ 매직 메서드로 각 회사들의 창업 년도를 빼본다면?
# 잘된다. 

print(co1 - co2) # 1

# 더 자세한 내용은 https://docs.python.org/2.0/ref/specialnames.html 공식 문서에 있다.