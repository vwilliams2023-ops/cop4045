class NVector():
    def __init__(self, param1, *param2):
        """Constructor of NVector, param1 is a list or tuple representing
         the elements of a NVector or the first element when additional 
          elements are giving in param2 """
        if param2:
            self.vector = [param1] + list(param2)
        else:
            self.vector = list(param1)
    
    def __len__(self):
        """returns the length of the vector"""
        return len(self.vector)

    def __getitem__(self,index):
        """ returns the item at a given index"""
        return self.vector[index]

    def __setitem__(self,index,value):
        """index must be set in valid index based on range of list.
        value is a integer assigned to an index in the list"""
        self.vector[index] = value

    def __str__(self):
        """returns string representing the NVector"""
        return f"NVector: {self.vector}"

    def __eq__(self, equal1):
        """returns true if self is equal, false if not"""
        if self.vector == equal1.vector:
            return True
        else: 
            return False

    def __ne__(self, notequal1):
        """returns true when not equal, false if equal"""
        return not (self == notequal1) 

    def __add__(self,other):
        """returns addition with another NVector (done element-wise) 
        or with a number (applied to all elements)"""
        if isinstance(other, int):
            return NVector([i + other for i in self.vector])
        
        elif isinstance(other, NVector):
            if len(other) == len(self):
                return NVector([self[i] + other[i] for i in range(len(self))])

            else: 
                raise ValueError("Lists not same length")
                            
        else: 
            raise ValueError("Not a integer or NVector") 

    def __radd__(self, other):
        """returns reflected addition, lets you put the integer before the 
        NVector"""
        return self.__add__(other)

    def __mul__(self, other):
        """returns scalar multiplication with another NVector or integer"""
        if isinstance(other, int):
            return sum([i * other for i in self.vector])
        
        elif isinstance(other, NVector):
            if len(other) == len(self):
                return sum([self[i] * other[i] for i in range(len(self))])

            else: 
                raise ValueError("Lists not same length")
                            
        else: 
            raise ValueError("Not a integer or NVector") 

    def __rmul__(self, other):
        """returns reflected multiplication, 
        lets you put the integer before the NVector"""
        return self.__mul__(other)

    def zeros(n):
        """returns a new NVector with 0 for all of its elements"""
        return NVector([0 for blah in range(n)])
    
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b 
    
def main():
    
    z = NVector(1, 2, 3)
    y = NVector((4, 5, 6))
    x = NVector([7, 8, 9])


    testif(len(x) == 3,"len", "len works", "len doesn't work")
    testif(y[2] == 6,"get_index", "get_index works", "get_index doesn't work")
    z[1] = 3
    testif(z[1] == 3,"set_item", "set_item works", "set_item doesn't work")
    testif(f"{x}" == "NVector: [7, 8, 9]","str", "str works", 
           f"str doesn't work. got: {x} expected: NVector: [7, 8, 9]")
    testif( x == NVector([7, 8, 9]),"eq", "eq works", "eq doesn't work")
    testif( x != NVector([7, 8, 4]),"ne", "ne works", "ne doesn't work")
    testif( x + y == NVector(11,13,15),"add_vectors", "add_vectors works", "add_vectors doesn't work")
    testif( x + 10 == NVector(17,18,19),"add_constant", "add_constant works", "add_constant doesn't work")
    testif( 10 + x == NVector(17,18,19),"radd", "radd works", "radd doesn't work")
    testif( x * y == 122,"mul", "mul works", "mul doesn't work")
    testif( x * 10 == 240,"mul", "mul works", "mul doesn't work")
    testif( 10 * x == 240,"rmul", "rmul works", "rmul doesn't work")
    testif( NVector.zeros(3) == NVector(0,0,0),"zeros", "zeros works", "zeros doesn't work")



    
    
if __name__ == "__main__":
    main()



