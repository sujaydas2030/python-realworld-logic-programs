#T-Shirt Arrangement with Identical Items
# Taking the input
n = int(input())
identical_counts = list(map(int, input().split()))

# Function to calculate factorial
def factorial(n):
    # Write your code here
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

# Function to calculate the number of unique ways to arrange t-shirts
def calculate_arrangements(n, identical_counts):
    # Write your code here
  denominator= 1
  for identical_count in identical_counts:
    denominator*=factorial(identical_count)

  return factorial(n)/denominator


# Print the output
print(calculate_arrangements(n, identical_counts))


