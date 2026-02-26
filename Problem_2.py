# Prime Number Generator # This program generates prime numbers between 1 and a user-specified number.
import math

# use while loop to continuously ask for input until the user decides to quit
while True:
    number = int(input("Enter a last number to do you want to generate like 100: "))
    print("Prime numbers between 1 and", number, "are:")
    if number <= 0:                                    # Check if the number is negative
        print("Please enter a positive number like 10, 100.")
        continue

    # Function to check if a number is prime
    def is_prime(number):
        if number <= 0:
           return False
        for i in range(2, int(math.sqrt(number)) + 1):
           if number % i == 0:
            return False
        return True
    
    # Generate and print prime numbers
    for number in range(1, number + 1):
        if is_prime(number):
            print(number, end=' ')
    break
