
def generate_fibonacci(n):
    
    fibonacci_sequence = [0, 1] 
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def main():
    try:
        n_terms = int(input("How many terms? "))
        if n_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_terms = generate_fibonacci(n_terms)
            print("Fibonacci sequence:")
            for term in fibonacci_terms:
                print(term, end=" ")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
