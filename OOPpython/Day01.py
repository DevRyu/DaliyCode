# 절차지향 VS 객체지향
# 절차 지향 => 함수적 프로그래밍
# 객체 지향 => 코드의 재사용, 코드 중복 방지
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 절차 지향적인 코딩 스타일
# 위에서 아래로 읽는다
student_1 =  "kim"
student_11 =  1
student_111 = [ {'hi':'how' }]

student_2 =  "kim"
student_22 =  1
student_222 = [ {'hi':'how' }]

student_3 =  "kim"
student_33 =  1
student_333 = [ {'hi':'how' }]


# 리스트 구조
# 관리하기 불편하고 위치 인덱스를 맵핑해서 사용해야함 
student_list = ['kim', 'lee', 'park']
student_grade_list = [1, 2, 3]
student_details_list = [
    {'gender': 'a', 'score' : 100, 'score2' : 100 }
]

# 리스트 인덱스 삭제시

del student_list[0]
del student_grade_list[1]

# 딕셔너리 구조로 바꾸기

students_dicts = [ 
    {'name' : 'kim' , 'gender': 'male' , 'student_detail' : {
        'math': '100', 'english' : '89'}
    },
    {'name' : 'ja' , 'gender': 'male' , 'student_detail' : {
        'math': '100', 'english' : '89'}
    }
]

del students_dicts[1]
# print(students_dicts)


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Student():

    # 속성(생성자)
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    # 행위(메서드)
    def __str__(self):
        return 'str : {} : {}'.format(self._name, self._number)
    
    # str이 없으면 호출해준다
    # str과 repr의 차이는 
    # str은 print문에 의한 출력과 동알한 문자열
    # str은 객체의 비공식적인 문자열출력 (사용자가 보기쉬운형태{보기쉽게 생략이될수도 있다.}) 
    # 예) s = Hello, World!
#   s = "Hello, World!"
# print(str(s))  # Hello, World!
# print(repr(s))  # 'Hello, World!'

    # print(s) 시 에러 str  은 문자열


    # repr은 객체의 공식적인 문자열 출력이다  (파이썬의 인터프린터가 해당 객체가 되어 인스턴스를  만들 수 있는 문자열)
    # 예) 소수점이 얼마나 찍히든 다 출력해준다.
    def __repr__(self): 
        return 'repr : {} : {}'.format(self._name, self._number)



student1 = Student('a',1,1, {'details':'male'})
student2 = Student('b',2,2, {'details':'male'})
student3 = Student('c',3,3, {'details':'female'})

print(student1)
print(student2.__dict__) # 파이썬의 모든 객체는 딕셔너리 형태로 가짐 그래서 딕셔너리 메서드를 쓰면 키 벨류 형태로 리턴함 

#위의 객체의 인스턴스들을 리스트에 담아서 호출 가능

stu_list = []

stu_list.append(student1)
stu_list.append(student2)
stu_list.append(student3)

#객체만 알려준다. 
print(stu_list)

#__str__오버라이드라는 함수인데 for 문의 in 연산자를 쓰면 보여진다.
for i in stu_list:
    # 또는 강제적으로 repr()써도됨
    print(repr(i))
    print(i)

# insight 

s  = 'Hello world'
print(s)
k = str(s)
j = repr(s)
print(type(k))
print(k)
kk = k
print(kk)
print(type(j))
print(j)
jj = j
print(jj)