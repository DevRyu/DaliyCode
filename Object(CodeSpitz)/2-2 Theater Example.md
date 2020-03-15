**Theater with Reservation**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-10.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-10.png "image_tooltip")


Information Expert Pattern :  정보 전문가 패턴

책임과 필요한 정보를 가진 객체에게 할당해야 캡슐화를 유지

현실 세계와 객체간은 다른 양상을 나타냄으로 정보전문가 패턴의 단점으로 적용된다.



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-11.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-11.png "image_tooltip")


고도화된 객체 지향 시스템에서는 문자열("") 숫자(1) 이 들어가지 않고 모든 것을 객체로 표현되어야 한다.

**Discount Type**

**DiscountCondition**

->조건과 액션

DiscountCondition == 수동적 개체

Iterator 패턴, Lazy Loading하기 위해



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-12.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-12.png "image_tooltip")


interface DiscountCondition { 

// 조건(외부 조건 확인)

public boolean isSatisfiedBy(Screening screening, int audienceCount); 

// 액션(발동 트리거)

public Money calculateFee(Money fee); 

}

**좋은 함수의 조건 **

인자를 하나 받는 함수가 좋은함수

인자들을 추상화 해서 객체화 시키면 하나의 인자로 만들 수 있다.

인자가 여러개 이면 충분히 추상화가 되지 않거나 형이 되지 않음

**좋은 인터페이스의 조건**

메소드가 없거나 최소한의 인터페이스

 

진정한 역할을 역할 자체를 나타 내는 것이지 어떻게 해야할지 정의하는 것이 아님으로

**DiscountPolicy**

-> Maker interface이다.

interface DiscountPolicy { 

interface AMOUNT extends DiscountPolicy { } 

interface PERCENT extends DiscountPolicy { } 

interface COUNT extends DiscountPolicy { } 

interface NONE extends DiscountPolicy{} 

}

자바에서 만큼은 enum으로 타입이 될 수 없으므로 인터페이스로 정의 된다 (가능한 언어도 있음)

**DiscountCondition을  SequenceAmountDiscount에서 상속 받는다.**


```
abstract public class SequenceDiscount implements DiscountCondition {
    private final int sequence;

    SequenceDiscount(int sequence) {
        this.sequence = sequence;
    }

    @Override
    public boolean isSatisfiedBy(Screening screening, int audienceCount) {
        return screening.sequence == sequence;
    }
}
