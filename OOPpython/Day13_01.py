
# 예전에는 프로그래밍 언어의 분파가 지금보다 더 많았 엇고 이를 구분짓고 정의를 하는 일이 많았 엇던 것 같다.
# 그중에 ALGOL언어가 지대한 영향을 끼친 것 같다.(Robin Popplestone) 
# 함수형 프로그래밍의 언어의 특징들을 서술한 것이지 어떤 코드에 대핸 내용이 아니다.
# 프로그래밍 언어론 인줄... 
# 귀도 반 로섬의 파이썬 언어 철학에 취한다~

# 귀도 say
# One of my goals for Python was to make it so that all objects were "first class." 
# By this, I meant that I wanted all objects that could be named in the language (e.g., integers, strings, functions, classes, modules, methods, etc.) to have equal status. 
# That is, they can be assigned to variables, placed in lists, stored in dictionaries, passed as arguments, and so forth.


# 함수형 프로그래밍에서 (js든 go든 python이든) 가장 중요한 함수에 대해 용어에 대해 민감해 지기로 했다.
# 80~90%는 내용의 쓰임새에 대해 이해 했으나 정확히 무었을 말하고 싶어하는 지 알고 싶었다.
# 엄밀히 각각의 세부적인 구분이 안되서 하나하나 코딩하면서 구별 지을려고 한다.
# 또한 정리한 내용은 다른 웹에서도 의견이 분분한 경우가 많아 정의의 경우 대부분 위키에서 참조하여 좀 더 쉽게 재해석 하였다. 
# 위의 구분은 코딩은 ADD의 기본적인 두개의 인자를 더하는 함수를 작성하여서 구분 하도록 하겠다.

# 정의 
# First Class Object     : A라는 객체에 일반적으로 사용되는 연산을 모두 사용가능 한 B객체 (B객체는 일급 객체)를 지키는 언어의 특징 = 객체지향 언어의 개념 중 하나

# 파이썬에서는 Object 클래스에서 상속받는 객체이다.
# 파이썬에서의 객체들은 이를 지킨다. 
# 파이썬의 모든 것은 객체이다. == 순수 객체지향언어의 특징 중 하나인 "모든 것은 사전에 또는 사용자가 객체로 지정될수 있다는 것"을 지킨다. 
# https://medium.com/@durgaswaroop/functions-as-first-class-citizens-in-python-2e70cdc6e357

# 특징
# 1. * 런타임에 생성할 수 있다                    == (적용에 논란)파이썬과 자바스크립트는 해당사항 일부의 의견(C에서는 이 조건을 들이대면 이급 객체로 불려짐)
# 2. 데이터 구조체의 변수나 요소에 할당할 수 있다. == 모든 요소는 할당 명령문의 대상이 될 수 있다.
# 3. 함수 인수로 전달할 수 있다.                  == 모든 요소는 함수의 실제 매개변수가 될 수 있다.
# 4. 함수 결과로 리턴할 수 있다.                  == 모든 요소는 함수의 반환 값이 될 수 있다.
# 5. 모든 요소는 동일 비교의 대상이 될 수 있다.    == 파이썬에서 일급 객체 dir로 호출시 내장 매직 매서드로 eq,ge,gt,le,lt를 가지고 았음


# 정의
# First Class Citizen : "다른 엔티티(테이블)의 연산을 가능하게 하는 엔티티들"이라는 의미 = 객체지향 언어의 특징 = 객체지향 언어의 개념 중 하나
#                       First Class Object와 First Class Citizen을 위키에서는 동일하게 보지만
#                       몇몇의 글들은 현재의 언어(파이썬)는 First Class Object가 First Class Citizen의 특징을 모두 지킨다고 말한다.
#                       이를 구분 지어야 햇던 옛날 언어 때문에 이걸 정확히 알고 싶어하는 후대 사람들이 고생하는거 아닐까?

# 특징
# 1. 변수에 값을 할당 할 수 있다.
# 2. 인자로 값을 전달을 할 수 있다.
# 3. 반환값으로 값을 전달 할 수 있다.

# 정의
# First Class-Function   : 자바스크립트에서는 일급함수(파이썬의 일급 객체와 같다.)라고 불리우지만 파이썬에서는 'First Class Object의 함수'라는 의미로 사용된다. = 객체지향 언어의 개념 중 하나

# 특징
# 1. 데이터 구조체의 변수나 요소에 할당할 수 있다.
# 2. 하나 이상의 함수를 인수(인자)로 가진다.
# 3. 함수의 결과를 반환한다.
# 4. 하나 이상의 함수를 인수(인자)로 가지고 함수의 결과를 반환한다.
# 5. 클로저를 지원하며 Non-local 변수가 지정될 수 있는곳(파이썬에서는 free variables)이 있는 프로그래밍 언어
# 6. 일반함수와 기능이 평등해야 한다.(확장, 내장, 참조) 


# 정의
# Higer Order Function   : 외부 상태 변경이나 가변(mutable)적인 함수 객체를 피하고 함수 객체 자체의 불변성(Immutability)을 지향하는 함수형 프로그래밍
                        #  아래의 조건중 하나 이상 지키면 고차함수라고 한다.

# 특징
# 1. 하나 이상의 함수를 인수(인자)로 가진다.
# 2. 함수의 결과를 반환한다.
# 3. 하나 이상의 함수를 인수(인자)로 가지고 함수의 결과를 반환한다.
# 4. 람다 함수,중첩 함수,클로저 등 함수를 인자로 취하는 함수를 리턴하는 중첩함수(nested)일 경우이다.
#   -> 람다함수(익명함수)와 중첩함수, 클로저라고 해서 항상 고차함수라고 할 수 없다. ex) lambda (x) (x+1)에서 인자를 숫자로 받으면 고차함수가 아니다. 리턴 또한 숫자이다.
#   -> 하지만 쉽게 이해한다면 클로저,중첩함수,람다를 고차함수라고 생각 할 수 있다. 
#   -> 핵심은 고차함수로서의 행위가 발생 해야지 고차함수라고 말하는 것이 맞다. 
# https://stackoverflow.com/questions/4999533/is-lambda-a-type-of-higher-order-function

First Class-Function // Higer Order Function의 정확한 차이
First Class-Function : 함수를 객체로 사용하겠다. 변수(싱글톤 객체)에 함수를 값 할당 <- 고차함수를 포함하는 포괄적인 의미
Higer Order Function : 함수가 다른 함수에서 사용 되어 진다.(인수(인자),반환)
# 정의
# Callable(__call__)     : 함수,클래스(클래스 내 return 되는 것)들을  호출 할 수 있는지 없는지 True False로 리턴해준다. (파이썬의 내장 함수)

# 정의
# Callback Function      : (호출 가능한)함수 인자, 인자로 쓰여저 실행되면그게 콜백 함수. 
#                          자체가 고차함수이다.


# 정의
# Closure                : 일급 함수를 지원하는 언어의 네임 바인딩 기술,  일반 함수와는 다르게, 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장한 뒤, 
#                          이 캡처한 값들에 접근하는 것. 
#                          = > 쉬운 말로 클로저 실행 중(프로그램 실행중) 파이썬에서 free variables에 값을 저장하면서 실행하겠다는 말이다. 
#                          고차 언어에서 많이 쓰이는 것이지 잘못 정의하면 위의 람다처럼 고차함수처럼 쓰이지 못할 수도 있다.

# 위에서 명시한 예시 순서 대로 



# Closure
# 자유변수 :자유변수는 코드블럭안에서 사용은 되었지만, 그 코드블럭안에서 정의되지 않은 변수를
# 프로그램의 흐름을 변수에 저장할 수 있습니다. 즉, 클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용합니다
# 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용합니다

def easy_closure(k):
    # ------------외부함수와 내부함수의 영역 = 자유 변수영역 시작 = 클로저 영역 시작------------
    i = 1
    # ------------- 자유영역 종료-----------------------------
    def add_(j):
        
        return i + j
    # easy_closure 함수가 밑에서 실행 되었다고 가정하고 easy_average를 반환 해서 클로저가 선언 되었지만
    # 여전히 자유 변수 영역을 사용할수 있다.
    return add_
    # ------------클로저 영역 종료-----------------------------

# 클로저를 변수에 할당
add__ = easy_closure()
print(add__(5)) # 6

# 만약 변수에 할당하지 않고 사용한다면 프로그램의 인터프리팅 과정에서 클로저는 더 이상 고차함수가 아니다.(극단적인 예 이니까 무시하자)
print(easy_closure())

# Callback == 함수 인자

# 프로그래밍에서 콜백(callback)은 다른 코드의 인자로서 넘겨주는 실행 가능한 코드를 말한다. 

# 콜백을 넘겨받는 코드는 이 콜백을 필요에 따라 즉시 실행할 수도 있고, 아니면 나중에 실행할 수도 있다.
def add(i, j):
    """ the callback """
    return i + j

def caller(func, i, j):
    return func(i, j)

# 즉시 실행할수도 
caller(add, 1,1)
print(callable(add))

# 아무것도 실행하지 않을 수도 
# 마치 제너레이터의 생성자와 닮아 있다. 




# Callable(__call__)
# 1.대부분의 함수는 가능하다 (사용자 정의 함수도 기본적으로 __call__  매직 메서드가 내장되어 있다.)
def Geek(): 
    return None
print(callable(Geek)) # True
print(dir(Geek)) # '__call__'
# 2. 변수값은 호줄이 불가능하다. 
num = 5 * 5
print(callable(num))  # False

# 3. __call__이 정의된 클래스의 인스턴스토 사용이 가능 하다. 

# __call__이 없는 경우
class Add2:

    # 덧샘을 리턴하는 함수
    def add(self,i,j):
        return i+j


add2 = Add2()
print(callable(add2)) # False 리턴  __call__이 없으니

# __call__이 있는 경우
class Add3:

    # 덧샘을 리턴하는 함수
    def add(self,i,j):
        return i+j

    callable
    def __call__(self,i,j):
        return self.add(i,j)

add3 = Add3()
print(callable(add3)) # True 리턴 __call__ 이 있으니
