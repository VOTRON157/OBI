number_of_questions = int(input())
test_answer = input()
student_answer = input()
count = 0
for i in range(number_of_questions):
    if test_answer[i] == student_answer[i]:
        count += 1
print(count)
