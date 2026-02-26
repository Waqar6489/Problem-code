# List Analysis

def list_analysis(numbers):

    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)

    # numbers above average
    above_average = []
    for num in numbers:
        if num > average:
            above_average.append(num)

    return maximum, minimum, average, above_average


# Input Validation
while True:
    user_input = input("Enter numbers separated by space: ").strip()  # Remove leading and trailing whitespace

    if user_input == "":
        print("Please enter numbers, not empty input.")
        continue

    try:
        nums = list(map(int, user_input.split()))
        break
    except ValueError:
        print("Please enter only numbers.")

# Function call
max_val, min_val, avg_val, above_avg = list_analysis(nums)

print("Maximum value:", max_val)
print("Minimum value:", min_val)
print("Average value:", avg_val)
print("Numbers above average:", above_avg)
