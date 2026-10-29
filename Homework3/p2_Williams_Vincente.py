class ParkingPermit():
    """defines a parking permit for a college"""
    def __init__(self, name, months, fee):
        """constructor with name as the permit owners name,
        months as the number of months paid for by owner and fee
        listing of fees"""
        self.owner_name = name
        self.months_bought = months
        self.fee_schedule = fee
        
    def cost(self):
        """returns the cost of the permit"""
        raise NotImplementedError("invalid permit type")

    def __repr__(self):
        """returns a string that represents the object and all of 
         its properties """
        return f"ParkingPermit({self.owner_name}, {self.months_bought}, {self.fee_schedule})"
        
    def __str__(self):
        """returns a string representation meant to be readable
        to humans"""
        return f"Name of owner: {self.owner_name}, Cost of Permit: {self.cost()}"
    

class StudentPermit(ParkingPermit):
    """sub class parking permit for students"""
    def __init__(self, name, months, vreg):
        """constructor with name as student permit owners name, months 
        as number of months the student has paid and vreg for the number of vehicles
        the student has registered"""
        super().__init__(name, months, {"student_fee_monthly": 25, 
                    "student_fee_onetime": 10,
                    })
        self.vreg_number = vreg
        if self.vreg_number < 1:

            raise ValueError("Must have a positive number of vehicles")

    def cost(self):
        """The one time registration cost and the recurring monthly cost"""
        partial_cost = self.months_bought*self.fee_schedule["student_fee_monthly"]
        partial_cost = partial_cost + self.vreg_number*self.fee_schedule["student_fee_onetime"] - self.fee_schedule["student_fee_onetime"]
        return partial_cost
    
    def __repr__(self):
            """"string returning the students permit information: Their name, months paid, payment cost and number
            of vehicles registered"""
            return f"StudentPermit({self.owner_name}, {self.months_bought}, {self.fee_schedule}, {self.vreg_number})"
           
    
class FacultyPermit(ParkingPermit):
    """sub class parking permit for faculty"""
    def __init__(self, name, months, garage):
        """constructor with name giving permit owners name, months giving 
        number of months paid for and garage giving garage access"""
        super().__init__(name, months, {
                    "faculty_fee_monthly": 40,
                    "garage_access": 15})
        self.g_access = garage

    def cost(self):
        """returns the cost with and without garage access"""
        partial_cost = self.months_bought*self.fee_schedule["faculty_fee_monthly"]
        if self.g_access:
            partial_cost = self.months_bought*(self.fee_schedule["faculty_fee_monthly"] + self.fee_schedule["garage_access"])
        return partial_cost

    def __repr__(self):
        """returns a string holding the faculty permit owners name, the number of months 
        bought, the cost of the permit and whether the owner is paying for garage access"""
        return f"FacultyPermit({self.owner_name}, {self.months_bought}, {self.fee_schedule}, {self.g_access})"


       
def summarize_list(permits):
    """takes a list of permit objects and returns their total value"""
    total_permits_cost = 0
    for i in permits:
        print(f"{i}")
        total_permits_cost = total_permits_cost + i.cost()
    return total_permits_cost

def main():

    permit1 = StudentPermit("Vincente Williams", 100, 20)
    permit2 = StudentPermit("Will Smith", 3, 2)
    permit3 = FacultyPermit("Jane Joe", 2, False)
    permit4 = FacultyPermit("John Joe", 5, True)
    x = summarize_list([permit1,permit2,permit3,permit4])
    print(f"Total cost of all permits: {x}")

if __name__ == "__main__":
     main()
    

