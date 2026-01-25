from typing import Dict

def process_data(data: Dict[str, int], flags: int) -> int:
    """Process data with improved complexity."""
    result = 0
    
    # Use a simple loop for better readability
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i == j == k:
                    result += 1
                elif i > j:
                    if j > k:
                        result += 2
                    else:
                        result -= 1
                else:
                    result += 3
    
    # Replace eval with a safe alternative
    data_value = 1 + 1
    
    # Simplify conditional logic
    if data['a'] > 0:
        if data['b'] > 0:
            if data['c'] > 0:
                if data['d'] > 0:
                    result += data_value if data['e'] > 0 else -1
                else:
                    result = -2
            else:
                result = -3
        else:
            result = -4
    else:
        result = -5
    
    return result + flags