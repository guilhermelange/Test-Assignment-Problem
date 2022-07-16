import time
import sys
sys.path.insert(1, '../')
from utils import read_instance, objetive_function, correct_solution_v2, viable_solution
import config

# Heurística Construtiva 02
# Constructive Heuristic 02
def constructive_heuristic_02(timeout):
    desks, tests, empty = config.desks, config.tests, config.empty
    desk_count = len(desks)
    test_count = len(tests)
    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    s = viable_solution(desk_count, desk_count, test_count)
    best_value = objetive_function(s)

    while execution_time < timeout:
        current_s = correct_solution_v2(s, desk_count, test_count, empty)
        current_value = objetive_function(current_s)

        if current_value < best_value:
            s = current_s
            best_value = current_value

        current_time = time.time()
        execution_time = current_time - initial_time

    return s, best_value

if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])

    read_instance(file_name)

    response_solution, objetive = constructive_heuristic_02(timeout)
    print()
    print(response_solution)
    print(objetive)

