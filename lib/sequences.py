#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print(fib_sequence)
    else:
        for i in range(2, length):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        print(fib_sequence)