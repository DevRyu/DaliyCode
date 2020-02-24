def change(coin):
    changes = 1000 - coin
    count = 0
    for i in [500, 100, 50, 10, 5, 1]:
        count += changes // i
        changes %= i
    return count
print(change(400))