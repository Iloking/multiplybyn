def multiply_one_iteration(N, M):
    """Multiplies N by M using a single iteration."""
    result = 0
    for _ in range(M):
        result += N
    return result

def multiply_n_iterations(N, M):
    """Multiplies N by M using nested iterations."""
    result = 0
    for _ in range(N):
        temp_sum = 0
        for _ in range(M):
            temp_sum += 1  # This adds 1, M times
        result += temp_sum  # Adds M to result for N iterations
    return result

# Taking user input for N and M
try:
    N = int(input("Enter the value of N: "))
    M = int(input("Enter the value of M: "))
    
    # Calling the functions and printing the results
    result_one_iteration = multiply_one_iteration(N, M)
    result_n_iterations = multiply_n_iterations(N, M)
    
    print(f"Result using 1 iteration: {result_one_iteration}")
    print(f"Result using N iterations: {result_n_iterations}")

except ValueError:
    print("Please enter valid integers for N and M.")
