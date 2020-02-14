def maxInversions(prices):
    count = 0
    length_price = len(prices)
    for i in range(1, length_price - 1):
        top = 0

        for j in range(i - 1, -1, -1):
            if prices[i] < prices[j]:
                top += 1

        bottom = 0
        for j in range(i + 1, length_price):
            if prices[i] > prices[j]:
                bottom += 1

        count += top * bottom
        
    return count


print(maxInversions([10,7,4,5,11]))
print(maxInversions([8, 6, 1, 4, 5]))
print(maxInversions([4,1,3,2,5]))