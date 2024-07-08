result = "Honey" + "Boo" * 3
print(result)  # Hasilnya adalah "HoneyBooBooBoo"


capitals = {}
capitals['Murica'] = 'Warshington'
capitals['Germany'] = 'Bonn'
capitals['France'] = 'Paris'
capitals['Engalnd'] = 'London'
capitals['Germany'] = 'Berlin'


result = capitals['Germany']
print(result)  # Hasilnya adalah "Berlin"


a = "23"
b = 9
try:
    result = a + b
except TypeError as e:
    result = str(e)
print(result)  # Hasilnya adalah "can only concatenate str (not 'int') to str"


letters = ["a", "b", "o", "c", "p"]

# a. letters[1]
result_a = letters[1]
print("a:", result_a)  # Hasilnya adalah "b"

# b. letters[len(letters) - 2]
result_b = letters[len(letters) - 2]
print("b:", result_b)  # Hasilnya adalah "c"

# c. letters + ["x"]
result_c = letters + ["x"]
print("c:", result_c)  # Hasilnya adalah ["a", "b", "o", "c", "p", "x"]

# d. letters
result_d = letters
print("d:", result_d)  # Hasilnya adalah ["a", "b", "o", "c", "p"]

result = ' '.join('h a n d s'.split())
print(result)  # Hasilnya adalah "hands"

import json

json_string = '[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]'
result = json.loads(json_string)[1][2]
print(result)  # Hasilnya adalah "f"


def pembagi_indeks1(nums, divisor):
    for i in range(len(nums)):
        if nums[i] % divisor == 0:
            return i
    return -1

vals = [101, 4, 12, 24]
result = pembagi_indeks1(vals, 2)
print(result)  # Hasilnya adalah 1

def mystery(n, m):
    p = 0
    e = 0
    while e < n:
        p = n
        e += 1
    return p

result = mystery(4, 3)
print(result)  # Hasilnya adalah 4
