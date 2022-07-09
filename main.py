import sys

file_name = sys.argv[1]
timeout = sys.argv[2]

def create_matriz(size, default_value):
    matriz = [[] for _ in range(size)]
    for i in range(size):
        matriz[i] = [default_value for _ in range(size)]
    return matriz

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
    selected = create_matriz(test_count, 0)

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
    return desk_distance, tests_similarity, selected, desks, tests, desk_empty_count


desk_distance, tests_similarity, selected, desks, tests, desk_empty_count = read_instance(file_name)

print(desk_distance)
print('desk_distance')
print(tests_similarity)
print('tests_similarity')
print(selected)
print('selected')
# objective_sum = 0.0
# for i in range(len(desk_distance)):
#     for j in range(i, len(desk_distance[i])):
#         if desk_distance[i][j] > 0:
#             objective_sum += desk_distance[i][j]