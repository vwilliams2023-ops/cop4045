import turtle
def draw_leaf_straight(rec_lvl,petiole):
    """sets the starting location, direction and creation 
    speed of the leaf"""
    turtle.up()
    turtle.goto(0,-500)
    turtle.down()
    turtle.left(90)
    var = turtle.Screen()
    turtle.delay(0)
    helper(rec_lvl,petiole)
    var.exitonclick()

def helper(rec_lvl,petiole):
    """ Recursive function that creates a leaf using turtle """
    if rec_lvl == 0:
        turtle.fd(petiole)
    else:
        turtle.fd(petiole)
        turtle.left(45)
        helper(rec_lvl-1,petiole/2)
        turtle.right(90)
        helper(rec_lvl-1,petiole/2)
        turtle.left(45)
        turtle.fd(petiole)
        helper(rec_lvl-1,petiole/2)
        turtle.back(petiole)
    turtle.back(petiole)

def mapping(number):
    """maps the possible outputs of the strB function into
    a single string and returns a character from the list"""
    str="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return str[number]

def strB(n, base=10):
    """Recursive function that converts n into a string representation
    of the given base"""
    if n < base:
        return mapping(n)
    else: 
        remainder = n%base
        var  = strB(n//base,base)
        return var + mapping(remainder)
    
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
    draw_leaf_straight(6,120)
    testif(strB(1028,16) == "404", "input1028/base16", "It worked!", "it didn't work...")
    testif(strB(1234,10) == "1234", "input1234/base16", "It worked!", "it didn't work...")
    testif(strB(100,16) == "64", "input100/base16", "It worked!", "it didn't work...")
    testif(strB(1024,16) == "400", "input1024/base16", "It worked!", "it didn't work...")
    testif(strB(15,13) == "12", "input15/base13", "It worked!", "it didn't work...")
    testif(strB(123456789,26) == "AA44A1", "input123456789/base26", "It worked!", "it didn't work...")
    testif(Cnk_m(3,3) == 1, "3C3", "It worked!", "it didn't work...")
    testif(Cnk_m(4,0) == 1, "4C0", "It worked!", "it didn't work...")
    testif(Cnk_m(5,3) == 10, "5C3", "It worked!", "it didn't work...")
    testif(Cnk_m(4,2) == 6, "4C2", "It worked!", "it didn't work...")
    testif(Cnk_m(6,2) == 15, "6C2", "It worked!", "it didn't work...")
    testif(make_pairs([1,2,3], [4,5,6]) == [(1,4),(2,5),(3,6)], "firstpair", "It worked!", "it didn't work...")  
    testif(make_pairs([1,2,3], [4,5]) == [(1, 4), (2, 5)], "secondpair", "It worked!", "it didn't work...")  
    testif(make_pairs([1,2,3], [4,5,6,7,8,9]) == [(1, 4), (2, 5), (3, 6)], "thirdpair", "It worked!", "it didn't work...")  
    testif(make_pairs([], [4,5,6,7,8,9]) == [], "fourthpair", "It worked!", "it didn't work...")  
    testif(make_pairs([1,2,3], []) == [], "fifthpair", "It worked!", "it didn't work...")  


def Cnk_m(n,k):
    """ returns the value of a the binomial coefficient using memoization """
    if n not in diction:
        diction[n] = {}
    if k not in diction[n]:
        if n==k or k == 0:
            diction[n][k] = 1
        else:
            diction[n][k] = Cnk_m(n-1, k-1) + Cnk_m(n-1, k)
    return diction[n][k]
diction ={}

def make_pairs(seq1,seq2):
    """takes two lists a parameters and returns a list with 
    all tuples where both lists have a element at a matching index
    """
    if len(seq1) == 0 or len(seq2) == 0:
        return []
    else:
        var1 = (seq1[0],seq2[0])
        var2 = make_pairs(seq1[1:],seq2[1:])
        return [var1] + var2

if __name__ == "__main__":
    main()
