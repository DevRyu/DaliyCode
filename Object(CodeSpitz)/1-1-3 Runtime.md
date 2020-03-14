**Program Timing**

Program 정의 

메모리에 적재되서 실행 될 때 프로그램이라고 함

(Compile language)Program LifeCycle 

**Language Code      : Lint Time          # 코드 작성 ## 코드품질을 위해서 lint 검사**

**Machine Language : Compile Time  # 기계어로 변환 ## 기계어로 번역 & 번역 시 에러 잡음**

File 				              # 파일로 변환 ## load에서 한 꺼번에 적재

					  # 프로그램 시작

Load 					  # 메모리 적재 **## 실행동안 Load &lt;-> Run 반복  **

**Run                         : Run Time 	  # 실행 ## 실행하는 동안의 에러 예)Recursive**

Terminate				  # 프로그램 종료

Runtime에러 안에 context error가 있음(실행 안해보면, 에러를 사전에 잡을 수 없음)(에러 구현 불가능)(제한된 환경에서 가능)

그래서 Runtime error를 Lint, Compile Time으로 앞당겨서 잡아야 한다.

(Script language)Program LifeCycle

**Language Code      : Lint Time          # 코드 작성 ## 코드품질을 위해서 lint 검사**

File 				              # 파일로 변환

					  # 프로그램 시작

Load 					  # 메모리 적재 **## 실행동안 Load &lt;-> Run 반복  **

Machine Language			  # 기계어로 변환 (한줄 한줄 씩)

**Run                         : Run Time 	  # 실행 ## 실행하는 동안의 에러 예)Recursive**

Terminate				  # 종료

Load&lt;->Machine Language 간 에러는 Syntex Error고

나머지 에러는 Runtime Error 
