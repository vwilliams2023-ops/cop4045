def multiples():

    result = [(a, b, c, d) 
          for a in range(1, 11)
          for b in range(a + 1, 11)
          for c in range(a + 1, 11)
          for d in range(c + 1, 11)
        if a**2 + b**2 == c**2 + d**2]
            
    return result
anything = multiples()
print(anything)


def strings(list):
    return [(i.lower(), len(i)) for i in list if len(i) < 5]
anything = strings(['One', 'SEVEN', 'three', 'two', 'Ten'])
print(anything)

def fullnames(names):
    result = [(name.find(" "), name.find(" ",(name.find(" ") + 1)), name) for name in names ]
    any = [word[2][0:word[0] + 1] + word[2][word[0] + 1] + "." + word[2][word[1]:] for word in result]
    return any
print(fullnames(['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']))

def ana(lst1,lst2):
#set to lowercase and check if they are equal, use sorted
    result = [(w1,w2)  for w1 in lst1 for w2 in lst2  
              if sorted(w1.lower()) == sorted(w2.lower())]
    return result
print(ana(["Spam", "Trams", "Elbows", "Tops", "Astral"],
      ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]))

def dic(s):
    result = {i:len(i) for i in s}
    return result
print(dic(['one', 'two', 'three']))

def dic2(text):
    result = {i:c for i,c in enumerate(text) if c.lower() in ["a","e","i","o","u"]}
    return result
print(dic2("Hello world"))