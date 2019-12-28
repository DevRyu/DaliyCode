# 정규화 :정규화는 전체구간을 0~100으로 설정하여 데터터를 관찰 
def normalize(x, x_min, x_max):

    normalized = (x-x_min) / (x_max-x_min)

    return normalized