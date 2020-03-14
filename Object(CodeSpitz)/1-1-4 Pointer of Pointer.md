**Pointer of Pointer**

특정 포인터를 직접 값으로 찾지 않고 

특정 포인터로 원하는 값 주소를 가진 포인터를 찾고 난 후 그 값을 얻겠 다는 의미

**참조전파(직접 참조시의 모순 발생)**

**B 값 변경 전**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-1-10.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-1-10.png "image_tooltip")


**B 값 변경 후**



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-1-11.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-1-11.png "image_tooltip")


B=&K 로 B의 값을 바꾸어도 

C,D는 이전에 11이라는 값을 할당 받은 상태임으로 &A의 11을 가리킴

ex)객체 생성 시점(setter)에서 내가 가져온 reference가 변하지 않았다는 믿음

-> 의도되로 프로그램의 결과가 나오지 않게 됨

**간접참조로 문제 해결**



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-1-12.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-1-12.png "image_tooltip")


B값이 중간에 바뀌어도 C,D가 동일한 값 을 가르킴

런타임에서 참조의 참조(Pointer of Pointer)는 연쇄 되면 링크드리스트, 데코레이터, 체이닝의 원리이고 동적바인딩의 개념

Pointer of Pointer를 사용하는 것이 런타임에서 안전하다.

그래서 객체지향에서는 값이 아닌 참조를 사용한다.
