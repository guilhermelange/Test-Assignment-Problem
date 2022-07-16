# Busca Local Múltiplos Inicios
# Local Search Multiple Starts
import sys
import time
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01/')
from utils import objetive_function, read_instance, viable_solution
from bls import best_improvement
import config

def blmi():
    desks, tests, empty, timeout = config.desks, config.tests, config.empty, config.timeout
    desk_count = len(desks)
    test_count = len(tests)
    s_ = viable_solution(desk_count, desk_count - empty, test_count)
    value_ = objetive_function(s_)

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time
    while execution_time < timeout:
        s = viable_solution(desk_count, desk_count - empty, test_count)
        s, value = best_improvement(s)

        if value < value_:
            s_ = s
            value_ = value

        current_time = time.time()
        execution_time = current_time - initial_time

    return s_, value_



if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    config.set_timeout(timeout)
    read_instance(file_name)
    s_, value_ = blmi()




    print(s_)
    print(value_)
