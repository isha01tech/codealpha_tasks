
def fibonacci_generator(n):
    """
    Generate the Fibonacci series up to the nth number.

    :param n: The number of terms in the Fibonacci sequence to generate.
    :return: A list containing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Initialize the first two terms
    fib_series = [0, 1]

    # Generate the rest of the series
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series


# Input from the user
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

# Generate and print the Fibonacci series
print(f"Fibonacci series up to {num_terms} terms: {fibonacci_generator(num_terms)}")