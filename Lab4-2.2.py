import random

# Define the DES initial permutation table (PC-1) and subkey permutation table (PC-2)
PC1 = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Define the key rotation schedule for each round
KEY_ROTATION_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def generate_random_key():
    # Generate a random 64-bit key (K+)
    return ''.join(str(random.randint(0, 1)) for _ in range(64))


def apply_initial_permutation(key):
    # Apply the initial permutation (PC-1) to the key
    return ''.join(key[i - 1] for i in PC1)


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

    # Apply the initial permutation (PC-1)
    K_plus = apply_initial_permutation(K_plus)

    print("\nKey after applying initial permutation (PC-1):")
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
