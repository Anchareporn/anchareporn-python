personal_info = ("View", 19, "Nakonnayok", "Thailand")


hobbies = ["Listen to music", "Sleep"]

def display_info():

    print("\n--- Personal Information ---")

    print(f"Name: {personal_info[0]}")

    print(f"Age: {personal_info[1]}")

    print(f"City: {personal_info[2]}")

    print(f"Country: {personal_info[3]}")

    print("Hobbies:", ", ".join(hobbies) if hobbies else "None")

    print("----------------------------\n")

def add_hobby():

    hobby = input("Enter a new hobby to add: ")

    hobbies.append(hobby)

    print(f"Hobby '{hobby}' added.\n")

def remove_hobby():

    hobby = input("Enter a hobby to remove: ")

    if hobby in hobbies:

        hobbies.remove(hobby)

        print(f"Hobby '{hobby}' removed.\n")

    else:

        print(f"Hobby '{hobby}' not found in the list.\n")

def update_age():

    global personal_info

    try:

        new_age = int(input("Enter new age: "))

        personal_info = (personal_info[0], new_age, personal_info[2], personal_info[3])

        print("Age updated.\n")

    except ValueError:

        print("Invalid age. Please enter a number.\n")



while True:

    print("Menu:")

    print("1. Display all information")

    print("2. Add new hobby")

    print("3. Remove hobby")

    print("4. Update age")

    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":

        display_info()

    elif choice == "2":

        add_hobby()

    elif choice == "3":

        remove_hobby()

    elif choice == "4":

        update_age()

    elif choice == "5":

        print("Exiting program.")

        break

    else:

        print("Invalid choice. Please try again.\n")
 