def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def calculate_sum(sequence):
    return sum(sequence)

def main():
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    
    if num_terms <= 0:
        print("Number of terms must be greater than 0.")
    else:
        fibonacci_sequence = generate_fibonacci(num_terms)
        sum_of_sequence = calculate_sum(fibonacci_sequence)
        
        print("Generated Fibonacci Sequence:")
        print(fibonacci_sequence)
        print("Sum of the Sequence:", sum_of_sequence)

if __name__ == "__main__":
    main()
