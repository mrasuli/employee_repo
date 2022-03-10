def read_options():
    while true:
        user_option = input("This is the list of options: ADD, remove, exit: Exit the app")
        user_option = user_option.strip()

        if user_option in ["add", "remove", "exit"]:
            return user_option
        else:
            print("Error, select an option")


def read_first_name():
    while True:
        first_name = Input("Enter...")
        first_name = first_name.strip()
        if len(first_name) >= 2:
            return first_name
        else:
            print("Error")


def create_employee_dictionary():
    employee_first_name = read_first_name()

    employee = {

    }


if __name__ == "__main__":
    while True:
        options = read_options()

        if option == "add": # dictionary is best used to add these data as you will have the key pairs so you can access data using keys
            employee_dict = create_employee_dictionary()
            print("the user want to add an employee")
        elif option == "remove":
            pritn("the user want remove an employee")
        elif option == "exit":
            print("Thanks, see you later")
            break
        else:
            print("Unknown options")


