def binary_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        # If the current bit is 1, multiply the result by the current base
        if exponent & 1:
            result *= base
        # Square the base
        base *= base
        # Move to the next bit
        exponent >>= 1
    return result

# Example usage
print(binary_exponentiation(3, 13))  # Output: 1594323