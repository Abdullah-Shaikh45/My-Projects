import random
import time

min_operand = 2
max_operand = 12
operators = ["+", "-", "*"]
total_rounds = 3

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
for i in range(total_rounds):
    expr, answer = generate_number()
    while True:
        guess = input("Problem #" + str(i + 1) + ' : ' + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print(f"Nice Work! Your total time is: {total_time} seconds")
print(f"Total incorrect attempts: {wrong}")
print("----------------------------")
