**RunTime내부에서 동작하는 과정**

**Compile Program**

cpu : 제어유닛(디코더),연산유닛(제어정보),데이터유닛(메모리계수기),외부버스

메모리 : 명령 | 값

**폰노이만 머신 기반 연산**

**1)Loading**

**2)Instruction Fetch & Decode**

**3)Execute**

자세하게



이미지

1. Fetch(메모리 명령 -> 제어유닛)

2. Decoding(제어유닛에서 명령어 해석)

3. 명령어 연산유닛으로 가져오고 연산 Execute(제어유닛 -> 연산유닛)

4. 값을 데이터유닛 Load(값->데이터유닛)

5. 데이터유닛의 값을 연산유닛으로 Load(데이터유닛 -> 연산유닛)

6. 연산유닛에서 명령과 값을 Execute

7. 연산유닛에서 실행한 결과 데이터 유닛으로

8. 결과값을 다시 메모리의 값으로 Store

요약

위의 그림처럼 메모리에 명령어,값이 적재 된 시점 부터 모든 명령이 해소되어 종료되는 시점까지

프로그램의 생명주기

동기적으로 실행 후 메모리에 적재 된 모든 명령어가 실행되면 프로그램은 종료

**Essential Definition Loading**

메모리에 명령어 값이 적재되면 최초의 프로그램 실행시 Essential Definition을 Loading한다.

**Vtable Mapping**

코드내 변수의 가상 메모리주소와 변수의 실제 메모리 주소를 맵핑한다.

왜냐하면 코드는 IDE내에서는 단지 Text이고, Compile단계에서 가상의 메모리 주소로 미리 할당?받아 Compile작업을 해서, 실제 메모리주소에 들어갈 때 가상의 매모리 주소dhk Mapping단계를 거친다

**Run**

프로그램 실행

**Runtime Definition Loading**

프로그램 실행 중에 class,func 정의

ex) c,js의 경우 실행 도중에 runtime내에서 class,func 정의

     단 java의 경우 ClassLoader 로 runtime loading을 한다.

**Run**

Runtime Definition Loading 이후 또 프로그램 실행

**Script Program**


이미지

**Run**

컴파일 단계 없이 실행부터 됨

Run time 내에서도 아래 1),2)로 쪼갤 수가 있다

왜냐하면 보는 관점 (전체적, 부분적)에 따라 다를 수 있기 때문에 절대적이지 않다.(상대적) 

1)static time(선언)

2)run time(실행)
