# Diberikan 3 variabel
p = 11
q = 5
r = 4

# a. ((p - r) == (r + q))
a = ((p - r) == (r + q))
print("a:", a)  # Hasilnya adalah False

# b. (((p % 3) + q) != (r % 2))
b = (((p % 3) + q) != (r % 2))
print("b:", b)  # Hasilnya adalah True

# c. ((q - 3) == (p % 2 + q))
c = ((q - 3) == (p % 2 + q))
print("c:", c)  # Hasilnya adalah False

# d. ((r + q) != ((p * 2) % 2))
d = ((r + q) != ((p * 2) % 2))
print("d:", d)  # Hasilnya adalah True

# e. ((((q % 3) + p) > (r % 2)))
e = ((((q % 3) + p) > (r % 2)))
print("e:", e)  # Hasilnya adalah True

# f. (((r + p) <= (q * 5)))
f = (((r + p) <= (q * 5)))
print("f:", f)  # Hasilnya adalah True
