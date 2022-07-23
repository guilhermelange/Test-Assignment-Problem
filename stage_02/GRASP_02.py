# GRASP
# Greedy Randomized Adaptive Search Procedure
import sys
import time
from semi_greedy import semi_greedy
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01')
import config
from local_search import local_search
from constructive_heuristic_01 import constructive_heuristic_01
from utils import corrent_solution_size, objetive_function, read_instance

# GRASP + constructive_heuristic_01 + first_improvment
def GRASP(timeout):
    s_ = []
    value_ = 1000000

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    while execution_time < timeout:
        s, _ = constructive_heuristic_01(False) # Heurística Construtiva 01
        s, _ = local_search(s, 0) # Primeira melhora

        value = objetive_function(s)
        if value <= value_:
            value_ = value
            s_ = s

        current_time = time.time()
        execution_time = current_time - initial_time

    s_, value_ = corrent_solution_size(s_, config.empty)

    return s_, value_

if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    read_instance(file_name)

    s_, value_ = GRASP(timeout)
    print(s_)
    print(value_)