import random
import time

min_operand = 2
max_operand = 12
operators = ["+", "-", "*"]
Total_round = 3

def generate_number():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

input("Press Enter to Start the Game!")
print("----------------------------")

start_time = time.time()

wrong = 0
for i in range(Total_round):
    expr, answers = generate_number()
    while True:
        guess = input("Problem #" + str(i+1) + ' : ' + expr + " = ")
        if guess == str(answers):
            break
        wrong += 1

end_time = time.time()
total_time = round(start_time - end_time, 2)

print(f"Nice Work! you're total time is: {total_time}")
print("----------------------------")

