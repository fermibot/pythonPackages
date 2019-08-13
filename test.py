from functions.tutorials.gus.mathematical_functions import Fibonacci, Tribonacci

if __name__ == '__main__':
    for i in range(1, 21):
        print(f"{i}th Fibonacci = {Fibonacci(i)} and {i}th Tribonacci = {Tribonacci(i)}")
