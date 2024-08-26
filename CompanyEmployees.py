class Employee:
    def __init__(self, name, salary=45000, work_hours=36.5, leave=15):
        self.name = name
        self.salary = salary
        self.work_hours = work_hours
        self.leave = leave

    def getName(self):
        return self.name

    def getLeave(self):
        return self.leave

    def getSalary(self):
        return self.salary

    def getHours(self):
        return self.work_hours

    def work(self):
        print(f"{self.name} is doing their work")

    def __str__(self):  
        return f"Employee(Name: {self.name}, Salary: {self.salary}, Work_hours: {self.work_hours}, Leave: {self.leave})"

    def leave_cost(self) -> float:
        daily_salary = self.salary / 260  # 260 working days IN YEAR
        return daily_salary * self.leave


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.salary += 20000  
        self.leave += 3

    def work(self):
        print(f"{self.name} is managing their departments")

    def __str__(self): 
        return f"Manager(Name: {self.name}, Salary: {self.salary}, Work_hours: {self.work_hours}, Leave: {self.leave})"


class Secretary(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.work_hours = 40

    def work(self):
        print(f"{self.name} is typing, filing, and taking messages")

    def __str__(self): 
        return f"Secretary(Name: {self.name}, Salary: {self.salary}, Work_hours: {self.work_hours}, Leave: {self.leave})"

#Main
def main():
    employees = [] 
    employees.append(Employee("Liepel"))
    employees.append(Employee("Samuel"))
    employees.append(Secretary("Bhavika"))
    employees.append(Secretary("Mikayla"))
    employees.append(Employee("Shaadli"))                #array with hardcoded values
    employees.append(Manager("Kakkarot"))
    employees.append(Employee("Demetri"))
    employees.append(Employee("Eric"))
    employees.append(Secretary("Athenkosi"))
    employees.append(Manager("Bu"))

    #  employees + work
    for emp in employees:
        print(emp)
        emp.work()

    #  average salary 
    total_salary = sum(emp.salary for emp in employees)
    avg_salary = total_salary / len(employees)
    print(f"\nAverage Salary is: R{avg_salary:.2f}")

    #  leave cost for each employee
    print("\nLeave cost is estimated at:")
    for emp in employees:
        cost = emp.leave_cost()
        print(f"{emp.name}'s cost: R{cost:.2f}")


# Run 
if __name__ == "__main__":
    main()
   




