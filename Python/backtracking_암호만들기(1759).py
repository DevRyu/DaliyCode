from itertools import combinations
vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))
# 가능한 암호를 사전식으로 출력해야 하므로 정렬 수행
array = input().split(' ')
array.sort()
# 길이가 l인 모든 암호 조합을 확인
for password in combinations(array, l):
# 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
        # 최소 한 개의 모음과 최소 두 개의 자음이 있는 경우 출력
        if count >= 1 and count <= l - 2:
            print(''.join(password))