import time
import sys
sys.path.insert(1, '../')
from utils import read_instance, viable_solution, objetive_function, correct_solution, random_neighbor, corrent_solution_size
import config

# Local Search
# Caminhada Aleatória
# Random Walk
def random_walk(timeout):
    desks, tests, empty = config.desks, config.tests, config.empty
    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time
    desk_count = len(desks)
    test_count = len(tests)

    response_solution = viable_solution(desk_count, desk_count, test_count)
    objetive = objetive_function(response_solution)

    while execution_time < timeout:
        current_solution = random_neighbor(response_solution)
        solution = objetive_function(current_solution)

        if solution < objetive:
            response_solution = current_solution
            objetive = solution

        current_time = time.time()
        execution_time = current_time - initial_time

    response_solution, objetive = corrent_solution_size(response_solution, empty)

    return response_solution, objetive

if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    read_instance(file_name)

    response_solution, objetive = random_walk(timeout)
    print('Resposta: ', response_solution, '\n', objetive)

    

