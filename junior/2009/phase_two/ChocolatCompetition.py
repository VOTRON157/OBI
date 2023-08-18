chocolate_amount, allowed_amount = map(int, input().split())
if chocolate_amount % (allowed_amount + 1) == 0:
    print("Carlos")
else:
    print("Paula")