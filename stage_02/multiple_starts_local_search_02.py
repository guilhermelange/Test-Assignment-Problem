# Busca Local Múltiplos Inicios
# Local Search Multiple Starts
import sys
import time
from stage_02.semi_greedy import semi_greedy

sys.path.insert(1, '../stage_01')
sys.path.insert(1, '../')
from utils import corrent_solution_size, objetive_function, read_instance, viable_solution
from local_search import local_search
import config

# Busca local múltiplos inícios + semi-guloso alpha + busca local primeira melhora
def multiple_starts_local_search(alpha, timeout):
    desks, tests, empty = config.desks, config.tests, config.empty
    desk_count = len(desks)
    test_count = len(tests)
    s_ = viable_solution(desk_count, desk_count, test_count)
    value_ = objetive_function(s_)

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time
    while execution_time < timeout:
        s, _ = semi_greedy(alpha, False)
        s, value = local_search(s, 0) # 1 = Primeira  melhora

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
    alpha = int(sys.argv[3])
    config.set_timeout(timeout)
    read_instance(file_name)
    s_, value_ = multiple_starts_local_search(alpha, timeout)

    print(s_)
    print(value_)
