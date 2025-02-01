import doctest

def add(a, b):
    """
    Returns the sum of two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    >>> add(10, 20)
    30
    """
    return a + b

if __name__ == "__main__":
    print("NAME:- SANKET MAHAPATRA")
    print("REGISTRATION NUMBER:- 2241013017")
    
    doctest.testmod()
    
    print("Explanation: The add() function includes test cases inside its docstring using the doctest format.")
    print("Explanation: The doctest module automatically runs these test cases when the script is executed, ensuring correctness.")
    print("Explanation: If all tests pass, the script runs silently; otherwise, it reports any failed test cases.")
    print("Explanation: Using doctest simplifies testing by embedding test cases directly within function documentation.")