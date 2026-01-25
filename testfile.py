from typing import Tuple

def process_data(a: int, b: int, c: int, d: int, e: int, f: int, g: int) -> int:
    """Process data with improved complexity."""
    result = 0
    
    # Simplified condition checking
    def check_positive(n: int) -> bool:
        return n > 0

    def nested_logic(a: int, b: int, c: int, d: int, e: int) -> Tuple[int, int]:
        if check_positive(a) and check_positive(b) and check_positive(c) and check_positive(d):
            if check_positive(e):
                # Reduced nesting level 5
                for i in range(10):
                    for j in range(10):
                        if i == j:
                            result += 1
                        elif i > j:
                            result += 2
                        else:
                            result += 3
            else:
                result = -1
        return result, 0  # Removed unused variable k

    result, _ = nested_logic(a, b, c, d, e)
    
    # Safe alternatives to eval
    data = 1 + 1
    
    return result + f + g