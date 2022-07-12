from main import read_instance, viable_solution, objetive_function
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

viable_solution = viable_solution(desk_count, desk_count - empty, test_count)
objetive = objetive_function(distance, similarity, viable_solution)

def random_walk(current_solution):
    return current_solution

while execution_time < timeout:
    current_solution = random_walk(viable_solution)
    solution = objetive_function(distance, similarity, current_solution)
    print('current_solution', current_solution)
    print('solution', solution)

    
    if solution < objetive:
        objetive = solution
        viable_solution = current_solution
    break
    current_time = time.time()
    execution_time = current_time - initial_time