import uuid
import random

# Utility function to generate a unique account ID
def generate_account_id():
    return str(uuid.uuid4())

# Utility function to generate a unique account number
def generate_account_number():
    # Assuming a simple 10-digit account number for demonstration purposes
    return ''.join(str(random.randint(0, 9)) for _ in range(10))