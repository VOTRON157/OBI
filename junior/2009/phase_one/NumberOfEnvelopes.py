type_candy_quantity = int(input())
if type_candy_quantity >= 1 and type_candy_quantity <= 1000:
    bullet_labels = map(int, input().split())
    if len(bullet_labels) == type_candy_quantity:
        less_number = 1000000
        for i in bullet_labels:
            if i <= less_number:
                less_number = i
        print(less_number)