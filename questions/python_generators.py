# Source: Akuna
# Question: Implement and explain lazy Python generators.
#

def count_up_to(n):
    count = 1

    while count <= n:
        yield count  # Pauses execution and returns the current count
        count += 1  # Resumes from here in the next call

# Using the generator
counter = count_up_to(3)

# Fetching values manually using next()
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
print(next(counter))  # Raises StopIteration


# Real-World Use Cases
# 1. Processing large files without loading them into memory

# def parse_log_file(path):
#     with open(path) as f:
#         for line in f:
#             if "ERROR" in line:
#                 yield line

# for error_line in parse_log_file("/var/log/app.log"):
#     print(error_line)
# # Reads one line at a time — works on a 100GB log file

# 2. Infinite sequences (impossible with lists)

# def fibonacci():
#     a, b = 0, 1
#     while True:         # runs forever — no problem, values are lazy
#         yield a
#         a, b = b, a + b