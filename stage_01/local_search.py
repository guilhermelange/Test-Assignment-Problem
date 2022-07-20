import sys
sys.path.insert(1, '../')
from utils import corrent_solution_size, objetive_function, read_instance, viable_solution
import config

# Primeira Melhora
# first improvement
def first_improvement(viable_solution):
    tests = config.tests
    final_soluction = viable_solution.copy()
    final_objetive = objetive_function(viable_solution)

    for desk in range(0, len(viable_solution)):
        for test in range(1, len(tests)):
            alt_soluction = viable_solution.copy()
            if(test != viable_solution[desk]):
                alt_soluction[desk] = test
                alt_objetive = objetive_function(alt_soluction)
                if(alt_objetive < final_objetive):
                    return alt_soluction, alt_objetive

    return final_soluction, final_objetive

# Melhor Melhora
# best improvement
def best_improvement(viable_solution):
    tests = config.tests
    final_soluction = viable_solution.copy()
    final_objetive = objetive_function(viable_solution)
    
    for desk in range(0, len(viable_solution)):
        for test in range(1, len(tests)):
            alt_soluction = viable_solution.copy()
            if(test != viable_solution[desk]):
                alt_soluction[desk] = test
                alt_objetive = objetive_function(alt_soluction)
                if(alt_objetive < final_objetive):
                    final_soluction = alt_soluction
                    final_objetive = alt_objetive

    return final_soluction, final_objetive

switcher = {
    0: first_improvement,
    1: best_improvement
}

description = {
    0: 'first_improvement',
    1: 'best_improvement'
}

def local_search(s0, strategy):
    empty = config.empty
    s = s0
    s_value = objetive_function(s)
    current_value = 0
    strategy_function = switcher.get(strategy)
    print(description.get(strategy))

    while True:
        s_, current_value = strategy_function(s)

        if current_value < s_value:
            s = s_
            s_value = current_value
        else:
            break

    s, s_value = corrent_solution_size(s, empty)
    return s, s_value


if __name__ == '__main__':
    file_name = sys.argv[1]
    algorith = int(sys.argv[2])
    distance, similarity, desks, tests, empty = read_instance(file_name)

    desk_count = len(desks)
    test_count = len(tests)

    viable_solution = viable_solution(desk_count, desk_count, test_count)
    objetive = objetive_function(viable_solution)

    response_solution, objetive = local_search(viable_solution, algorith)

    print(response_solution)
    print(objetive)
