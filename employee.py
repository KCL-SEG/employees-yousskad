"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryOnly(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}.'



class HourlyWithoutComm(Employee):
    def __init__(self, name, wage, hours):
        super().__init__(name)
        self.wage = wage
        self.hours = hours

    def get_pay(self):
        return self.wage * self.hours

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour. Their total pay is {self.get_pay()}.'

class SalaryPlusComm(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def get_pay(self):
        return self.salary + self.bonus

    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}.'


class HourlyPlusComm(Employee):
    def __init__(self, name, wage, hours, bonus):
        super().__init__(name)
        self.wage = wage
        self.hours = hours
        self.bonus = bonus

    def get_pay(self):
        return (self.wage * self.hours) + self.bonus

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}.'


class SalaryPlusBonus(Employee):
    def __init__(self, name, num_of_contracts, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus
        self.num_of_contracts = num_of_contracts


    def get_pay(self):
        return self.salary + (self.bonus*self.num_of_contracts)

    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.num_of_contracts} contract(s) at {self.bonus}/contract. Their total pay is {self.get_pay()}.'


class HourlyPlusBonus(Employee):
    def __init__(self, name, num_of_contracts, wage, hours, bonus):
        super().__init__(name)
        self.wage = wage
        self.hours = hours
        self.bonus = bonus
        self.num_of_contracts = num_of_contracts


    def get_pay(self):
        return (self.hours*self.wage) + (self.bonus*self.num_of_contracts)

    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.num_of_contracts} contract(s) at {self.bonus}/contract. Their total pay is {self.get_pay()}.'



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryOnly('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyWithoutComm('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryPlusBonus('Renee', 4, 3000, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyPlusBonus('Jan', 3, 25, 150, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryPlusComm('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyPlusComm('Ariel', 30, 120, 600)
