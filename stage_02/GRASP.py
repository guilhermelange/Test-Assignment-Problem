# GRASP
# Greedy Randomized Adaptive Search Procedure
import sys
import time
from semi_greedy import semi_greedy
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01')
import config
from local_search import local_search
from utils import corrent_solution_size, objetive_function, read_instance

def GRASP(alpha, timeout):
    s_ = []
    value_ = 1000000

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    while execution_time < timeout:
        s, _ = semi_greedy(alpha, 0) # Guloso Randomizado
        s, _ = local_search(s, 1) # Melhor melhora

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
    alpha = int(sys.argv[3])
    read_instance(file_name)

    s_, value_ = GRASP(alpha, timeout)
    print(s_)
    print(value_)