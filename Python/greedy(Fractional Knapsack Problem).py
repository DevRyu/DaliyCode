# 탐욕알고리즘
# 최적의 해에 가까운 값을 구하기 위해 사용
# 여러 경우중 하나를 결정할 때 매순간 최적의 경우

# 부분 배낭 문제 (Fractional Knapsack Problem)
# - 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
#     - 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
#     - 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem 으로 부름
#         - Fractional Knapsack Problem 의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Knapsack Problem 으로 부름)

# (무게,가치) 순서 
backpack = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def fractional_knapsack(backpack, capacity):
    # 람다함수로 무게/가치의 순위를 키로 잡고 내림차순 정렬
    backpack = sorted(backpack, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    result = list()

    # 가성비 좋은 백팩의 데이터순서 대로 가방 capacity에서 무게들을 빼고 
    # 가치는 따로 total_value에 담고
    # 결과를 result에 리스트로 담음
    for data in backpack:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            result.append([data[0], data[1], 1])
        # 가방 capacity가 data보다 작아 부분적으로 쪼개서 넣을경우
        else:
            # 남은 용량에서 무개의 퍼센트를 구하고
            fractional = capacity / data[0]
            # 가치와 퍼센트를 곱함
            total_value += data[1] * fractional
            result.append([data[0], data[1], fractional])
            그 이후의 가치는 break
            break
    return total_value, result

print(fractional_knapsack(backpack, 30))
# 가치, 무게,가치,개수
(24.5, [[10, 10, 1], [15, 12, 1], [20, 10, 0.25]])

# 한계 -> 그때 상황에 따라서 최저의 값을 구할수 밖에 없다.

# - 탐욕 알고리즘은 근사치 추정에 활용
# - 반드시 최적의 해를 구할 수 있는 것은 아니기 때문
# - 최적의 해에 가까운 값을 구하는 방법 중의 하나임
