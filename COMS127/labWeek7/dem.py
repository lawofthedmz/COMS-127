def take_input():
    numbers = []
    while True:
        user_input = input("Enter an integer (or * to finish): ")
        if user_input == '*':
            break
        if user_input.isdigit():  # Check if the input consists of digits
            numbers.append(user_input)
        else:
            print("Invalid input. Please enter a valid integer.")
    return numbers

def convert_to_integers(numbers):
    return [int(num) for num in numbers]

def findMin(numbers):
    if not numbers:
        return None
    min_num = int(numbers[0])
    for num in numbers:
        if int(num) < min_num:
            min_num = int(num)
    return min_num

def main():
    input_numbers = take_input()
    converted_numbers = convert_to_integers(input_numbers)
    
    if not converted_numbers:
        print("No numbers were entered.")
    else:
        print("Entered numbers:", converted_numbers)
        min_num = findMin(converted_numbers)
        print("Minimum number:", min_num)

if __name__ == "__main__":
    main()