fibonacci_series = lambda n: [0, 1] + [fibonacci_series(i)[-1] + fibonacci_series(i)[-2] for i in range(2, n)]

n = int(input("Enter the limit : "))
print(fibonacci_series(n))