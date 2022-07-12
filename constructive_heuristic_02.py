from main import read_instance, objetive_function
import random
import time
import sys

file_name = sys.argv[1]
timeout = int(sys.argv[2])

distance, similarity, desks, tests, empty = read_instance(file_name)
desk_count = len(desks)
test_count = len(tests)
initial_time = time.time()
current_time = time.time()
execution_time = current_time - initial_time

def viable_solution(size, test_count):
    selected = [random.randint(1, test_count-1) for _ in range(size)]
    return selected

def correct_solution(current_solution):
    for i in range(len(current_solution)):
        if current_solution[i] == 0:
            current_solution[i] = random.randint(1, test_count-1)

    for i in random.sample(range(desk_count), empty):
        current_solution[i] = 0
    return current_solution


s = viable_solution(desk_count, test_count)
best_value = objetive_function(distance, similarity, s)

while execution_time < timeout:
    current_s = correct_solution(s)
    current_value = objetive_function(distance, similarity, current_s)

    if current_value < best_value:
        s = current_s
        best_value = current_value

    current_time = time.time()
    execution_time = current_time - initial_time

print(s)
print(best_value)