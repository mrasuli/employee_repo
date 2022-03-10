#always start with the basic things:
#we have a loop, user need to pick options
#always we start with the: __main__ == "__main

def read_employee_id():
    while True:
        employee_id_str = input("Please enter your employee id: ")
        if employee_id_str.isdigit():
            employee_id = int(employee_id_str)
            return id
        else:
            print("Enter valid numbers: ")


def read_first_name():
    while True:
        first_name = input(f"Please enter your first name :")
        if len(first_name.strip()) > 2:
            return first_name
        else:
            print("Please enter a valid name: ")


def read_last_name():
    while True:
        last_name = input("Please enter your second name: ")
        if len(last_name.strip()) > 2:
            return last_name
        else:
            print("Please enter a valid name: ")


def read_birth_year():
    while True:
        birth_year_str = input("Please enter you birth year: ")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year >= 1900) and (birth_year <= 2004):
                return birth_year
            else:
                print("Please enter years between 1900 - 2004: ")
        else:
            print("Please enter the correct dates in digits: ")

def read_birth_month():
    while True:
        birth_month_str = input("Please enter you birth month: ")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month >= 1) and (birth_month <= 12):
                return birth_month
            else:
                print("Please enter numbers between 1 and 12: ")
        else:
            print("Please enter the correct dates in digits: ")


def read_birth_day():
    while True:
        birth_day_str = input("Please enter you birth day: ")
        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day >= 1) and (birth_day <= 31):
                return birth_day
            else:
                print("Please enter dates between 1 and 31: ")
        else:
            print("Please enter the correct dates in digits : ")


def read_emp_position():
    while True:
        emp_position_str = input("Please enter your employee position: ")
        if len(emp_position_str.strip()) > 0:
            emp_position = str(emp_position_str)
            return emp_position
        else:
            print("Please enter your position using characters: ")


def read_graduate():
    choices = ["Yes", "No"]
    while True:
        graduated_str = input("Please type 'Yes' if you have graduated from uni or 'No' if you have not: ")
        if graduated_str in choices:
            return graduated_str
        else:
            print("Please enter 'Yes' if you have graduated from uni or 'No' if you have not: ")

def add_employee():  # a dictionary of employees

    employee = {
                "Employee ID" : read_employee_id(),
                "Employee First Name" : read_first_name(),
                "Employee Last Name" : read_last_name(),
                "Birth Year" : read_birth_year(),
                "Birth Month" : read_birth_month(),
                "Birth Day" : read_birth_day(),
                "Employees Position" : read_emp_position(),
                "Is employee a graduate?" : read_graduate(),
                }
    return employee
#
def remove_employees():
    remove_employee_id = input("Please enter employee id: ")
    if remove_employee_id.isdigit():
        for id in range (len(employee)):
            if employee [id]["Employee ID"] == remove_employee_id:
                del employee[id]
                return employees
            else:
                print("Employee ID doesnt match: ")

        # else:
        #     print("Please enter the correct employee id: ")
        #     elif choices_remove = 1:
        #     remove_id = remove_employees()
        #     del employee [remove_id]
        #     print(f"The employee with {remove_id} has been removed")
        #     print(employee)



if __name__ == "__main__":

    while True:  # copy these and should go above the line
        employee = add_employee() # one employee
        print(employee)
        return
        remove_employees()
        break