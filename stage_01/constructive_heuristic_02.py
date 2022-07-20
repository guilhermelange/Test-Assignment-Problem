import random
import sys
sys.path.insert(1, '../')
from utils import read_instance, objetive_function, corrent_solution_size
import config

# Heurística Construtiva 02
# Constructive Heuristic 02
# Random para selecionar o teste e calculado a melhor mesa para aplicá-lo
def constructive_heuristic_02():
    def validade_best_desk(solution, idx):
        # idx = test number / index
        iteration_value = 100000
        iteration_solution = solution.copy()

        for i in range(0, desk_count):
            current_solution = solution.copy()
            if solution[i] == 0: # Não sobrescrever casos já alocados
                current_solution[i] = idx
                current_value = objetive_function(current_solution)
                if current_value < iteration_value:
                    iteration_value = current_value
                    iteration_solution = current_solution.copy()
        return iteration_solution, iteration_value

    desks, tests, empty = config.desks, config.tests, config.empty
    desk_count = len(desks)
    test_count = len(tests)
    s = [0 for _ in range(desk_count)]
    best_value = 0
    desk_with_test = 0

    while desk_with_test < (desk_count):
        sort_list = [i for i in range(1, test_count)]
        idx = random.choice(sort_list)
        s, best_value = validade_best_desk(s, idx)
        desk_with_test += 1

    s, best_value = corrent_solution_size(s, empty)
    return s, best_value


if __name__ == '__main__':
    file_name = sys.argv[1]
    read_instance(file_name)

    response_solution, objetive = constructive_heuristic_02()
    print()
    print(response_solution)
    print(objetive)

