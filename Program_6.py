fibonacci_series = lambda n: [0, 1] if n == 1 else [0, 1] + [fibonacci_series(i)[-1] + fibonacci_series(i)[-2] for i in range(2, n) if fibonacci_series(i)[-1] < n and fibonacci_series(i)[-1] + fibonacci_series(i)[-2] <= n]
n = int(input("Enter the value for n : "))
fib_series = fibonacci_series(n)
while fib_series[-1] == fib_series[-2]:
    fib_series.pop()
print("Fibonacci Series upto "+str(n))
print(fib_series)
