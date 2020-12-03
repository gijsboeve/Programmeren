n = 25
threshold = 1e-7
approximation = n/25

while True:
    better = (approximation + (n / approximation)) / 2
    print("approximation:", better)
    if abs(approximation - better) < threshold:
        print("Best:", better)
        break
    approximation = better

n = 6

triangle = 0
for height in range (1, n + 1):
    triangle += height
    print(height, "/t/t", triangle)

candidate = 17
for divisor in range(2, candidate // 2):
    if candidate % divisor == 0:
        print(divisor, "is a divisor of", candidate, "therefore it is not a prime")
        break
else:
    print("No divisor found for", candidate, "therefore it is a prime")
    print(True)