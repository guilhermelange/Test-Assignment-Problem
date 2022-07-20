# Busca Local Randomizada
# Random Local Search
import sys
import time
import random
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01/')
from utils import corrent_solution_size, read_instance, objetive_function, generate_random_neighbor, viable_solution
from local_search import best_improvement
import config

def randomized_local_search(s0, p):
    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    s = s0
    s_ = s
    value_ = objetive_function(s_)
    while execution_time < timeout:
        r = random.randint(0, 1)

        if r <= p:
            s = generate_random_neighbor(s)
        else:
            s, value_strategy = best_improvement(s) # se não apresentar melhora chamar a vizinha
            if value_strategy >= value_:
                s = generate_random_neighbor(s)

        value = objetive_function(s)

        if objetive_function(s) < value_:
            s_ = s
            value_ = value

        current_time = time.time()
        execution_time = current_time - initial_time

    s_, value_ = corrent_solution_size(s_, config.empty)

    return s_, value_

if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    p = int(sys.argv[3])
    config.set_timeout(timeout)
    _, _, desks, tests, desk_empty_count = read_instance(file_name)

    initial = viable_solution(len(desks), len(desks), len(tests))
    s_, value_ = randomized_local_search(initial, p)
    print(s_)
    print(value_)