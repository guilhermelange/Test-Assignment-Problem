from posixpath import split
import random
import re
import config

def create_matriz(size, default_value):
    matriz = [[] for _ in range(size)]
    for i in range(size):
        matriz[i] = [default_value for _ in range(size)]
    return matriz

def viable_solution(size, selected_count, test_count):
    selected = [random.randint(1, test_count-1) if i < selected_count else 0 for i in range(size)]
    random.shuffle(selected)
    return selected


# new version random walk. Pra cada carteira que for zerar calcular a que melhor.
def correct_solution(current_solution, desk_count, empty):
        for i in random.sample(range(desk_count), empty):
            current_solution[i] = 0
        return current_solution

def correct_solution_v2(current_solution, desk_count, test_count, empty):
    for i in range(len(current_solution)):
        if current_solution[i] == 0:
            current_solution[i] = random.randint(1, test_count-1)

    for i in random.sample(range(desk_count), empty):
        current_solution[i] = 0
    return current_solution

def generate_random_neighbor(solution):
    tests = config.tests
    test_count = len(tests)

    list_desks = range(len(solution))
    i = random.choice(list_desks)
    opt = solution[i]

    tests_numbers = list(range(1, test_count))
    if opt > 0: tests_numbers.remove(opt) 
    solution[i] = random.choice(tests_numbers)

    if opt <= 0:
        options = [j for j in range(len(solution)) if solution[j] > 0]
        i = random.choice(options)
        solution[i] = 0

    return solution



# new
def random_neighbor(solution):
    desk_count = len(config.desks)
    test_count = len(config.tests)

    # Random Desk to change
    idx = random.randint(0, desk_count-1)
        
    # Random Test to change, different from previous. And update
    tests_numbers = list(range(1, test_count))
    tests_numbers.remove(solution[idx])
    solution[idx] = random.choice(tests_numbers)

    return solution

# new
def corrent_solution_size(solution, empty):
    count = 0
    best_solution = solution.copy()
    best_value = objetive_function(best_solution)
    while count < empty:
        # For each Desk on Solution
        iteration_best_solution = best_solution.copy()
        iteration_best_value = objetive_function(iteration_best_solution)

        for i in range(len(solution)):
            if best_solution[i] > 0:
                iteration_solution = best_solution.copy()
                iteration_solution[i] = 0
                iteration_value = objetive_function(iteration_solution)

                if iteration_value < iteration_best_value:
                    iteration_best_value = iteration_value
                    iteration_best_solution = iteration_solution
        
        best_solution = iteration_best_solution
        best_value = iteration_best_value
        count += 1

    return best_solution, best_value

def objetive_function(solution):
    distance = config.distance
    similarity = config.similarity
    size = len(distance)

    objective_sum = 0.0
    for d in range(size):
        for e in range(d, size):
            if distance[d][e] > 0:
                test1 = solution[d]
                test2 = solution[e]
                aux = 0
                
                if test2 < test1:
                    aux = test1
                    test1 = test2
                    test2 = aux

                objective_sum += distance[d][e] * similarity[test1][test2]

    return objective_sum

def correct_string(line):
    line = re.sub("\t", " ", line)
    line = re.sub(r"\s+", " ", line)
    return line

def read_instance(file_name):
    # Open File
    print('Start instance reading')
    file = open(file_name, 'r')
    lines = file.readlines()
    lines = map(lambda l: l.rstrip('\n'), lines)
    fields = next(lines)
    fields = correct_string(fields)
    fields = fields.split(' ')
    
    # Header
    desk_count = int(fields[0])
    desk_empty_count = int(fields[3])
    edge_count = int(fields[1])
    test_count = int(fields[2])
    desks = []
    tests = [str(i) for i in range(0, test_count)]
    desk_distance = create_matriz(desk_count, 0)
    tests_similarity = create_matriz(test_count, 0)

    # Read
    for _ in range(0, desk_count):
        desks.append(int(next(lines)))

    for _ in range(0, edge_count):
        line = correct_string(next(lines)).split(' ')
        x, y, distance = line[0], line[1], float(line[2])

        x_index, y_index = desks.index(int(x)), desks.index(int(y))
        desk_distance[x_index][y_index] = distance

    for line in lines:
        line = correct_string(line).split(' ')
        x, y, similarity = int(line[0]), int(line[1]), float(line[2])
        tests_similarity[x][y] = similarity


    print('End instance reading')
    config.update_instance(desk_distance, tests_similarity, desks, tests, desk_empty_count)
    return desk_distance, tests_similarity, desks, tests, desk_empty_count