class ParkingPermit():
    
    def __init__(self, name, months, fee):
        self.owner_name = name
        self.months_bought = months
        self.fee_schedule = fee
        
    def cost(self):
        raise NotImplementedError("come back later")

    def __repr__(self):
                return f"ParkingPermit({self.owner_name}, {self.months_bought}, {self.fee_schedule})"
        
    def __str__(self):
                return f"Name of owner: {self.owner_name}, Cost of Permit: {self.cost()}"
    

class StudentPermit(ParkingPermit):

    def __init__(self, name, months, vreg):
        super().__init__(name, months, {"student_fee_mountly": 25, 
                    "student_fee_onetime": 10,
                    })
        self.vreg_number = vreg
        if self.vreg_number < 1:

            raise ValueError("Must have a positive number of vehicles")

    def cost(self):
        partial_cost = self.months_bought*self.fee_schedule["student_fee_mountly"]
        partial_cost = partial_cost + self.vreg_number*self.fee_schedule["student_fee_onetime"] - self.fee_schedule["student_fee_onetime"]
        return partial_cost
    
    def __repr__(self):
            return f"StudentPermit({self.owner_name}, {self.months_bought}, {self.fee_schedule}, {self.vreg_number})"
           
    
class FacultyPermit(ParkingPermit):

    def __init__(self, name, months, garage):
        super().__init__(name, months, {
                    "faculty_fee_mounthly": 40,
                    "garage_access": 15})
        self.g_access = garage

    def cost(self):
        partial_cost = self.months_bought*self.fee_schedule["faculty_fee_mounthly"]
        if self.g_access:
            partial_cost = self.months_bought*(self.fee_schedule["faculty_fee_mounthly"] + self.fee_schedule["garage_access"])
        return partial_cost

    def __repr__(self):
        return f"FacultyPermit({self.owner_name}, {self.months_bought}, {self.fee_schedule}, {self.g_access})"


       
def summarize_list(permits):
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
main()
    

