MAX = 100

def calculate_sum(arr):
    return sum(arr)  # Usar la función integrada sum()

def get_valid_input(prompt, validation_fn):
    while True:
        try:
            value = int(input(prompt))
            if validation_fn(value):
                return value
            print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_number_of_elements():
    return get_valid_input(
        "Enter the number of elements (1-100): ",
        lambda x: 1 <= x <= MAX
    )

def get_elements(n):
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        arr.append(get_valid_input("Enter an integer: ", lambda x: True))
    return arr

def main():
    try:
        n = get_number_of_elements()
        arr = get_elements(n)
        print("Sum of the numbers:", calculate_sum(arr))  # Llamar directamente a calculate_sum()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)

if __name__ == "__main__":
    main()
