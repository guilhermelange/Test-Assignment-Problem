from main import read_instance, objetive_function
import random
import sys

file_name = sys.argv[1]

distance, similarity, desks, tests, empty = read_instance(file_name)
desk_count = len(desks)
test_count = len(tests)

s = [0 for _ in range(desk_count)]
best_value = 0
desk_with_test = 0

def validade_best(solution, idx):
    iteration_value = 100000
    iteration_solution = solution.copy()

    for i in range(1, test_count):
        solution[idx] = i
        current_value = objetive_function(distance, similarity, solution)
        if current_value < iteration_value:
            iteration_value = current_value
            iteration_solution = solution.copy()
    return iteration_solution, iteration_value


while desk_with_test < (desk_count - empty):
    sort_list = [i for i in range(desk_count) if s[i] == 0]
    idx = random.choice(sort_list)
    s, best_value = validade_best(s, idx)
    desk_with_test += 1

print(s)
print(best_value)