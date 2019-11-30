# 객체의 메소드
# 클래스 메소드 
# 인스턴스 메소드
# 스테틱 메소드



class Student(object):

    '''
    author  : Ryu
    Date    : 2019-11-30 
    '''

    tuition = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id         = id
        self._first_name = first_name
        self._last_name  = last_name
        self._email      = email
        self._grade      = grade
        self._tuition    = tuition
        self._gpa        = gpa

    # 인스턴스의 메소드
    # 인스턴스 생성후 사용하는 메서드, self가 있으면 인스턴스 메서드이다.
    def full_name(self):
        return '{},{}'.format(self._first_name, self._last_name)

    def detail_info(self):
        return 'detail info :{},{},{},{},{},{}'.format(self._id, self.full_name(), self._email ,self._grade ,self._tuition ,self._gpa )

    def get_fee(self):
        return 'Before Tuition -> id : {}, fee : {}'.format(self._id, self._tution)

    def get_fee_culc(self):
        #                                                                  인스턴스변수* 클래스변수
        return 'after tution -> id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition)

    # 매직 인스턴스 메서드
    # '__'를 던더라고 부른다.
    def __str__(self):
        return 'st info -> name : {} grade : {} email : {}'.format(self.full_name(), self._grade, self._email)

    # 클래스 메서드
    # 모든 인스턴스가 사용하는 클래스 변수를 접근해서 수정할때는
    # @classmethod를 사용해서 수정하는 로직을 작성해야 한다.
    # 첫번째 인자로 클래스를 받고 두번째 인자로 원하는 값을 받는다
    # cls가 self처럼 클래스가 넘어간다.
    # print(cls) = ><class '__main__.Student'>

    @classmethod
    def raise_fee(cls, per):
        if per <= 1: 
            print("1이상의 퍼센트를 알려주세요")
            return
        cls.tuition = per
        print({'MESSAGE':'SUCCESS'})

    # 클래스 메서드로 객체를 인스턴스화 시킬수도 있다.
    # 위의 __init__의 인자들을 똑같이 하고 리턴해준다.
    # 리턴할 때 클래스의 인스턴스
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        #  def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        #      self._tuition    = tuition * Student.tution으로 사용하지 못한다.
        #      클래스 메서드로 인스턴스 생성시                 클래스변수와 파라미터간의 계산이 가능하다
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition, gpa)

    # 인자가 인스턴스 밖에 필요 없고 어떠한 인스턴스도 사용할 수 있는게 스테틱 메서드
    @staticmethod
    def is_scholar(inst):
        if inst._gpa >= 4.3 :
            return '{} is yes'.format(inst._last_name)
        return 'no'

# 인스턴스 선언
st1 = Student(1, 'Ryu',  'Maru', 'a@a.com', '1', 0, 4.5)
st2 = Student(2, 'Kim',  'Maru', 'b@b.com', '4', 100, 3.5)
st3 = Student(3, 'Park', 'Maru', 'b@b.com', '6', 400, 3.8)

# 기본정보보기
print('--')
print(st1)

# 전체정보보기
print('----')
print(st1.detail_info())
print(st2.detail_info())
print(st3.detail_info())

# 클래스 메서드 사용시
Student.raise_fee(1)


# 학비퍼센트(클래스 변수) 올리기 [클레스 메소드 미사용시]
# 직접접근해서 수정한다(PEP8에서는 지양! 한다. 이유는 안쓰는게 실수가 덜나서 클래스메서드로 쓴다.) 
print('------')
Student.tuition = 1.2
print(st1.get_fee_culc())
print(st2.get_fee_culc())

# 클래스 메서드 인스턴스 생성하기 
# 장점은 클래스 메서드로 생성시 메서드의 네이밍만 보고 의미 전달이 더 편하다.
print('--------')
st4 = Student.student_const(4, 'cls', 'Maru', 'd@b.com', '7', 300, 3.7)

# st4를 프린트하면 __str__ 매직 인스턴스 메서드를 거쳐서 출력되어진다.
print('----------')
print(st4)
print(st4.detail_info())

# 학생 학비 변경 확인
print('------------')

print(st4._tuition)
print(Student.tuition)
일단 클래스와직접 선언 한다
# 장학금 판별 함수
# 사실 밖에서 써도 상관없는 추세이다
def is_scholarship(inst):
    if inst._gpa >= 4.3 :
        return '{} is yes'.format(inst._last_name)
    return 'no'
print('--------------')

print(is_scholarship(st1))
print(is_scholarship(st2))
print(is_scholarship(st3))
print(is_scholarship(st4))

# 위의 메서드도 괜찮지만 클래스 내에 있는게 좋다.
# 인자가 필요없고 어떠한 인스턴스도 사용할 수 있는게 스테틱 메서드

print('----------------')

print(Student.is_scholar(st1))
print(Student.is_scholar(st2))
print(Student.is_scholar(st3))
print(Student.is_scholar(st4))

# 인스턴스에서 접근해서 사용시
print('------------------')

print(st1.is_scholar(st1))
print(st2.is_scholar(st2))
print(st3.is_scholar(st3))
print(st4.is_scholar(st4))


# insight 
# 이러한 3가지 메서드를 잘 분류하는 것을 모듈화 모듈화가 모이면 패키지다
# 인스턴스 생성후 사용하는 메서드, self가 있으면 인스턴스 메서드이다.
# 클래스 메서드는 첫번째 인자로 클래스를 받고 두번째 인자로 원하는 값을 받는다 
# 클래스 메서드로 객체를 인스턴스화 시킬수도 있다.
# 스테틱 메서드는 인자가 인스턴스 밖에 필요 없고 어떠한 인스턴스도 사용할 수 있다
