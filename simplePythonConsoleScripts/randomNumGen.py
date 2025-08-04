import random

def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

if __name__ == "__main__":
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))
    
    if min_value >= max_value:
        print("Minimum value must be less than maximum value.")
    else:
        random_number = generate_random_number(min_value, max_value)
        print(f"Generated random number between {min_value} and {max_value}: {random_number}")

        
        