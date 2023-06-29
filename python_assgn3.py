def generate_fibonacci(limit):
    fib_numbers = [0, 1]
#Initialize the list with the first two Fibonacci numbers

    while fib_numbers[-1] + fib_numbers[-2] <= limit:
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)

    return fib_numbers


#Get the limit from the user
limit = int(input("Enter the limit for Fibonacci numbers: "))

# Generate and print Fibonacci numbers up to the specified limit
fibonacci_numbers = generate_fibonacci(limit)
print("Fibonacci numbers up to", limit, ":")
print(fibonacci_numbers)
