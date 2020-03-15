변수는 메모리주소의 별명

**Type(형)**

데이터 타입은 메모리에서의 길이

(아래의 설명은 참조타입)

Role : 형을 통해 역할을 묘사함

Responsibility : 형을 통해 로직을 표현함(함수도 하나의 형(강타입 컴파일일시))

Message(주고 받는 메세지) : 형을 통해 메세지를 공유함 (메세지 함수의 인자는 형으로 표현)

Protocol : 객체 간 계약을 형을 통해 공유함

**Supported types**

Java 기준으로

static : 단 한개의 인스턴스가 존재(동시성 문제를 해결해야 함)

-> static인 경우 factory(하나의 인스턴스 만들어주는 공장)이거나, utility(상태를 갖지 않는경우)인 경우

-->유틸리티 함수인 경우this,self가 없다면 utility 임으로 static이고 해당 클래스 메소드에서 제거 해야 함

enum : 제한된 수의 인스턴스가 존재 (제네릭 사용불가) ->동시성, 안정성 확보를 위해

class : 무제한의 인스턴스가 존재

**condition(조건)**

1.조건 분기는 결코 제거 할 수 없다.

2단계 조건 분기 이상으로 진행 한다면 이해하기 어렵기 때문에 

1단계 조건 분기만을 가져야 한다.

예)코딩에서 대체로 진리표를 짜고 분기문을 작성하 작성하지 않기 때문에 5번의 분기로 테스트케이스가 통과해서 6번째에서 제대로 작동 할 수 있을지 장담하기 어렵기 때문 

2. 조건 분기에 대한 전략은 두가지 뿐이다. 

1) 내부에서 응집성있게 모아두는 방식

     장점: 모든 경우의 수를 한 곳에서 파악할 수 있다.

     단점: 분기가 늘어날 때마다 코드가 변경된다.(회귀 테스트)



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-10.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-10.png "image_tooltip")


**2) 외부에 분기를 위임하고 경우의 수 만큼 처리기를 만드는 방식**

     장점: 분기가 늘어날 때마다 처리기만 추가하면 된다.

     단점: 모든 경우의 수를 파악할 수 없다.

     ex)스프링 라우터,전략패턴



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-11.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-11.png "image_tooltip")


main은 클라이언트측 코드, 클라이언트의 요구에 따른 변화되는 코드

processConidtion은 라이브러리 코드

분기를 라이브러리 코드에서  클라이언트 코드로 가져가게 하는 것이 목적 

**중간 정리**

조건은 외부에 분기를 위임하고 경우의 수 만큼 처리기를 만드는 방식으로 하면

변화율에 따른 분기를 해서 격리를 할수 있다

**Responsibility Driven**

**value = responsibility**

1)시스템의 존재 가치는 사용자에게 제공되는 기능

2)사용자가 사용할 기능 = 시스템의 책임

**책임** : 알고리즘이 들어가 있는 코드(기능)

3)시스템 차원의 책임을 더 작은 단위의 책임으로 분할

응집성이 높으며 결합도가 낮게 쪼갠다.

4)해당 책임을 추상화하여 역할을 정의함

**역할** : 책임은 기능, 책임들의 공통점을 모은(추상화) 그룹

연역적인 방법으로 역할을 만들고 다시 귀납적으로 책임을 만들 수 있다.



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-12.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-12.png "image_tooltip")


다양한 분기 케이스(책임)에서  Runnable(역할)로 추상화가 된다.

위의 그림을 통해 책임들과 역할로 귀납과 연역을 황용해 

분기 케이스를 수정 하기도, 역할을 수정 하기도 할 수있다.

(만약 함수에 인자가 추가가 되면 전체적으로 수정되기 때문에

도메인을 깊게 이해한다면 처음부터 잘 설계를 할 수 있다.)

5)역할에 따라 협력이 정의됨

책임 단계에서 협력 단계를 정의 하면 안된다.

책임이 수정되면 협력관계 또한 수정이 된다. 
