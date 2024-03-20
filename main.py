
def encode(password):
    coded = ""
    for char in password:
        check = int(char)
        if check >= 7:
            check = check - 7
        else:
            check += 3
        coded += str(check)

    return coded

while True:
    print("1. Encode\n2. Decode\n3. Exit")
    print("")

    option = int(input("Please choose an option from the menu: "))

    if option == 1:
        print(encode(str(input("Please enter an 8 digit password: "))))
        print("")

    if option == 3:
        break

print("Goodbye!")