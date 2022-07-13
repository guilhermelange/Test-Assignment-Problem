import random
import time
import sys
sys.path.insert(1, '../')
from utils import read_instance, viable_solution, objetive_function, correct_solution

def execute():
    def random_walk(current_solution):
        idx = random.randint(0, desk_count-1)

        tests_numbers = list(range(1, test_count))
        tests_numbers.remove(current_solution[idx])

        current_solution[idx] = random.choice(tests_numbers)
        return current_solution

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time
    desk_count = len(desks)
    test_count = len(tests)

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

    response_solution = correct_solution(response_solution, desk_count, empty)
    objetive = objetive_function(distance, similarity, response_solution)

    return response_solution, objetive

if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    distance, similarity, desks, tests, empty = read_instance(file_name)

    response_solution, objetive = execute()
    print()
    print('Resposta: ', response_solution, '\n', objetive)

    

