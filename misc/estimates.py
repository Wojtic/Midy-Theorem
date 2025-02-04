from math import sqrt

m = 2
beta = (m + sqrt(m**2 + 4))/2
N = 2

print("Sudé cifry: ")
sumation = 0
for i in range(N):
    c = m if i % 2 == 0 else 0
    sumation += c*(-1/beta)**i

print(abs(sumation))
print("Horní odhad: ", beta - 1/beta**(N))

print("Liché cifry: ")
sumation = 0
for i in range(N):
    c = 0 if i % 2 == 0 else m
    sumation += c*(-1/beta)**i

print(abs(sumation))
print("Horní odhad: ", 1 - 1/beta**(N))
