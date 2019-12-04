from collections import namedtuple

# 학생 전체 그룹 생성
# 반20명 , 4개의 반-> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension in namedtuple # 첫번째 for문       # 중첩되어 있는 for문
students = [Classes(rank, number) for rank in ranks for number in numbers] 

print('EX5-1 -', len(students))
print('EX5-2 -', students)

#List Comprehension 구조 = 값 할당 || for문 || 조건문

# 가독성 X

# 아래처럼 가독성을 증가 시켜줄 수 있다.
students2 = [Classes(rank, number) 
                    for rank in 'A B C D'.split() 
                        for number in [str(n) 
                            for n in range(1,21)]]


print('EX6-1 -', len(students2))
print('EX6-2 -', students2)


# 출력
for s in students:
    print('EX7-1 -', s)

