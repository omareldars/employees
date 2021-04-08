from employee import Employee
class Salary:
    working_rate = 0.0
    working_years = 0
    def __init__(self,working_years,fname,lname):
        global company_name
        company_name = 'Kuwait Company'
        self.emb_obj = Employee(fname,lname)
        self.working_years = working_years
        if working_years < 0:
            working_years = 0
            working_rate = 0.0
        elif working_years <= 12:
            working_rate = 110.8
        else:
            working_rate = 210.3

    
    def cal_salary(self,working_years,working_rate):
        salary = self.working_rate * self.working_years
        return salary

    def __gt__(self,other):
        emp1 = self.cal_salary(self.working_years,self.working_rate)
        emp2 = other.cal_salary(other.working_years,other.working_rate)
        if emp1 > emp2:
            return True
        else:
            return False


    def __str__(self):
        self.emb_obj.__str__()
        print(company_name," gives a monthly salary of ",self.cal_salary(self.working_years,self.working_rate))
