list_A = ['A', 'B', 'C', 'D', 'E']
'''
for i in range(len(list_A)):
    print(f'{i}: {list_A[i]}')

number_1, number_2, number_3 = (4, 5, 6)
print(f'Number 2 is {number_1}')

for index, value in enumerate(list_A):
    print(f'{index + 1}: {value}')

print(tuple(enumerate(list_A)))
'''

cubes = [item**3 for item in range(6)]
print(cubes)

def is_odd(x):
    return x % 2 != 0

print(list(filter(is_odd, cubes)))

