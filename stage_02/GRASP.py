# GRASP
# Greedy Randomized Adaptive Search Procedure
import sys
import time
from semi_greedy import semi_greedy
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01')
from bls import best_improvement
from utils import objetive_function, read_instance

def GRASP(alpha, timeout):
    s_ = []
    value_ = 1000000

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    while execution_time < timeout:
        s, _ = semi_greedy(alpha) # Guloso Randomizado
        s, _ = best_improvement(s)

        value = objetive_function(s)
        if value <= value_:
            value_ = value
            s_ = s

        current_time = time.time()
        execution_time = current_time - initial_time

    return s_, value_

if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    alpha = int(sys.argv[3])
    read_instance(file_name)

    s_, value_ = GRASP(alpha, timeout)
    print(s_)
    print(value_)