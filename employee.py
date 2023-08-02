
import os
import getpass
n = -1


class Record:
    index = []
    name = []
    salary = []
    department = []
    city = []
    emp_comp = []
    for i in range(50):
        index.append(-1)
        name.append('')
        salary.append(-1)
        department.append(-1)
        city.append('')
        emp_comp.append(-1)


rec = Record()


class Employee:
    arr = []
    num = -1
    emp_salary, emp_name, emp_dpt, emp_city, emp_comp = -1, '', -1, '', -1

    @staticmethod
    def add_record():
        global n
        n = int(input("Enter the number of employees: "))
        print("Enter employee ID, employee name, employee salary, employee department, employee city, employee company")
        temp_num = 0
        if os.path.exists("nC.txt"):
            with open("nC.txt", 'r') as nf:
                if os.stat("nC.txt").st_size == 0:
                    nf.write('0')
                else:
                    temp_num = int(nf.read())
        else:
            with open("nC.txt", 'w') as temp_file:
                temp_file.write('0')
        k = n + temp_num
        for i in range(temp_num, k):
            print(f"Employee {i + 1}")
            temp_in = input().split()
            rec.index[i], rec.name[i], rec.salary[i], rec.department[i], rec.city[i], rec.emp_comp[i] = temp_in[0], \
                                                                                                      temp_in[1], \
                                                                                                      temp_in[2], \
                                                                                                      temp_in[3], \
                                                                                                      temp_in[4], \
                                                                                                      temp_in[5]


    @staticmethod
    def create_file():
        global n
        with open("nC.txt", 'r') as nf:
            temp_num = nf.read()
        k = n + int(temp_num)
        with open("nC.txt", 'w') as nf_temp:
            nf_temp.write(str(k))
        j = int(k)
        with open("record.txt", 'a') as f:
            for i in range(int(temp_num), j):
                temp_f = f"{i + 1} {rec.salary[i]} {rec.name[i]} {rec.department[i]} {rec.city[i]} {rec.emp_comp[i]}\n"
                f.write(temp_f)

    @staticmethod
    def display():
        if os.stat("record.txt").st_size == 0:
            print("\nNo Employees to display\n")
            return
        with open("record.txt", 'r') as f:
            for i in f:
                lines = i.split()
                print(
                    f"Employee Name : {lines[2]}\t\tSalary : {lines[1]}\t\tDepartments : {lines[3]}\t\tCity : {lines[4]}\t\tEmployee company : {lines[5]}")

    def delete_record(self):
        if os.stat("record.txt").st_size == 0:
            print("\nNo Employees to delete\n")
            return
        self.arr = []
        self.num = -1
        name = input("Enter the name of the employee you want to delete : ")
        with open("record.txt", 'r') as f:
            for i in f:
                self.arr.append(i)
        flag = False
        for i in range(len(self.arr)):
            temp = self.arr[i].split()
            for j in temp:
                if j == name:
                    flag = True
                    self.num = i
        if flag:
            self.delete()
            print("\nEmployee deleted successfully\n")
        else:
            print("\nEmployee Does not Exist\n")

    def delete(self):
        with open("record.txt", 'w') as f:
            j = 0
            for i in range(len(self.arr)):
                temp = self.arr[i].split()
                if i == self.num:
                    continue
                else:
                    temp_f = f"{j} {temp[1]} {temp[2]} {temp[3]} {temp[4]} {temp[5]}\n"
                    f.write(temp_f)
                    j += 1
        with open("nC.txt", 'r') as f:
            a = f.read()
        a = int(a) - 1
        if a == -1:
            a = 0
        with open("nC.txt", 'w') as f:
            f.write(str(a))

    def modify(self):
        if os.stat("record.txt").st_size == 0:
            print("\nNo Employees to modify\n")
            return
        name = input("Enter the name of the Employee to modify : ")
        self.arr = []
        self.num = -1
        with open("record.txt", 'r') as f:
            for i in f:
                self.arr.append(i)
        flag = False
        for i in range(len(self.arr)):
            temp = self.arr[i].split()
            if name == temp[2]:
                flag = True
                self.num = i
                self.emp_name, self.emp_salary, self.emp_dpt, self.emp_city, self.emp_comp = temp[2], temp[1], temp[3], temp[
                    4], temp[5]
        if flag:
            print(f'''Choose an option
            1. Modify Name
            2. Modify Salary
            3. Modify Department
            4. Modify Company
            5. Exit''')
            ch = int(input("Enter your choice : "))
            if ch == 1:
                self.col_name = input("Enter the new Name : ")
                print("Employee Name Changed Successfully")
            elif ch == 2:
                self.col_rank = input("Enter the new Salary : ")
                print("Employee Salary Changed Successfully")
            elif ch == 3:
                self.col_br = input("Enter the new Department : ")
                print("Employee Department Changed Successfully")
            elif ch == 4:
                self.col_el = input("Enter the new Employee Company : ")
                print("Employee Company Changed Successfully")
            elif ch == 5:
                return
            else:
                print("\nInvalid Choice\n")
                return
            with open("record.txt", 'w') as f:
                j = 0
                for i in range(len(self.arr)):
                    temp = self.arr[i].split()
                    if i == self.num:
                        continue
                    else:
                        temp_f = f"{j} {temp[1]} {temp[2]} {temp[3]} {temp[4]} {temp[5]}\n"
                        f.write(temp_f)
                        j += 1
                temp_ff = f"{j} {self.emp_salary} {self.emp_name} {self.emp_dpt} {self.emp_city} {self.emp_comp}"
                f.write(temp_ff)
                print()
        else:
            print("\Employee Does not exist\n")

    @staticmethod
    def search_emp_id():
            emp_id = input("Enter the Employee ID: ")
            temp = []
            with open("record.txt", 'r') as f:
                for i in f:
                    line = i.split()
                    temp.append(line)
            for i in range(len(temp)):
                if temp[i][0] == emp_id:
                    print("\nEmployee found\n")
                    print(
                        f"Employee ID: {temp[i][0]}\t\tEmployee Name: {temp[i][2]}\t\tSalary: {temp[i][1]}\t\tDepartment: {temp[i][3]}\t\tCity: {temp[i][4]}\t\tEmployee Company: {temp[i][5]}")
                    return
            print(f"\nEmployee with ID {emp_id} does not exist")

        
    @staticmethod
    def search_emp_salary():
        emp_salary = input("Enter the Employee Salary : ")
        temp_salary = []
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp_salary.append(line)
        for i in range(len(temp_salary)):
            if temp_salary[i][1] == emp_salary:
                print("\nEmployee found\n")
                print(
                    f"Employee Name : {temp_salary[i][2]}\t\tSalary : {temp_salary[i][1]}\t\tDepartment : {temp_salary[i][3]}\t\tCity : {temp_salary[i][4]}\t\tEmployee Company : {temp_salary[i][5]}")
                return
        print(f"\nEmployee with the salary {emp_salary} does not exist")

    @staticmethod
    def search_emp_name():
        name = input("Enter the Employee Name : ")
        temp = []
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        for i in range(len(temp)):
            if temp[i][2].lower() == name.lower():
                print("\nEmployee found\n")
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company: {temp[i][5]}")
                return
        print(f"\n{name} does not exist")

    @staticmethod
    def search_emp_city():
        city = input("Enter the City Name : ")
        temp = []
        count = True
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        for i in range(len(temp)):
            if temp[i][4].lower() == city.lower():
                count = False
                print("\nEmployee found")
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        if count:
            print(f"\nEmployee does not exist in {city}")

    @staticmethod
    def search_emp_comp():
        emp_comp = input("Enter the Employee Company : ")
        temp = []
        count = True
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        for i in range(len(temp)):
            if temp[i][5] == emp_comp:
                count = False
                print("\nEmployee found")
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        if count:
            print(f"\nEmployee with company {emp_comp} does not exist")

    @staticmethod
    def sort_emp_salary():
        order = input("Sort by Ascending or Descending\nEnter A or D : ").lower()
        temp = Employee.bubble_sort(1)
        if order == 'a':
            for i in range(len(temp)):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        elif order == 'd':
            for i in range(len(temp) - 1, -1, -1):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        else:
            for i in range(len(temp)):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")

    @staticmethod
    def sort_emp_comp():
        order = input("Sort by Ascending or Descending\nEnter A or D : ").lower()
        temp = Employee.bubble_sort(1)
        if order == 'a':
            for i in range(len(temp)):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        elif order == 'd':
            for i in range(len(temp) - 1, -1, -1):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        else:
            for i in range(len(temp)):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")

    @staticmethod
    def sort_emp_name():
        order = input("Sort by Ascending or Descending\nEnter A or D : ").lower()
        temp = Employee.bubble_sort(2)
        if order == 'a':
            for i in range(len(temp)):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        elif order == 'd':
            for i in range(len(temp) - 1, -1, -1):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")
        else:
            for i in range(len(temp)):
                print(
                    f"Employee Name : {temp[i][2]}\t\tSalary : {temp[i][1]}\t\tDepartment : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEmployee Company : {temp[i][5]}")

    @staticmethod
    def bubble_sort(ch):
        if ch == 1:
            emp = 1
        elif ch == 2:
            emp = 2
        elif ch == 3:
            emp = 3
        temp = []
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        if emp == 2:
            for j in range(len(temp)):
                for i in range(0, len(temp) - j - 1):
                    if temp[i][emp].lower() > temp[i + 1][emp].lower():
                        temp[i], temp[i + 1] = temp[i + 1], temp[i]
        else:
            for j in range(len(temp)):
                for i in range(0, len(temp) - j - 1):
                    if int(temp[i][emp]) > int(temp[i + 1][emp]):
                        temp[i], temp[i + 1] = temp[i + 1], temp[i]
        return temp


def main():
    c = Employee()
    print(f'''
+------------------------------------------------+
|                                                |
|                                                |
|       Employee Record Management System        |
|                                                |
|                                                |
+------------------------------------------------+
    ''')
    while True:
        print(f'''\nChoose an option
        1. For Admin
        2. For User
        3. To Exit''')
        ans = int(input("Enter your choice: "))
        if ans == 1:
            password = getpass.getpass("Enter the password: ")
            if password == "admin":
                print("\nAccess Granted")
                print("Welcome Admin\n")
                while True:
                    print(f'''Choose an option
                    1. Add Data
                    2. Delete Data
                    3. Display
                    4. Exit''')
                    ch = int(input("Enter your choice: "))
                    if ch == 1:
                        c.add_record()
                        c.create_file()
                    elif ch == 2:
                        c.delete_record()
                    elif ch == 3:
                        c.display()
                    elif ch == 4:
                        break
                    else:
                        print("\nInvalid Choice\n")
            else:
                print("\nInvalid Password\n")
        elif ans == 2:
            print(f'''Choose an option
            1. Display
            2. Search by ID
            3. Search by Salary
            4. Search by Name
            5. Search by City
            6. Search by Company
            7. Exit''')
            ch = int(input("Enter your choice: "))
            if ch == 1:
                c.display()
            elif ch == 2:
                c.search_emp_id()
            elif ch == 3:
                c.search_emp_salary()
            elif ch == 4:
                c.search_emp_name()
            elif ch == 5:
                c.search_emp_city()
            elif ch == 6:
                c.search_emp_comp()
            elif ch == 7:
                break
            else:
                print("\nInvalid Choice\n")
        elif ans == 3:
            print("\nSuccessfully Logged Out\n")
            break
        else:
            print("\nInvalid Choice\n")


main()