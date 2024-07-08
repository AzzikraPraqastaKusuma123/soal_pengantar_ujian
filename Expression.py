# a. 15 mod 5
a = 15 % 5
print("a:", a)  # Hasilnya adalah 0

# b. 12 + 3 * 5 == 75
b = 12 + 3 * 5 == 75
print("b:", b)  # Hasilnya adalah False

# c. "PML" + "15523"
c = "PML" + "15523"
print("c:", c)  # Hasilnya adalah "PML15523"

# d. "100" + 234
try:
    d = "100" + 234
except TypeError as e:
    d = str(e)
print("d:", d)  # Hasilnya adalah TypeError: can only concatenate str (not "int") to str

# e. ((11 % 3) + 2) != 8 / 2
e = ((11 % 3) + 2) != 8 / 2
print("e:", e)  # Hasilnya adalah True
