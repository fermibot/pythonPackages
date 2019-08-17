from functions.tutorials.gus.mathematical_functions import fibonacci, tribonacci

if __name__ == '__main__':
    for i in range(1, 21):
        print(f"{i}th Fibonacci = {fibonacci(i)} and {i}th Tribonacci = {tribonacci(i)}")
