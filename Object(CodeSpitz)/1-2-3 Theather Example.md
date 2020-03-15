**Theater 예시**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-1-1-20.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-1-1-20.png "image_tooltip")


잘못된 설계(절차지향적?)



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-1-1-21.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-1-1-21.png "image_tooltip")


위의 그림으로 설명

화살표를 받는 쪽 보다 주는 쪽이 많이 정보를 제공해 줘야 한다.

의인화를 통해서 객체를 설계하면 객체간의 의존도를 식별 할 수 있다.

**Theater**

**Ticket**

this == EMPTY 식별자로 식별

**Invitation**

**TicketOffice**

**TicketSeller**

코드가 물 흐르듯 읽혀 질려면 많이 해보는 방법밖에 없음

특히 제어문을 내 생각 대로 표현하는 것이 어려움

객체설계에서 도메인을 평가 했을 때 

어떤 로직이 어떤 변화율과 어떤 값으로 변화 하는지 나누는 눈이 필요함

**Audience**

결론

Main에서 도메인에 맞는 시나리오를 먼저 짜고 각 도메인별 클래스를 작성하자

(객체들을 먼저 생성하고 객체들이 어떻게 협력하는지 보고 클래스를 명세 하는 것이 좋다)

(TDD)테스트 코드로 설계를 반영할려면 어렵기 때문에 위의 시나리오 별로 하는 것이 더쉽다.
