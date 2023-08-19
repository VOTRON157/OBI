numerator_one, denominator_one, numerator_two, denominator_two = map(int, input().split())
count = 1
switch = 0
mmc = 0
while switch == 0:
    if (denominator_one * count) % denominator_two == 0:
        mmc = denominator_one * count
        switch = 1
    else:
        count += 1
numerator_result = (mmc / denominator_one) * numerator_one + (mmc / denominator_two) * numerator_two
denominator_result = mmc
switch = 0
count = 2
while switch == 0:
    if numerator_result % count == 0 and denominator_result % count == 0:
        switch = 1
    else:
        if count >= max(numerator_result, denominator_result):
            switch = 1
        else:
            count += 1
if count >= max(numerator_result, denominator_result):
    print(numerator_result, denominator_result)
else:
    print(numerator_result / count, denominator_result / count)