# Test Case 1: Basic output
assert say_hello() == "Hello, world!", "Test Case 1 Failed"

# Test Case 2: Output should be a string
assert isinstance(say_hello(), str), "Test Case 2 Failed"

# Test Case 3: Output should not be empty
assert len(say_hello()) > 0, "Test Case 3 Failed"

# If all tests pass:
print("All test cases passed!")
