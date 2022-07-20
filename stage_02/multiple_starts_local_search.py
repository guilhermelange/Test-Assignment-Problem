# Busca Local Múltiplos Inicios
# Local Search Multiple Starts
import sys
import time

sys.path.insert(1, '../stage_01')
sys.path.insert(1, '../')
from utils import corrent_solution_size, objetive_function, read_instance, viable_solution
from local_search import local_search
import config

def multiple_starts_local_search(timeout):
    desks, tests, empty = config.desks, config.tests, config.empty
    desk_count = len(desks)
    test_count = len(tests)
    s_ = viable_solution(desk_count, desk_count, test_count)
    value_ = objetive_function(s_)

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time
    while execution_time < timeout:
        s = viable_solution(desk_count, desk_count, test_count)
        s, value = local_search(s, 1) # 1 = Melhor melhora

        if value < value_:
            s_ = s
            value_ = value

        current_time = time.time()
        execution_time = current_time - initial_time

    s_, value_ = corrent_solution_size(s_, empty)
    return s_, value_



if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    config.set_timeout(timeout)
    read_instance(file_name)
    s_, value_ = multiple_starts_local_search(timeout)

    print(s_)
    print(value_)
