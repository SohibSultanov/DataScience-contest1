
def typeBasedTransformer(**kwargs):
    """Transforms values based on their types."""
    transformed_data = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  # Square numbers
            transformed_data[key] = value ** 2
        elif isinstance(value, str):  # Reverse strings
            transformed_data[key] = value[::-1]
        elif isinstance(value, bool):  # Invert booleans
            transformed_data[key] = not value
        elif isinstance(value, (list, tuple)):  # Reverse lists/tuples
            transformed_data[key] = value[::-1]
        elif isinstance(value, dict):  # Swap keys and values in dictionaries
            if len(set(value.values())) == len(value.values()):  # Ensure unique values
                transformed_data[key] = {v: k for k, v in value.items()}
            else:
                transformed_data[key] = value  # Leave unchanged if values are not unique
        else:
            transformed_data[key] = value  # Leave unsupported types unchanged

    return transformed_data

# Example usage:
if __name__ == "main":
    sample_data = {
        "num": 4,
        "text": "Hello",
        "flag": True,
        "list_data": [1, 2, 3],
        "tuple_data": (10, 20, 30),
        "dict_data": {"a": 1, "b": 2}
    }
    print(typeBasedTransformer(**sample_data))