def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of numbers (int or float)
        
    Returns:
        float: The average of the numbers
        
    Raises:
        ValueError: If the list is empty
        TypeError: If the list contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
        
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All values must be numeric")
        
    return sum(numbers) / len(numbers)