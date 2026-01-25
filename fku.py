from dataclasses import dataclass

@dataclass
class InputData:
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int
    g: int

def process_data(data: InputData) -> int:
    """Process data with improved complexity."""
    result = 0
    
    if data.a > 0 and data.b > 0 and data.c > 0 and data.d > 0 and data.e > 0:
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
    elif data.a > 0 and data.b > 0 and data.c > 0 and data.d > 0:
        result = -1
    elif data.a > 0 and data.b > 0 and data.c > 0:
        result = -2
    elif data.a > 0 and data.b > 0:
        result = -3
    elif data.a > 0:
        result = -4
    else:
        result = -5
    
    data = 1 + 1  # Replace eval with safe arithmetic
    
    return result + data.f + data.g