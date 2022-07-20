import sys
from utils import read_instance, viable_solution, objetive_function

file_name = sys.argv[1]
distance, similarity, desks, tests, empty = read_instance(file_name)

print('len(desks)', len(desks))
print('empty', empty)
print('len(tests)', len(tests))

# response_solution = viable_solution(len(desks), len(desks) - empty, len(tests))
response_solution = [2, 0, 1, 2, 3, 0, 0, 2, 3, 3, 0, 3, 0, 3, 2, 3, 3, 2, 1, 0, 1, 3, 3, 3, 2, 0, 2, 3, 3, 2, 3, 3, 3, 3, 0, 3, 3, 3, 3, 2, 0, 0, 2, 3, 3, 2, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3]
objetive = objetive_function(response_solution)


# print(distance)
# print(response_solution)
# print(objetive)