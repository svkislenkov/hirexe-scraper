import random

# Avoid bot detection by varying the time we wait from 2-6 seconds
def get_stall():
    return random.uniform(2, 4)

# Same as above, only now wait longer for page to load
def get_stall_long():
    return random.uniform(5, 8)