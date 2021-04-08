class Employee:
    Firstname = ''
    Lastname = ''
    def __init__(self,fname,lname):
        global company_name
        company_name = 'Kuwait Company'
        self.Firstname = fname
        self.Lastname = lname
    
    def __str__(self):
        print(self.Firstname," ",self.Lastname," is working in ",company_name)



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


def __init__():
    print("Please Enter Emplyee (0) info")
    fname = input("First Name: ")
    lname = input("last Name: ")
    workhours = int(input("Years of Employemnt: "))
    p1 = Salary(workhours,fname,lname)
    p1.__str__()
    print("Please Enter Emplyee (1) info")
    ffname = input("First Name: ")
    llname = input("last Name: ")
    wworkhours = int(input("Years of Employemnt: "))
    p2 = Salary(wworkhours,ffname,llname)
    p2.__str__()
    if p1.__gt__(p2):
        print(fname," ",lname," has a higher salary than ",ffname," ",llname)
    else:
        print(ffname," ",llname," has a higher salary than ",fname," ",lname)
    