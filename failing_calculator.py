def average_ratios(numbers):
    """Calculate average of ratio values (100 / each number)."""
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    
    # Check for zero values before division
    zero_values = [num for num in numbers if num == 0]
    if zero_values:
        raise ValueError(f"Cannot calculate ratios with zero values: {zero_values}")
    
    total = 0
    for i in range(len(numbers)):
        total += 100 / numbers[i] 
    return total / len(numbers)


if __name__ == "__main__":
    # Test with valid input
    try:
        result = average_ratios([10, 5, 2])
        print(f"average_ratios([10, 5, 2]) = {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Test with zero value (will raise error)
    try:
        result = average_ratios([10, 5, 0])
        print(f"average_ratios([10, 5, 0]) = {result:.2f}")
    except ValueError as e:
        print(f"Error with [10, 5, 0]: {e}")
