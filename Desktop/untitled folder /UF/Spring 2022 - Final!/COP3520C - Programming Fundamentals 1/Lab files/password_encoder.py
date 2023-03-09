# Sophia John - COP3502C - Spring 2023
# Lab 6: Software Engineering
# Create a password encoder and decoder

def encode(password):
    #Encodes the given password by adding 3 to each digit
    encoded_password = ""
    for digit in password:
        encoded_password += str(int(digit) + 3)
    return encoded_password


def decode(encoded_password):
    #Decodes the given password by subtracting 3 from each digit
    decoded_password = ""
    for digit in encoded_password:
        decoded_password += str(int(digit) - 3)
    return decoded_password


def main():
    #Main function that displays the menu and handles user input
    option = 0
    password = ""
    encoded_password = ""

    while option != 3:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            if not encoded_password:
                print("You haven't encoded a password yet!")
            else:
                print("The encoded password is", encoded_password, "and the original password is", decode(encoded_password))
        elif option == 3:
            print("Goodbye!")
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()


