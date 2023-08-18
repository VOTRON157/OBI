days_quantity = int(input())
price_variation = input().split()
total_sum = -100
running_sum = 0
while len(price_variation) >= 4:
    for i in range(4):
        running_sum += int(price_variation[i])
    if running_sum > total_sum:
        total_sum = running_sum
    running_sum = 0
    price_variation.pop(0)
print(total_sum)