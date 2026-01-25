from dataclasses import dataclass
from typing import Tuple

@dataclass
class Data:
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int
    g: int

def process_data(data: Data) -> int:
    """Process data with improved complexity."""
    
    if data.a > 0 and data.b > 0 and data.c > 0 and data.d > 0 and data.e > 0:
        result = 0
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
        result += data.f + data.g
    else:
        result = -sum(data.a, data.b, data.c, data.d, data.e)
    
    # Safe alternative to eval
    data_result = 1 + 1
    
    return result + data_result