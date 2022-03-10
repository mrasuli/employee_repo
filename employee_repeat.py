def read_list():
    while True:  # step one
        user_option = input(
            "Please select from the list of your options: add: to add an employee, remove: to remove an employee, list: to list the employees, update: to update employee data, exit: Exit the app: \n")
        user_option = user_option.strip()
        if user_option in ["add", "remove", "list", "update", "exit"]:
            return user_option
        else:
            print("Error, please add a valid option from the list")


def read_first_name():
    while True:
        first_name = input("Please enter your first name: ")
        first_name = first_name.strip()
        if len(first_name) >= 2:
            return first_name
        else:
            print("Please enter a valid name more than 2 characters")


def read_last_name():
    while True:
        last_name = input("Please enter your Last Name: ")
        last_name = last_name.strip()
        if len(last_name) >= 2:
            return last_name
        else:
            print("Please enter your Last Name: ")


def read_position():
    while True:
        emp_position = input("Please enter your position: ")
        emp_position = emp_position.strip()
        if len(emp_position) >= 1:
            return emp_position
        else:
            print("Error, the employee position should be more than 1 character")


def read_year():
    while True:
        year_str = input("Please enter the Birth year")
        year_str = year_str.strip()
        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, the employee birth year should be between 1900 and 2004")
        else:
            print("Error, the employee birth year should be a digit")

def read_month():
    while True:
        month_str = input("Please enter the Birth month")
        month_str = month_str.strip()
        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, the employee birth year should be between 1 and 12")
        else:
            print("Error, the employee birth month should be a digit")


def read_day():
    while True:
        day_str = input("Please enter the Birth day")
        day_str = day_str.strip()
        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, the employee birth day should be between 1 and 12")
        else:
            print("Error, the employee birth day should be a digit")


def read_graduated():
    while True:
        is_graduated_str = input("Have the employee graduated from the Uni (y/n):")
        is_graduated_str = is_graduated_str.strip()
        if is_graduated_str in ["y", "n"]:
            if is_graduated_str == "yes":
                return True
            else:
                return False
        else:
            print("Please enter y or n ")

# def read_graduate():
#     choices = ["Yes", "No"]
#     while True:
#         graduated_str = input("Please type 'Yes' if you have graduated from uni or 'No' if you have not: ")
#         if graduated_str in choices:
#             return graduated_str
#         else:
#             print("Please enter 'Yes' if you have graduated from uni or 'No' if you have not: ")



def create_employee_dictionary():  # step 5
    employee_first_name = read_first_name(),
    employee_last_name = read_last_name(),
    empployee_position = read_position(),
    employee_birth_year = read_year(),
    employee_birth_month = read_month(),
    employee_birth_day = read_day(),
    employee_is_graduated = read_graduated(),
    employee = {
        "first_name": employee_first_name,  # step 5
        "last_name": employee_last_name,
        "employee Position": read_position(),
        "employee_birth_year": read_year(),
        "employee_birth_month": read_month(),
        "employee_birth_dau": read_day(),
        "employee_is_graduated": read_graduated(),
    }
    return employee

def read_employee_id():
    while True:
        employee_id_str = input("Please enter the employee id")
        employee_id_str = employee_id_str.strip()
        if employee_id_str.isdigit():
            id = int(employee_id_str)
            if id > 0:
                return id
            else:
                print("Error, the employee id should be a positive number")
        else:
            print("Error, the employee id should be a digit")



if __name__ == "__main__":  # step 2

    while True:
        user_option = read_list()  # step 3 = this reads the user options

        if user_option == "add":  # step 4 = adding the user options which are the inputs from step one
            print("The user wants to add an employee")
            employee_dictionary = create_employee_dictionary()  # step 5 = will return a value an d ican use it in the variable
            print(employee_dictionary)

# here we need to save the dictionary because everytime we enter a new employee, the previous one will be gone.
# so we should create a dictionary of dictionaries so everytime a new employee is added with their id as the key with the values
# we need to define a dictionary as all employees dictionary

            employee_id = read_employee_id

            all_employees_dictionary = {
                employee_id: employee_dictionary   # employee id will be the key and the employee dictionary will be the value
            }
            print(all_employees_dictionary)

        elif user_option == "remove":
            print("The user wants to remove an employee")
        elif user_option == "list":
            print("The user wants the list of employees")
        elif user_option == "update":
            print("The user wants to update the employees")
        elif user_option == "exit":
            print("Thanks, see you later")
        else:
            print("Unknown error")
