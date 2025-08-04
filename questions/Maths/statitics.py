import statistics

def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    sorted_numbers = sorted(numbers)  
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    try:
        return statistics.mode(numbers)
    except statistics.StatisticsError:
        return "No unique mode"

def std_dev(numbers):
    return statistics.stdev(numbers)

user_data = input("Enter numbers separated by spaces: ").strip()

try:
    numbers = list(map(float, user_data.split()))
except ValueError:
    print("Invalid input. Please enter numeric values only.")
    exit()

if not numbers:
    print("No numbers entered. Please try again.")
    exit()

mean = mean(numbers)
median = median(numbers)
mode = mode(numbers)
std_dev = std_dev(numbers)

print(f"\nResults:")
print(f"Mean = {mean}")
print(f"Median = {median}")
print(f"Mode = {mode}")
print(f"Standard Deviation = {std_dev}")
