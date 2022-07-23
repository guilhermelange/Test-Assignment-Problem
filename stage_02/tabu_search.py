# Busca Tabu
# Tabu Search
import sys
import time
sys.path.insert(1, '../')
sys.path.insert(1, '../stage_01')
import config
from utils import corrent_solution_size, objetive_function, read_instance, viable_solution
from local_search import first_improvement

# Busca Tabu + primeira melhora
def tabu_search(s0, d):
    initial_time = time.time()
    current_time = time.time()
    execution_time = current_time - initial_time

    empty = config.empty
    desk_count = len(config.desks)
    M = [0 for i in range(desk_count)]
    s = s0
    s_ = s
    value_ = objetive_function(s_)
    value = value_
    last_index_tabu = 0

    # mais importante:
    # guardar no array o numer ao invés da solução inteira.
    # aceitar caso haja uma melhora no teste
    # ao gera melhor vizinho, já considerar a tabu

    count = 0
    while execution_time < timeout:
        count += 1
        s_current, _, index_tabu = first_improvement(s, M, value_, count, d) # Aceita está contido na geração da vizinhança
        s = s_current
        
        if index_tabu < 0: # Nao localizada index pra mudar
            M = [0 for i in range(desk_count)] # reinicia lista tabu
            index_tabu = last_index_tabu
        else:
            last_index_tabu = index_tabu

        M[index_tabu] = count # atualiza memória
        
        value = objetive_function(s)
        if value < value_:
            s_ = s
            value_ = value

        current_time = time.time()
        execution_time = current_time - initial_time
        

    corrent_solution_size(s_, empty)
    return s_, value_


if __name__ == '__main__':
    file_name = sys.argv[1]
    timeout = int(sys.argv[2])
    memory_size = int(sys.argv[3])
    _, _, desks, tests, desk_empty_count = read_instance(file_name)

    initial = viable_solution(len(desks), len(desks) - desk_empty_count, len(tests))
    s_, value_ = tabu_search(initial, memory_size)
    print(s_)
    print(value_)