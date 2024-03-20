
# David: main() and encoded()
def encode(password):
    # creates an empty string
    coded = ""
    # updates each character in the string accordingly
    for char in password:
        check = int(char)
        if check >= 7:
            check = check - 7
        else:
            check += 3
        coded += str(check)
    # returns the resultant string
    return coded

while True:

    # display menu
    print("1. Encode\n2. Decode\n3. Exit")
    print("")

    option = int(input("Please choose an option from the menu: "))

    # utilize the encode function
    if option == 1:
        print(encode(str(input("Please enter an 8 digit password: "))))
        print("")

    # terminate the while loop
    if option == 3:
        break

print("Goodbye!")