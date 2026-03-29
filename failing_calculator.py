"""Calculator module for ratio calculations."""

from typing import List


def average_ratios(numbers: List[float]) -> float:
    """
    Calculate the average of ratio values (100 divided by each number).
    
    Args:
        numbers: List of non-zero numeric values
        
    Returns:
        The average of all ratio calculations
        
    Raises:
        ValueError: If list is empty or contains zero values
        TypeError: If list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    
    # Check for zero values before division
    zero_values = [num for num in numbers if num == 0]
    if zero_values:
        raise ValueError(f"Cannot calculate ratios with zero values: {zero_values}")
    
    try:
        ratios = [100 / num for num in numbers]
    except TypeError:
        raise TypeError("All values must be numeric")
    
    return sum(ratios) / len(ratios)
