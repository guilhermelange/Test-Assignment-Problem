import random
import sys
sys.path.insert(1, '../')
from utils import read_instance, objetive_function, corrent_solution_size
import config

# Heurística Construtiva 01
# Constructive Heuristic 01
# Ramdom para selecionar a carteira que será alterada, e calculado a melhor mesa
def constructive_heuristic_01(correct_size):
    def validade_best_test(solution, idx):
        iteration_value = 100000
        iteration_solution = solution.copy()

        for i in range(1, test_count):
            solution[idx] = i
            current_value = objetive_function(solution)
            if current_value < iteration_value:
                iteration_value = current_value
                iteration_solution = solution.copy()
        return iteration_solution, iteration_value

    desks, tests, empty = config.desks, config.tests, config.empty
    desk_count = len(desks)
    test_count = len(tests)
    s = [0 for _ in range(desk_count)]
    best_value = 0
    desk_with_test = 0

    while desk_with_test < (desk_count):
        sort_list = [i for i in range(desk_count) if s[i] == 0]
        idx = random.choice(sort_list)
        s, best_value = validade_best_test(s, idx)
        desk_with_test += 1

    if correct_size:
        s, best_value = corrent_solution_size(s, empty)
    return s, best_value


if __name__ == '__main__':
    file_name = sys.argv[1]
    read_instance(file_name)

    response_solution, objetive = constructive_heuristic_01(True)
    print()
    print(response_solution)
    print(objetive)

