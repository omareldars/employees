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

    