import sys
sys.path.insert(1, '../')
from utils import objetive_function, read_instance, viable_solution
import config

# Busca Local Simples Primeira Melhora
# Simple Local Search first improvement
def first_improvement(viable_solution):
    tests = config.tests
    current_solution = viable_solution
    final_objetive = objetive_function(viable_solution)

    for desk in current_solution:
        alt_soluction = current_solution
        for test in tests:
            if(int(test) != current_solution[desk] and int(test) != 0):
                alt_soluction[desk] = int(test)      
            alt_objetive = objetive_function(alt_soluction)
            if(alt_objetive > final_objetive):
                return alt_soluction, alt_objetive
    return current_solution, final_objetive

# Busca Local Simples Melhor Melhora
# Simple Local Search best improvement
def best_improvement(viable_solution):
    tests = config.tests
    final_soluction = viable_solution
    final_objetive = objetive_function(viable_solution)
    for desk in viable_solution:
        alt_soluction = viable_solution
        for test in tests:
            if(int(test) != viable_solution[desk] and int(test) != 0):
                alt_soluction[desk] = int(test)      
            alt_objetive = objetive_function(alt_soluction)
            if(alt_objetive > final_objetive and alt_objetive):
                final_soluction = alt_soluction
                final_objetive = alt_objetive

    #GLL DEIXAR? #if(final_objetive > objetive):
    return final_soluction, final_objetive

if __name__ == '__main__':
    file_name = sys.argv[1]
    algorith = int(sys.argv[2])
    distance, similarity, desks, tests, empty = read_instance(file_name)

    desk_count = len(desks)
    test_count = len(tests)

    viable_solution = viable_solution(desk_count, desk_count - empty, test_count)
    objetive = objetive_function(viable_solution)

    #if(final_objetive > objetive):

    response_solution, objetive = [], 0
    if algorith >= 1:
        print('First')
        response_solution, objetive = first_improvement(viable_solution)
    else:
        print('Best')
        response_solution, objetive = best_improvement(viable_solution)
    
    print()
    print(response_solution)
    print(objetive)