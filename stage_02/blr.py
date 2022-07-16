# Busca Local Randomizada
# Random Local Search
import sys
import time
import random
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01/')
from utils import read_instance, objetive_function, generate_random_neighbor, viable_solution
from bls import best_improvement
import config

def blr(s0, p):
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
            s = best_improvement(s)

        value = objetive_function(s)

        if objetive_function(s) < value_:
            s_ = s
            value_ = value

        current_time = time.time()
        execution_time = current_time - initial_time

    return s_, value_

if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    p = int(sys.argv[3])
    config.set_timeout(timeout)
    _, _, desks, tests, desk_empty_count = read_instance(file_name)

    initial = viable_solution(len(desks), len(desks) - desk_empty_count, len(tests))
    s_, value_ = blr(initial, p)
    print(s_)
    print(value_)