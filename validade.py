import sys
from utils import read_instance, viable_solution, objetive_function

file_name = sys.argv[1]
distance, similarity, desks, tests, empty = read_instance(file_name)

print('len(desks)', len(desks))
print('empty', empty)
print('len(tests)', len(tests))

# response_solution = viable_solution(len(desks), len(desks) - empty, len(tests))
response_solution = [1, 0, 2, 0, 2, 0, 0, 3, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 2]
objetive = objetive_function(response_solution)


print(response_solution)
print(objetive)