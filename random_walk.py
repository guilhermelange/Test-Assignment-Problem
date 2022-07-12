from main import read_instance, viable_solution, objetive_function
import random
import time
import sys

file_name = sys.argv[1]
timeout = int(sys.argv[2])

distance, similarity, desks, tests, empty = read_instance(file_name)

initial_time = time.time()
current_time = time.time()
execution_time = current_time - initial_time
desk_count = len(desks)
test_count = len(tests)



def random_walk(current_solution):
    idx = random.randint(0, desk_count-1)

    tests_numbers = list(range(1, test_count))
    tests_numbers.remove(current_solution[idx])

    current_solution[idx] = random.choice(tests_numbers)
    return current_solution

def correct_solution(current_solution):
    for i in random.sample(range(desk_count), empty):
        current_solution[i] = 0
    return current_solution

response_solution = viable_solution(desk_count, desk_count, test_count)
objetive = objetive_function(distance, similarity, response_solution)

while execution_time < timeout:
    current_solution = random_walk(response_solution)
    solution = objetive_function(distance, similarity, current_solution)

    if solution < objetive:
        response_solution = current_solution
        objetive = solution

    current_time = time.time()
    execution_time = current_time - initial_time

print('Resposta: ', response_solution, '\n', objetive)