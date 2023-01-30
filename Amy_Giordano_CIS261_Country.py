def display_menu():
    print("COMMAND MENU")
    print("view - View country name")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program")
    print()


def view_country(countries):
    if not countries:
        print("No countries found.")
        return


    print("country codes:", end=" ")
    for code in countries:
        print(code, end=" ")
    print()


    code = input("Enter country code: ").upper()
    if code in countries:
        print("Country name:", countries[code])
    else:
        print(code, "is not a valid country code.")



def add_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        print(countries[code], "is already using this code.")
    else:
        name = input("Enter country name: ")
        countries[code] = name
        print(name, "was added.")


def delete_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        print(countries[code], "was deleted.")
        del countries[code]
    else:
        print(code, "is not a valid country code.")


def main():
    countries = {"CA": "Canada", "MX": "Mexico", "US": "United States"}
    display_menu()
    while True:
        command = input("Command: ").lower()
        if command == "view":
            view_country(countries)
        elif command == "add":
            add_country(countries)
        elif command == "del":
            delete_country(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")


if __name__ == "__main__":
    main()