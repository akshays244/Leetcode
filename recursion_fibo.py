def fibonacci_sequence(n, current=0):
    # Base case: Stop recursion when current reaches n
    if current == n:
        return

    # Print the Fibonacci number for the current index
    print(fibonacci(current), end=" ")  # end=" " keeps the numbers on the same line

    # Recursively call the function to print the next Fibonacci number
    fibonacci_sequence(n, current + 1)


# Helper function to calculate the Fibonacci number at a given index
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# Call the function to print the Fibonacci sequence for n=5
fibonacci_sequence(20)