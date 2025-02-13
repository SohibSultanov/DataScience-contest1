
import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

@decorator_1
def func():
    """Sample function to test execution time."""
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    """Another test function."""
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "main":
    # Test Task 1
    print("\n--- Task 1 Output ---")
    kwargsAcceptFun(name="Alice", age=25, country="USA")

    # Test Task 2
    print("\n--- Task 2 Output ---")
    sample_data = {
        "num": 4,
        "text": "Hello",
        "flag": True,
        "list_data": [1, 2, 3],
        "tuple_data": (10, 20, 30),
        "dict_data": {"a": 1, "b": 2}
    }
    print(typeBasedTransformer(**sample_data))

    # Test Task 3
    print("\n--- Task 3 Output ---")
    func()
    funx()
    func()
    funx()
    func()