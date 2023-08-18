bits_number, dividend, divider = map(int, input().split())
if dividend < bits_number and divider < bits_number:
    print(dividend, divider)
else:
    if dividend / 10 < bits_number and divider / 10 < bits_number:
        if dividend / 10 > 1 and divider / 10 > 1:
            print(int(dividend / 10), int(divider / 10))
        else:
            print("IMPOSSÍVEL")