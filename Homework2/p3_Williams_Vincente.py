def add_user(sn, username, fullname):
    """ This adds new users to the social network"""
    if username in sn:
        return False
    else:
        sn[username] = (fullname,[])  
        return True

def add_friend(sn, user1, user2):
    """This allows people to connect their accounts and stores that information"""
    if user1 in sn and user2 in sn:
        fullname1 = sn[user1] 
        fullname2 = sn[user2]
        fullname1 = (fullname1[0],fullname1[1] + [user2])
        fullname2 = (fullname2[0],fullname2[1] + [user1])
        sn[user1] = fullname1
        sn[user2] = fullname2
        return True
    else:
        return False

def get_friends(sn, user1, distance):
    """ Gets a users friends and gets the friends of the initial users friends"""
    if user1 in sn:
        userinfo = sn[user1] 
        friendlist = userinfo[1]
        extrafriends = set(friendlist)
        #Loops through and stores the users friends list and the friends of friends
        for i in range(1,distance):
            allfriends = set()
            for a in extrafriends:
                userinfo = sn[a] 
                friendlist = userinfo[1]
                allfriends = allfriends.union(friendlist)
            extrafriends = extrafriends.union(allfriends)
            extrafriends.discard(user1)
        return extrafriends
    else:
        return []

def save_network(filename,sn):
    """Saves the sn dictionary into a csv file"""
    openfile = None
    try:
        openfile = open(filename, "w")
        for username in sn:
            userinfo = sn[username]
            fullname = userinfo[0]
            friendlist = userinfo[1]
            openfile.write(f"{username},{fullname},{"/".join(friendlist)}\n")
    except FileNotFoundError:
        print("File does not exist.")
        raise

    except Exception:
        print("Unknown error occurred")
        raise

    finally:
        if openfile is not None: 
            openfile.close()
def load_network(filename):
    """Prints the user data from sn taken from the save_network function"""
    openfile = None
    sn = {}
    try:
        openfile = open(filename, "r")
        for i in openfile:
            comma1 = i.find(",")
            username = i[0:comma1]
            comma2 = i[comma1 + 1:].find(",") + comma1 + 1
            fullname = i[comma1 + 1:comma2]
            friendlist = i[comma2 + 1:].strip().split("/")
            sn[username] = (fullname, friendlist)
        return sn
    except FileNotFoundError:
        print("File does not exist.")
        raise

    except Exception:
        print("Unknown error occurred")
        raise

    finally:
        if openfile is not None: 
            openfile.close()
def main():
    """Calling all functions"""
    sn = {'alice': ('Alice Smith', ['maria']),
'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
'joe': ('Joseph Adams', ['maria', 'eve']),
'eve': ('Evelyn Cooper', ['joe']),
'david': ('David Benson', ['maria'])}
    add_user(sn, "Vincente", "Vincente Williams")
    add_friend(sn, "eve", "Vincente")
    print(sn)
    print(get_friends(sn,"alice",3))

    save_network("userdata",sn)

    print(load_network("userdata"))

main()