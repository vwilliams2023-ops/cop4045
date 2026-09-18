def line_number(file1,file2):
    """ Reads file1 line by line, 
    adds numbers and decimals to each line in the file
    adds the formatted file1 text to file2"""
    f1 = None
    f2 = None
    try:
       f1 = open(file1, "r")
       f2 = open(file2, "w")
       count = 0     
#Itterates through file1, numbers/dots each line and pushes the formatted text into file2
       for line in f1:
           count = count + 1
           f2.write(f"{count}. {line}" )
#If computer can't find file1 or file2 outputs errors
    except FileNotFoundError: 
        print("File does not exist.")
        raise

    except Exception:
        print("Unknown error occurred")
        raise
#Closing the file
    finally:
        if f1 is not None: 
            f1.close()
        if f2 is not None: 
            f2.close()


def main(): 
    """ main functions tells line and parse functions to run """
    line_number("test.py","test.py.txt")
    tuples = parse_functions("funs.py")
    print(tuples)

def alph(sortname):
    """ Returns from the tuple the name element
    to put it in alphabetical order"""
    return sortname[1]


def parse_functions(file):
    """ Reads through file seaching for function names, perameters, non-commented code
     inside functions, and the line the function is declared on. Prints all function info found
      in a tuple of tuples """
    try:
        f = open(file, "r")
        name = None
        arg = None 
        string = ""
        count = 0
        startcount = 0
        tuples = ()
        doc = False
        for line in f:
            count = count + 1
            comment = line.find("#")
            cleanline = line[0:comment]
            cstrip = cleanline.strip()
#ignores the spaces from the cleanline string
            if cstrip != "":
                if cstrip.startswith('"""'):
                    doc = True
                if doc: 
                    if cstrip.endswith('"""'):
                        doc = False
                    continue
                if cleanline.startswith("def "):
                    if name is not None:
                #tuples inside a tuple 
                        tuples = tuples + ((startcount,name,arg,string),)
                #Text from file stored and put in the tuple
                    startcount = count
                    string = ""
                    end = cleanline.find("(")
                    start = cleanline.find("def ")
                    name = cleanline[4:end]
                    end = cleanline.find(")")
                    start = cleanline.find("(") + 1
                    arg = cleanline[start:end]
                string = string + cleanline
        tuples = tuples + ((startcount,name,arg,string),)
        sortedtuple = tuple(sorted(tuples,key=alph))
        return sortedtuple
    
    except FileNotFoundError: 
        print("File does not exist.")
        raise
    
    except Exception:
        print("Unknown error occurred")
        raise
    
    finally:
        if f is not None: 
            f.close()
        
main()