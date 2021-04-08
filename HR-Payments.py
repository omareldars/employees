from itertools import zip_longest as zl

class RegularPay:
    Name = ''
    pyRate = 0.0
    def __init__(self, name, pyrate):
        self.Name = name
        self.pyRate = pyrate

    def computePay(self, hours):
        Rate = hours * self.pyRate
        print(self.Name, " will be  paid: ", Rate)

    def showNames(self):
        print(self.Name)


class HazardPay(RegularPay):
    hazardRate = 0.0
    def __init__(self, name, payrate, hazardRate):
        super().__init__(name,payrate)
        self.hazardRate = hazardRate

    def computePay(self, hours):
        hRate = hours * self.hazardRate
        super().computePay(hours)
        print(self.Name, " will be  paid as Hazard: ", hRate)

    def showNames(self):
        super().showNames()


def main():
    l1 = []
    l2 = []
    while True:
        print("\n What would you like to do? \n 1- Add Regular Pay employee \n 2- Add Hazard Pay employee \n 3- Print employees info \n 4- Compute payment \n 5- Exit \n")
        choice = int(input())
        if choice == 1:
            name = input("Enter Employee Name: ")
            rate = int(input("Enter Pay Rate: "))
            l1.append(RegularPay(name, rate))
        elif choice == 2:
            hname = input("Enter Employee Name: ")
            prate = int(input("Enter Pay Rate: "))
            hrate = int(input("Enter Hazard Rate: "))
            l2.append(HazardPay(hname, prate, hrate))
        elif choice == 3:
            print("The employees are:\n")
            for i in l1:
                i.showNames()
            for j in l2:
                j.showNames()
        elif choice == 4:
            cname = input("Enter Employee Name: ")
            hours = int(input("Enter the hours: "))
            for l11, l22 in list(zl(l1, l2)):
                if l11.Name == cname:
                    l11.computePay(hours)
                elif l22.Name == cname:
                    l22.computePay(hours)
                else:
                    print(cname," was not found!")
        elif choice == 5:
            print("Thank You")
            break
        else:
            print("Invalid Choice !!")


main()




# Sample Output
# What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 1
# Enter Employee Name: Aisha
# Enter Pay Rate: 5

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 3
# The employees are:

# Aisha

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 2
# Enter Employee Name: maryam
# Enter Pay Rate: 2
# Enter Hazard Rate: 3

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 3
# The employees are:

# Aisha
# maryam

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 4
# Enter Employee Name: Aisha
# Enter the hours: 10
# Aisha  will be  paid:  50

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 6
# Invalid Choice !!

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 1
# Enter Employee Name: Noor
# Enter Pay Rate: 3

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 3
# The employees are:

# Aisha
# Noor
# maryam

#  What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 4
# Enter Employee Name: Asmaa
# Enter the hours: 20
# Asmaa  was not found

# What would you like to do? 
#  1- Add Regular Pay employee 
#  2- Add Hazard Pay employee 
#  3- Print employees info 
#  4- Compute payment 
#  5- Exit 

# 5
# Thank You