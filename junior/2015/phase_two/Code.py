int(input())
nums = input().split()
nova = ""
sequencias = 0

for i in nums:
    nova += i
    if(nova.endswith("100")): sequencias +=  1
print(sequencias)