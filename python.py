def fib_iterative(n):
    """Calculate Fibonacci number using an iterative approach."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n):
    """Calculate Fibonacci number using a simple recursive approach."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_memo(n, memo=None):
    """Calculate Fibonacci number using recursion with memoization."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def approximate_golden_ratio(n):
    """Approximate the golden ratio using Fibonacci numbers.
    
    It calculates fib(n+1) / fib(n) using the iterative Fibonacci function.
    n must be greater than 0.
    """
    if n <= 0:
        raise ValueError("n must be greater than 0 for golden ratio approximation")
    fib_n = fib_iterative(n)
    if fib_n == 0:
        raise ValueError("The Fibonacci number at position n is zero, cannot compute ratio")
    fib_next = fib_iterative(n + 1)
    return fib_next / fib_n

if __name__ == "__main__":
    test_values = [0, 1, 2, 5, 10, 15, 20, 25, 30]

    print("Testing Fibonacci implementations:\n")
    for n in test_values:
        print(f"fib_iterative({n}) = {fib_iterative(n)}")
        print(f"fib_recursive({n}) = {fib_recursive(n)}")
        print(f"fib_memo({n}) = {fib_memo(n)}")
        if n > 0:
            golden = approximate_golden_ratio(n)
            print(f"approximate_golden_ratio({n}) = {golden}")
        print("-" * 40)