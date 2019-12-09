# 파이썬에서 파라미터의 기본값은 클래스의 인스턴스화에 어떤 영향을 끼치는가(파라미터와 인자의 구분은 왜 두는 것인가)?

# 이 글은 파라미터, 인자의 구분까지 아신다고 가정하에 작성되었습니다.
# 그냥 구분을 하는것 보다 왜 왜 구분지어 부르는지에 대해 궁금한지 파헤치는 글입니다.
# 파라미터 기본값(Parameter Default Value)
# 키워드 인자(Keyword Arguments) (여기서 인자로 값을 넣어주는것)

# 파라미터에 기본값(mutable)을 지정한 클래스의 인스턴스화는 얕은 복사가 일어난다!  

# 함수에서의 파라미터의 기본값을 사용하는 것은 함수 안의 로컬 영역의 변수(객체) 할당의 행위이다!

# (단 함수 호출시 인자로 새로운 값을 넣어줘서 디폴트 값을 사용하지 않으면 상관 없습니다. 이렇게 되면 디폴트 값 선언된 것은 사용되어 지지 않습니다!)

# 함수 내에 파라미터, 인자들도 결국 하나의 값 할당 전의 변수이거나 값을 할당한 변수이다.

# 파라미터의 기본값을 사용하는 클래스의 인스턴스화는 얕은 복사가 일어난다!

# 하지만 파라미터와 상관없이 인자를 주면 클래스의 인스턴스화는 깊은 복사가 일어난다!

# 선행 지식
# - 단순 객채복사, 얕은복사, 깊은복사간 차이
# 단순 객채복사 : 객체id,변수,값 다 같은 것을 복사, 단 mutable(변경가능)한 객체에만 해당, 
#              : immutable(불변)한 것은 새로운 객id를 부여함으로 예외이다.. 크게 숫자와 문자열, 튜플입니다.
# 얕은 복사     : 복합변경 가능한 객체(리스트,셋,딕셔너리)id는 다름 하지만 안의 변수,값 내용은 원래 복사하기 전의 객체와 같다.(공유)
# 깊은 복사     : id,변수,값 셋다 독립적으로 변합니다.



# 저의 예상을 빗나가고 많은 깨우침을 준 함수를 설명해 볼려고합니다.
# 함수에서의 파라미터의 기본값이 설정되어 있으면 우리는 이것을 단순히 독립된 하나의 값으로 봐야 하나요 하나의 할당된 변수로 봐야 할가요?
# 클래스의 인스턴스화는 항상 깊은 복사만 일어날가요?

# 위의 설명이 어려우시다고요? 
# 일단 한번 예제를 통해 다루어 보겠습니다.

# 홍콩 택시를 타봅시다. 

# HongKongTaxi회사 클래스입니다.
class HongKongTaxi:

    # 기본값으로 탑승인원
    def __init__(self, customers=[]):
        self.customers = customers 
    # 출발 중간 합승으로 태우는 사람 함수
    def pick(self, name):
        self.customers.append(name) 
    # 중간에 내리는 사람 함수
    def drop(self, name):
        self.customers.remove(name)

taxi1 = HongKongTaxi(['Alpha', 'Beta']) # taxi1에 기본값으로 알파 베타가 탑승합니다.
taxi1.pick( 'Charlie') # 찰리도 타네요
taxi1.drop('Alpha')    # 알파가 내립니다.

print(taxi1.customers) # ['Beta', 'Charlie'] # 현재 승객입니다.

taxi2 = HongKongTaxi() # taxi2에 기본값으로 아무도 타지 않았습니다.
taxi2.pick('Charlie')  # 찰리가 중간에 탑니다.

print(taxi2.customers) # ['Charlie'] # 현재 승객입니다.

taxi3 = HongKongTaxi() # taxi3에 기본값으로 아무도 타지 않았습니다.
taxi3.pick('Delta')    # 찰리가 중간에 탑니다.

print(taxi3.customers) # ['Charlie', 'Delta'] # 엥? 찰리는 taxt2에 있엇는데 taxi3에도 있네요...? 

taxi4 = HongKongTaxi() # taxi4에 기본값으로 아무도 타지 않았습니다.

print(taxi4.customers) # ['Charlie', 'Delta'] # taxi4는 비어 있엇는데 흠.... 둘다 탓네요...

# 사실 HongKongTaxi는 잘못이 없습니다. 
# Taxi를 설계한 나의 잘못입니다. 
# 그는 좋은 택시 였습니다...
# 이렇게 우리를 tricky 하게 만드는 것을 한번 코드 내부적으로 까봅시다.
# 위의 설명을 택시번호(id) 증명해보겠습니다.


# HongKongTaxi3회사 클래스입니다. (HongKongTaxi회사와 다릅니다!)
class HongKongTaxi3:

    def __init__(self, customers=[]):
        print('출발지에서 탄 택시의 아이디 =>', id(customers)) # customers변수의 id를 공유하는지 볼게요
        self.customers = customers 

    def pick(self, name):
        self.customers.append(name) 

    def drop(self, name):
        self.customers.remove(name)

taxi1 = HongKongTaxi3(['Alpha', 'Beta']) # 출발지에서 탄 택시의 아이디 => 139936628240784
print('인스턴스의 id',id(taxi1))          # 인스턴스의 id 139681696451344
taxi1.pick('Charlie')
taxi1.drop('Alpha')

print(taxi1.customers)                   # ['Beta', 'Charlie']

taxi2 = HongKongTaxi3()                  # 출발지에서 탄 택시의 아이디 => 139936628240944
print('인스턴스의 id',id(taxi2))          # 인스턴스의 id 139681696450896
taxi2.pick('Charlie')
print(id(taxi2.customers[0]))            # taxi2의 찰리 아이디: 140114413072880
print(taxi2.customers)                   # ['Charlie']

taxi3 = HongKongTaxi3()                  # 출발지에서 탄 택시의 아이디 => 139936628240944
print('인스턴스의 id',id(taxi3))          # 인스턴스의 id 139681696451024
taxi3.pick('Delta')

print(id(taxi3.customers[0]))            # taxi3의 찰리 아이디: 140114413072880


print(taxi3.customers)                   # ['Charlie', 'Delta']

taxi4 = HongKongTaxi3(customers=['zeta'])# 출발지에서 탄 택시의 아이디 => 139936629582896
print('인스턴스의 id',id(taxi4))          # 인스턴스의 id 139681696451088
print(taxi4.customers)                   # ['zeta']

# 이런...HongKongTaxi3회사의 taxi3번이 사실 taxt2와 같은 id, 같은 차였군요....
# 다음에 타실 손님께 죄송하니까 taxi4 는 기본 값을 주었습니다.

# 위의 설명과 지금의 예시에 대해 종합적으로 다시 정리해 보겠습니다

# taxi2 = HongKongTaxi3(), taxi3 = HongKongTaxi3()객체를 인스턴스할 때 얕은 복사가 일어나서 그렇습니다!
# 여기가 얕은 복사가 증명되는 순간입니다.
# taxi2의 인스턴스의 id 139681696450896와 taxi3의 인스턴스의 id 139681696451024 다르지만 내부의 값은 같습니다
# print(id(taxi3.customers[0]))            # taxi3의 찰리 아이디: 140114413072880
# taxi2의 찰리 아이디, taxi3의 찰리 아이디 같은거 보이시죠?
# 이렇듯 파라미터에 기본값(mutable)을 사용한 클래스의 인스턴스는 얕은 복사가 일어납니다.  
# 여기 class HongKongTaxi3:내의 함수 __init__(customers=[])의 디폴트 값을 잘 확인 하셔야합니다.

# 당연히 우리는 그냥 taxi2 = HongKongTaxi3(), taxi3 = HongKongTaxi3()객체를 인스턴스화 시킨거지만
# 실제로는 HongKongTaxi3(customers=[])을 쓰는데 customers변수가 mutable하니까 얕은 복사가 일어나는 겁니다!

# 다시말해 파라미터의 기본값을 사용하실 때 이것은 함수내의 로컬 변수로 저장이 되고
# 이후 새롭개 클래스 인스턴스로 생성을 해도 위에서 사용한 함수내의 로컬 변수를 그대로 이용하게 됩니다.



# 그렇다면 기본값을 가지는 파라미터와 인자를 받는 파라미터를 혼용해서 하면 어떨까요?
# 단 기본값을 가지는 파라미터는 항상 뒤로 오고 기본값이 없는 인자는 앞에 와야 합니다.
# 인자의 순서도 같습니다.
class HongKongTaxi4:

    def __init__(self, driver, customers=[]):
        print('출발지에서 탄 택시의 아이디 =>', id(customers)) # customers변수의 id를 공유하는지 볼게요
        self.customers = customers 
        self.driver    = driver

    def pick(self, name):
        self.customers.append(name) 

    def drop(self, name):
        self.customers.remove(name)

taxi1 = HongKongTaxi4('Kim',['Alpha', 'Beta']) # 출발지에서 탄 택시의 아이디 => 140111659877472
print('인스턴스의 id',id(taxi1))                # 인스턴스의 id 140111659888784
taxi1.pick('Charlie')
taxi1.drop('Alpha')

print(taxi1.customers)                         # ['Beta', 'Charlie']

taxi2 = HongKongTaxi4('Park')                  # 출발지에서 탄 택시의 아이디 => 140111659877632
print('인스턴스의 id',id(taxi2))                # 인스턴스의 id 140111659888848
taxi2.pick('Charlie')
print(id(taxi2.customers[0]))                  # taxi2의 찰리 아이디: 140111659996016
print(taxi2.customers)                         # ['Charlie']

taxi3 = HongKongTaxi4(driver ='Choi')          # 출발지에서 탄 택시의 아이디 => 140111659877632
print('인스턴스의 id',id(taxi3))                # 인스턴스의 id 140111659998736
taxi3.pick('Delta')

print(id(taxi3.customers[0]))                  # taxi3의 찰리 아이디: 140111659996016

print(taxi3.customers)                         # ['Charlie', 'Delta']

taxi4 = HongKongTaxi4( 'Ryu' , customers=['zeta'])  # 출발지에서 탄 택시의 아이디 => 140111659877712
print('인스턴스의 id',id(taxi4))                # 인스턴스의 id 140111659998864
print(taxi4.customers)                         # ['zeta']


# 예상하셧나요? 
# taxi2, taxi3 둘다 def __init__(self, driver, customers=[]): 에서 같은 id(customers=[] 140111659877632)를 공유 하고 있군요.
# 결국 여러 인자가 있어도 기본값을 사용하는 파라미터가 있다면! HongKongTaxi3과 같이 얕은 복사가 일어 나는 것을 증명했습니다.

# 사실 이렇게 파라미터에 기본값을 안 줘도 홍콩 택시는 어리숙하지 않게 잘 돌아갑니다.
# 단지 이러한 issue들을 저는 만나지 못하고 항상 아래의 패턴으로 사용 했엇거든요
# 그냥 인자에 []를 넣으면 되거든요! (사실 저는 이렇게 했거든요요요)
# 인자에 값을 넣으면 파라미터에 상관없이 깊은 복사가 일어나거든요요요요!

# HongKongTaxi2 회사입니다
class HongKongTaxi2:

    def __init__(self, customers):
        self.customers = customers

    def pick(self, name):
        self.customers.append(name)

    def drop(self, name):
        self.customers.remove(name)

taxi1 = HongKongTaxi2(['Alpha', 'Beta'])
print('인스턴스의 id',id(taxi1))
taxi1.pick('Charlie')
taxi1.drop('Alpha')
print(taxi1.customers) # ['Beta', 'Charlie']

taxi2 = HongKongTaxi2([])
print('인스턴스의 id',id(taxi2)) # 인스턴스의 id 139779190389520
taxi2.pick('Carrie')
print(taxi2.customers) # ['Carrie']

taxi3 = HongKongTaxi2([])
print('인스턴스의 id',id(taxi3)) # 인스턴스의 id 139779190389072
taxi3.pick('Delta')
print(taxi3.customers) # ['Delta']