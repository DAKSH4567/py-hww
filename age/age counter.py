try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age entered")
    else:
        print("Valid age")

        if age % 2 == 0:
            print("Age is Even")
        else:
            print("Age is Odd")

except ValueError:
    print("Error: Please enter a valid number")
