def ed_read(filename, frm=0, to=-1):
    """Function for reading """
    file = open(filename, 'r').read()
    if to==-1:
        return file[frm:]
    elif to > len(file):
        raise IndexError("Parameter exceeds file lenth")
    else:
        return file[frm:to] 

def ed_find(filename, search_str):
    file = open(filename, 'r')
    file_string= file.read()
    varf=set([file_string.find(search_str,i) for i in range(len(file_string))])
    varf.discard(-1)
    varf = list(varf)
    varf.sort()
    file.close()
    return varf

def ed_replace(filename, search_str, replace_with, occurrence=-1):
    file = open(filename, 'r')
    file_string= file.read()
    file.close()
    ed = ed_find(filename, search_str)
    file = open(filename, 'w')
    if occurrence == -1:
        #replace everywhere
        file.write(file_string.replace(search_str,replace_with))
        file.close()
        return len(ed)
    elif occurrence >= len(ed):
        #dont replace
        return 0
    else:
    #replace specific occurrence 
        repl=ed[occurrence]
        portion=file_string[repl:].replace(search_str,replace_with,1) 
        var = file_string[0:repl]+ portion
        file.write(var)
        file.close()
        return 1
def ed_append(filename,string):
    file = open(filename, 'a')
    file.write(string)
    file.close()
    return len(string)

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

def test_ed_find():
    fn = "testfile1.txt" # assume this file does not exist yet.
    ed_append(fn, "0123456789") # this will create a new file
    ed_append(fn, "0123456789") # the file content is: 01234567890123456789
    lst = ed_find(fn, "345")
    testif(lst == [3,13], "test_ed_find", "Success", "Fail")

def test_ed_replace():
    fn = "testfile2.txt" # assume this file does not exist yet.
    ed_append(fn, "0123456789") # this will create a new file
    ed_append(fn, "0123456789") # the file content is: 01234567890123456789
    var1=ed_replace(fn, "345", "ABCDE", 1) # changes the file to 0123456789012ABCDE6789
    # assume we reset the file content to 01234567890123456789 (not shown)
    testif(var1 == 1,"replace_num","correct replacement amount", "incorrect replacement amount")
    testif(ed_find(fn, "ABCDE") == [13],"test_ed_replace1", "correct replacement", "incorrect replacement")
    var2=ed_replace(fn, "12", "XYZ") # changes the file to 012ABCDE6789012ABCDE6789
    testif(var2 == 2,"replace_num","correct replacement amount", "incorrect replacement amount")
    testif(ed_find(fn, "XYZ") == [1,12],"test_ed_replace2", "correct replacement", "incorrect replacement")
    var3=ed_replace(fn, "6789", "GIT", 5) 
    testif(var3 == 0,"replace_num","correct replacement amount", "incorrect replacement amount")
def main():
    test_ed_find()
    test_ed_replace()
main()