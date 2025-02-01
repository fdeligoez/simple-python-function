# Simple Python Function

This repository contains a simple Python function that calculates the average of a list of numbers.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from simple_function.calculator import calculate_average

numbers = [1, 2, 3, 4, 5]
result = calculate_average(numbers)
print(f"The average is: {result}")
```

## Testing

To run the tests:

```bash
python -m pytest tests/
```

## Features

- Calculates average of numeric lists
- Handles both integers and floats
- Input validation
- Comprehensive test coverage

## Error Handling

- Raises ValueError for empty lists
- Raises TypeError for non-numeric values
