### **Discount Type(implement inversion)**

public class AmountDiscount implements DiscountPolicy.AMOUNT , SequenceDiscount{

    private final Money amount;

    public SequenceAmountDiscount(Money amount){

        this.amount = amount;

    }

    @Override

    public Money calculateFee(Money fee){

        return fee.minus(amount);

    }

}

public class PercentDiscount implements DiscountPolicy.PERCENT ,

 SequenceDiscount{

    private final double percent;

    public SequenceAmountDiscount(double percent){

        this.percent = percent;

    }

    @Override

    public Money calculateFee(Money fee){

        return fee.minus(fee.multi(percent));

    }

}

분기(if)를 제거하는 방법으로 제너릭을 사용 -> **외부에 분기를 위임하고 경우의 수 만큼 처리기를 만드는 방식 **(클래스 명 자체가 분기의 조전을 가지고 있는 경우가 있음)

if를 제네릭으로 대체하면 컴파일러가 제공하는 형이다.

**Movie class**

public class Movie&lt;T extends DiscountPolicy & DiscountCondition> {

    private final String title;

    private final Duration runningTime;

    private final Money fee;

    private final Set&lt;T> discountConditions = new HashSet&lt;>();

    public Movie(String title, Duration runningTime, Money fee, T... conditions) {

        this.title = title;

        this.runningTime = runningTime;

        this.fee = fee;

        this.discountConditions.addAll(Arrays.asList(conditions));

    }

    Money calculateFee(Screening screening, int audienceCount) {

        for (T condition : discountConditions) {

            if (condition.isSatisfiedBy(screening, audienceCount)) {

                return condition.calculateFee(fee).multi((double) audienceCount);

            }

        }

        return fee;

    }

}

<sub>위 제네릭에서 </sub>discountConditions<sub>  List가 아닌 Set</sub>

<sub> Container에서 값 context가 아니기 때문, 객체 context 사용이 되기 때문</sub>


### **Value Object(값 객체)**

특징 : 불변성(final), 새로운 객체로 반환(값을 갱신할 수 없음)

public class Money{ //Value Object

    public static Money of(Double amount){}

    private final Double amount; 

-------------위 데이터를 내부로 은닉-------------

-------------아래는 외부에 api를 통해 연산의 안정성 제공-------- 

   public Money minus(Money amount) {

        return new Money(this.amount > amount.amount ? this.amount - amount.amount : 0.0);

    }

    public Money multi(Double times) {

        return new Money(this.amount * times);

    }

    public Money plus(Money amount) {

        return new Money(this.amount + amount.amount);

    }

    public boolean greaterThen(Money amount) {

        return this.amount >= amount.amount;

    }

}

-> 동시성 문제를 해결


#### **reservation**

순수한 값 객체 

예 1)(이펙티브 자바 예시)

public class Reservation {

    static final Reservation NONE = new Reservation(null, null, null, 0);

    final Theater theater;

    final Movie movie;

    final Screening screening;

    final int count;

    Reservation(Theater theater, Movie movie, Screening screening, int audienceCount) {

        this.theater = theater;

        this.movie = movie;

        this.screening = screening;

        this.count = audienceCount;

    }

}

예 2)

public class Screening {

    private int seat;

    final int sequence;

    final LocalDateTime whenScreened;

    public Screening(int sequence, LocalDateTime when, int seat) {

        this.sequence = sequence;

        this.whenScreened = when;

        this.seat = seat;

    }

// trigger & action : 외부에서 사용하기위해서 정의

// trigger

    boolean hasSeat(int count) {

        return this.seat >= count;

    }

// action

    void reserveSeat(int count) {

        if (hasSeat(count)) seat -= count;

        else throw new RuntimeException("no seat");

    }

}

**Theater**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-20.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-20.png "image_tooltip")


**class Theater **

class Theater {

    public static final Set&lt;Screening> EMPTY = new HashSet&lt;>();

    private final Set&lt;TicketOffice> ticketOffices = new HashSet&lt;>();

    private final Map&lt;Movie, Set&lt;Screening>> movies = new HashMap&lt;>();

    private Money amount;

    public Theater(Money amount) {

        this.amount = amount;

    }

    public boolean addMovie(Movie movie) {

        if (this.movies.containsKey(movie)) return false;

        movies.put(movie, new HashSet&lt;>());

        return true;

    }

    public boolean addScreening(Movie movie, Screening screening) {

        if (!this.movies.containsKey(movie)) return false;

        return movies.get(movie).add(screening);

    }

// -------------------------------------------------------------------

    public boolean contractTicketOffice(TicketOffice ticketOffice, Double rate) {

        if (!ticketOffice.contract(this, rate)) return false;

        return this.ticketOffices.add(ticketOffice);

    }

    public boolean cancelTicketOffice(TicketOffice ticketOffice) {

        if (!this.ticketOffices.contains(ticketOffice) || !ticketOffice.cancel(this)) return false;

        return this.ticketOffices.remove(ticketOffice);

    }

// 값 객체를 쓸 때는 외부로 노출되면 안됨(현재 Pointer of Pointer 를 지키지 못함)

    void plusAmount(Money amount) {

        this.amount = this.amount.plus(amount);

    }

// -------------------------------------------------------------------

    public Set&lt;Screening> getScreening(Movie movie) {

        if (!this.movies.containsKey(movie) || this.movies.get(movie).size() == 0) return EMPTY;

        return this.movies.get(movie);

    }

    boolean isValidScreening(Movie movie, Screening screening) {

        return movies.containsKey(movie) && movies.get(movie).contains(screening);

    }

// -------------------------------------------------------------------

    public boolean enter(Customer customer, int count) {

        Reservation reservation = customer.reservation;

        return reservation != Reservation.NONE &&

                reservation.theater != this &&

                isValidScreening(reservation.movie, reservation.screening) &&

                reservation.count == count;

    }

Reservation reserve(Movie movie, Screening screening, int count) {

        if (!isValidScreening(movie, screening) || !screening.hasSeat(count)) return Reservation.NONE;

        screening.reserveSeat(count);

        return new Reservation(this, movie, screening, count);

    }

}

// -------------------------------------------------------------------

public class TicketOffice {

    private Money amount;

    private Map&lt;Theater, Double> commissionRate = new HashMap&lt;>();

    public TicketOffice(Money amount) {

        this.amount = amount;

    }

    boolean contract(Theater theater, Double rate) {

        if (commissionRate.containsKey(theater)) return false;

        commissionRate.put(theater, rate);

        return true;

    }

    boolean cancel(Theater theater) {

        if (!commissionRate.containsKey(theater)) return false;

        commissionRate.remove(theater);

        return true;

    }

// -------------------------------------------------------------------

    Reservation reserve(Theater theater, Movie movie, Screening screening, int count) {

        if (!commissionRate.containsKey(theater) ||

                !theater.isValidScreening(movie, screening) ||

                !screening.hasSeat(count)

        ) return Reservation.NONE;

        Reservation reservation = theater.reserve(movie, screening, count);

        if (reservation != Reservation.NONE) {

            Money sales = movie.calculateFee(screening, count);

            Money commission = sales.multi(commissionRate.get(theater));

            amount = amount.plus(commission);

            theater.plusAmount(sales.minus(commission));

        }

        return reservation;

    }

}

// -------------------------------------------------------------------

public class TicketSeller {

    private TicketOffice ticketOffice;

    public void setTicketOffice(TicketOffice ticketOffice){

        this.ticketOffice = ticketOffice;

    }

    Reservation reserve(Customer customer, Theater theater, Movie movie, Screening screening, int count){

        Reservation reservation = Reservation.NONE;

        Money price = movie.calculateFee(screening, count);

        if(customer.hasAmount(price)){

            reservation = ticketOffice.reserve(theater,movie,screening,count);

            if(reservation != Reservation.NONE) customer.minusAmount(price);

        }

        return reservation;

    }

}

// -------------------------------------------------------------------

public class Customer {

    Reservation reservation = Reservation.NONE;

    private Money amount;

    public Customer(Money amount) {

        this.amount = amount;

    }

    public void reserve(TicketSeller seller, Theater theater, Movie movie, Screening screening, int count) {

        reservation = seller.reserve(this, theater, movie, screening, count);

    }

    boolean hasAmount(Money amount) {

        return this.amount.greaterThen(amount);

    }

    void minusAmount(Money amount) {

        this.amount = this.amount.minus(amount);

    }

}

다시 위의 시나리오 코드를



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-21.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-21.png "image_tooltip")



```
-SequenceAmountDiscount로 if문 제거됨
```




<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/-22.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/-22.png "image_tooltip")
