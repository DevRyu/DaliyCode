# 탐욕알고리즘
# 최적의 해에 가까운 값을 구하기 위해 사용
# 여러 경우중 하나를 결정할 때 매순간 최적의 경우

# 동전문제
# - 지불해야 하는 값이 4720원 일 때 1원 50원 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
# - 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
# - 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨
# - coin_list = [1, 100, 50, 500]

# 동전을 가장 큰 순서 대로 정렬
coin_list = [1, 100, 50, 500]
print (coin_list)
coin_list.sort(reverse=True)
print (coin_list)
#[500, 100, 50, 1]

# value 4720원, coin_list 코인 종류
def greedy_coin(value,coin_list):
    total_coin_count =0
    pocket = list()
    coin_list.sort(reverse = True)
    for coin in coin_list:
        # 가장 큰 코인으로 나눌수 있는 만큼 나눈후 캐수를 coin_num에 저장
        coin_num = value // coin
        # 코인의 개수를 충 개수에 더함
        total_coin_count += coin_num
        # 위에 구한 코인종류와 개수를 곱해 서 총 value에서 뻄
        value -= coin_num * coin
        # 코인 종류와 코인 개수를 추가
        pocket.append([coin,coin_num])
    return pocket,total_coin_count

greedy_coin(4720, coin_list)
