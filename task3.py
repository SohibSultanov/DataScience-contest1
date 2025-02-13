
import time

def decorator_1(func):
    """Decorator to measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.name} call executed in {execution_time:.4f} sec")
        return result

    return wrapper

# Example usage:
if __name__ == "main":
    @decorator_1
    def sample_function():
        time.sleep(1)  # Simulating some computation
        print("Function executed!")

    sample_function()