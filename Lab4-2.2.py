import random

# Define the key rotation schedule for each round
KEY_ROTATION_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def generate_random_key():
    # Generate a random 64-bit key (K+)
    return ''.join(str(random.randint(0, 1)) for _ in range(64))

def calculate_Ci_and_Di(K_plus, round_number):
    # Calculate Ci and Di for the given round number
    C, D = K_plus[:28], K_plus[28:]
    for _ in range(KEY_ROTATION_SCHEDULE[round_number - 1]):
        # Perform a circular left shift on C and D
        C = C[1:] + C[0]
        D = D[1:] + D[0]
    return C, D

def main():
    # Generate a random 64-bit key (K+)
    K_plus = generate_random_key()

    print("Randomly generated 64-bit key (K+):")
    print(K_plus)

    round_number = int(input("\nEnter the round number (1 to 16) to calculate Ci and Di: "))

    if round_number < 1 or round_number > 16:
        print("Invalid round number. Please enter a number between 1 and 16.")
    else:
        # Calculate Ci and Di for the specified round
        C, D = calculate_Ci_and_Di(K_plus, round_number)

        print(f"\nCi for round {round_number}:")
        print(C)

        print(f"\nDi for round {round_number}:")
        print(D)

if __name__ == "__main__":
    main()
