import random

def create_matriz(size, default_value):
    matriz = [[] for _ in range(size)]
    for i in range(size):
        matriz[i] = [default_value for _ in range(size)]
    return matriz

def viable_solution(size, selected_count, test_count):
    selected = [random.randint(1, test_count-1) if i < selected_count else 0 for i in range(size)]
    random.shuffle(selected)
    return selected

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

def objetive_function(distance, similarity, solution):
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

def read_instance(file_name):
    # Open File
    print('Start instance reading')
    file = open(file_name, 'r')
    lines = file.readlines()
    lines = map(lambda l: l.rstrip('\n'), lines)
    fields = next(lines).split('\t')
    
    # Header
    desk_count = int(fields[0])
    desk_empty_count = int(fields[3])
    edge_count = int(fields[2].split('  ')[0])
    test_count = int(fields[2].split('  ')[1])
    desks = []
    tests = [str(i) for i in range(0, test_count)]
    desk_distance = create_matriz(desk_count, 0)
    tests_similarity = create_matriz(test_count, 0)

    # Read
    for _ in range(0, desk_count):
        desks.append(int(next(lines)))

    for _ in range(0, edge_count):
        line = next(lines).split(' ')
        x, y, distance = line[0], line[1], float(line[2])

        x_index, y_index = desks.index(int(x)), desks.index(int(y))
        desk_distance[x_index][y_index] = distance

    for line in lines:
        line = line.split('  ')
        x, y, similarity = int(line[0]), int(line[1]), float(line[2])
        tests_similarity[x][y] = similarity


    print('End instance reading')
    return desk_distance, tests_similarity, desks, tests, desk_empty_count