
def kwargsAcceptFun(**kwargs):
    """Function that accepts an arbitrary number of named arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
if __name__ == "main":
    kwargsAcceptFun(name="Alice", age=25, country="USA")