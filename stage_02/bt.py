# Busca Tabu
# Tabu Search
import sys
import time
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01')
from bls import best_improvement
from utils import objetive_function, read_instance, viable_solution

def bt(s0, d):
    def aceita(solution, M):
        if solution in M:
            return False
        else:
            return True

    def atualiza_memoria(M, d, solution): 
        if len(M) >= d:
            M = M[1:]
        M.append(solution)
        return M

    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    M = []
    s = s0
    s_ = s
    value_ = objetive_function(s_)

    # mais importante:
    # guardar no array o numer ao invés da solução inteira.
    # aceitar caso haja uma melhora no teste
    # ao gera melhor vizinho, já considerar a tabu

    while execution_time < timeout:
        s_current, _ = best_improvement(s)

        if aceita(s_current, M):
            s = s_current
        
        M = atualiza_memoria(M, d, s_current)

        value = objetive_function(s)
        if value < value_:
            s_ = s
            value_ = value

        current_time = time.time()
        execution_time = current_time - initial_time
    return s_, value_


if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    memory_size = int(sys.argv[3])
    _, _, desks, tests, desk_empty_count = read_instance(file_name)

    initial = viable_solution(len(desks), len(desks) - desk_empty_count, len(tests))
    s_, value_ = bt(initial, memory_size)
    print(s_)
    print(value_)