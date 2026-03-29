"""Data processing module with clean code principles."""

from typing import List
import logging

# Configuration constants
PRICE_MULTIPLIER = 1.15
LOG_FILE_PATH = "log.txt"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(message)s'
)


def apply_price_multiplier(base_price: float) -> float:
    """
    Apply a percentage increase to a base price.
    
    Args:
        base_price: The original price value
        
    Returns:
        The price after applying the multiplier
    """
    return base_price * PRICE_MULTIPLIER


def calculate_total_prices(prices: List[float]) -> List[float]:
    """
    Calculate adjusted prices for a list of base prices.
    
    Args:
        prices: List of base prices to adjust
        
    Returns:
        List of adjusted prices
        
    Raises:
        ValueError: If prices list is empty
        TypeError: If prices contain non-numeric values
    """
    if not prices:
        raise ValueError("Prices list cannot be empty")
    
    return [apply_price_multiplier(price) for price in prices]


def log_prices(adjusted_prices: List[float]) -> None:
    """
    Log the processing results to file.
    
    Args:
        adjusted_prices: List of calculated prices to log
    """
    logging.info(f"Processed prices: {adjusted_prices}")


def display_prices(adjusted_prices: List[float]) -> None:
    """
    Display formatted prices to console.
    
    Args:
        adjusted_prices: List of prices to display
    """
    for price in adjusted_prices:
        formatted_output = f"Total: {price:.2f}"
        print(formatted_output)


def process_data(prices: List[float]) -> List[float]:
    """
    Process a list of prices with logging and display.
    
    This is the main orchestration function that:
    - Applies price multiplier to each price
    - Displays results to console
    - Logs results to file
    
    Args:
        prices: List of base prices to process
        
    Returns:
        List of adjusted prices
    """
    adjusted_prices = calculate_total_prices(prices)
    display_prices(adjusted_prices)
    log_prices(adjusted_prices)
    
    return adjusted_prices
