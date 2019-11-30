# 클래스 상세
# 인스턴스
# 클래스 변수
# 인스턴스 변수
# 클래스 설계 하기



class Student():
    """
    author : ryu
    date : 2019-11-30
    """

    # 클래스 변수(공용 scope)
    student_count = 0 

    # 인스턴스의 변수(인스턴스 선언시의  scope)      이메일을 디폴트값으로 선언 한 것이다. 
    def __init__(self, name, number, grade, detail, email=None, student_count = 10):
        self._name      =  name
        self._number    =  number
        self._grade     =  grade
        self._detail    =  detail
        self._email     =  email
        self._student_count = student_count
        #클래스 인스턴스 생성될때마다 하나씩 추가한다. 
        Student.student_count += 1

    def __str__(self):
        return 'str{}'.format(self._name)
    
    def __repr__(self):
        return 'repr{}'.format(self._name)
    
    def whatiself1():
        print('whatiself1')
    
    def whatiself2(self):

        #밑의 셀프를 설명하기 위해 프린트 해보겠다
        print(id(self), 'print(id(self))')
        
    #학생의 자세한 정보를 출력하는 함수 
    def detail_info(self):
        print('Current id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self_details))
    
    # 계정이 삭제될 때의 인스턴스 총합 빼기
    def __del__(self):
        Student.student_count -= 1

# Self의 의미   
s = Student('ryu', '010', '5', 'he is male', 'a@a.com')
s1 = Student('ryu', '010', '5', 'he is male', 'a@a.com')
s2 = Student('pakr', '010', '5', 'he is male', 'a@a.com')

# 클래스내에 정의된 함수를 메서드라고 하는데 첫번재 인자가 항상 self여야 한다는것은 틀린 말이다
# 위에 클래스 선언후 인터프리터 실행 시 클래스에는 문제가 없고 
# 밑의 출력도 잘되기 때문이다. 즉 빈 매개변수 의 개념
print('--------------------------')
print(s1.whatiself1)

# 대신에 빈[self가 들어갈] 매개변수를 가지는 () 문자를 메서드 뒤에 붙이면
# 파이썬 메서드의 첫 번째 인자로 항상 인스턴스[==self]가 전달되야 해서 발생하는 문제가 있다.
# print(s1.whatiself1())

# '인스턴스.메서드()’,‘클래스.메서드(인스턴스)’가 호출되는 방식은 아무차이가 없다.
# 그래도 가독성을 위해 보통은 '인스턴스.메서드()’를 취하고
# 클래스의 함수를 그대로 사용하고 싶으면 클래스.메서드(인스턴스)를 취한다.
print('----------------------------')
print(s1.whatiself2())
print(Student.whatiself2(s1))

# 아래의 두가지의 값은 같다.
print('--------------------------------')
s1.whatiself2()
print(id(s1))



# 객체의 인스턴스화는 같지가 않다.
# is는 인스턴스의 아이디 값을 비교한다.
print('----------------------------------')
print(s1 is s2)

# 하지만 값을 비교하는 비교 연산자(==)  사용하는 경우 같아진다
print('------------------------------------')
print(s1._name is s2._name)
print(s1._number == s2._number)

# 하지만 객체의 인스턴스 간의 비교는 비교 연산자도  아이디 값만 비교하여 False를 출력한다
print('--------------------------------------')
print(s1 == s2)
 
# dir & __dict__ 확인
# dir은 사용가능한 내장함수를 확인할수 있다. 대신 키(변수)만 볼 수 있고 값은 볼 수 없다
# __dict__ 으로 print로 보면 딕셔녀리 형태로 속성 키, 값 둘다 볼수 있다. 읽기 전용 딕셔너리인 mappingproxy 라는 타입으로 반환이 된다 
# mappingproxy 라는 타입으로 값을 수정 [즉 R을 제외한 CUD] 할 수 없다
# 인터프리터에서 더 간단하게 .을찍고 탭을 두번 누르면 다음 입력할수 있는 키(변수)를 보여준다.
print('----------------------------------------')
print(dir(s))
print(s.__dict__)

# __doc__ 주석을 출력하는 함수 이다.
# 클래스에 직접 접근하는 함수로 적혀져 있는 주석을 참조 한다. 
print('------------------------------------------')
print(Student.__doc__)


print('--------------------------------------------')
print(Student.student_count)

# 해당 인스턴스에서 속성을 불러도 된다. 
print('----------------------------------------------')
print(s.student_count)
print(s.detail_info)
print(s.__del__)

# 객체의 인스턴스를 삭제 한 다음 
del(s)

print('------------------------------------------------')
# 출력하면 당연히 0이 된다.
print(Student.student_count)
print('--------------------------------------------------')

# __class__ 인스턴스의 클래스를 알고 싶을때(부모) 사용한다.
print('----------------------------------------------------')
print(s1.__class__)

# 부모끼리 같은지도 비교가 된다.
print('------------------------------------------------------')

print(s1.__class__ == s2.__class__)

# 인스턴스 변수(클래스의 인스턴스 속성)
# 가능은 하지만 직접 접근해서 CUD를 하는 행위는 PEP에서는 지양한다
print('--------------------------------------------------------')
s1._name = "no direct access to change"
print(s1._name)

# 클래스 변수(클래스 속성)
# 누구나 접근이 가능하다(공유성)
print('----------------------------------------------------------')
print(s1.student_count)
print(s2.student_count)
print(Student.student_count)

# student_count(클래스 변수) 공유되는지 확인하기
# 클래스에서는 보이지만
print('------------------------------------------------------------')
print(Student.__dict__)

# 인스턴스에서 딕셔너리 메서드 사용시  클래스 변수가 나타나지 않는다
# 이유는 인스턴스 네임스페이스에 없으면 파이썬이 자동으로 상위에서 알아서 검색한다.
# 즉 인스턴스 -> 부모클래스 순으로 검색함으로 실제 __dict__에서는 나오지 않지만 값을 내포한다.
# 위의 역은 성립하지 않는다.
print('----------------------------------------------------------')
print(s1.__dict__)

# 그러므로 클래스 변수나 인스턴스 변수나 동일한 이름으로 변수 생성 가능 
print('--------------------------------------------------------')
print(s2.__dict__)

# s2를 삭제하고 s1인 인스턴수 student_count와 클래스변수인 Student의 student_count 어디에 영향이 가는지 확인 
#     당연히 클래스 변수를 빼주는 함수를 쓴것 이므로 
#     클래스 변수만 값이 줄어 드는 것을 확인 가능
    # def __del__(self):
    #     Student.student_count -= 1
print('------------------------------------------------------')
print(Student.__dict__)
print('-----------------------------인스턴스 1개 삭제----------------------')
del(s2)
print(Student.__dict__)
print(s1.__dict__)

*네임스페이스란?
프로그래밍 언어의 객체를 이름에 따라 구분할 수 있는 범위(scope)
딕셔너리 형태
전역 네임스페이스: 모듈별로 존재하며, 모듈 전체에서 통용될 수 있는 이름들이 소속된다.
지역 네임스페이스: 함수 및 메서드 별로 존재하며, 함수 내의 지역 변수들의 이름들이 소속된다.
빌트인 네임스페이스: 기본 내장 함수 및 기본 예외들의 이름들이 소속된다. 파이썬으로 작성된 모든 코드 범위가 포함된다.

insight 
클래스 변수와 인스턴스 변수의 차이 및 활용 방법 
인스턴스 네임스페이스(__dict__)에 클래스 변수가 없어도 부모 클래스로 찾아 간다 (상속)
self의 참의미와 활용법
