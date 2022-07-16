# GRASP
# Greedy Randomized Adaptive Search Procedure
import sys
import time
from bls import best_improvement
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01')
from utils import objetive_function, read_instance

def GRASP(alpha, timeout):
    s_ = []
    value_ = 0

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    def random_glutton(alpha):
        if alpha >= 1:
            print('aleatório')
        else:
            print('comportamento guloso')
        return [] # Solução viável

    while execution_time < timeout:
        s = random_glutton(alpha) # Guloso Randomizado
        s = best_improvement(s)

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