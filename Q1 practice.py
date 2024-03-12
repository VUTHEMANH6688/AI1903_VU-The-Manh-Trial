def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(sequence):
    primes = [num for num in sequence if is_prime(num)]
    return primes

def main():
    try
        sequence = list(map(int, input("Enter a sequence of positive integers separated by spaces: ").split()))
        if not all(num > 0 for num in sequence):
            print("Please enter only positive integers.")
            return
        primes = get_primes(sequence)
        print("Prime numbers in the sequence:", primes)
        if primes:
            print("The largest prime number in the sequence is:", max(primes))
        else:
            print("There are no prime numbers in the sequence.")
            
    except ValueError:
        print("Invalid input. Please enter only integers.")

if _name_ == "_main_":
    main()