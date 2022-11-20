import random
import time
 # shuffle algorithm for perceivably true random shuffling

"""generate test list for use in rng function, !uncomment for use!"""
t = time.time()
testlist = [f"test song {i}" for i in range(1, 1000)]  
print(testlist)
print("\n this is test list") 

def rng(x):
    """generate a random ceiling for the rng and save it in a variable"""
    ceiling = random.randint(100, 10000)
    """verify that ceiling is larger than the size of the song list and regenerate until true"""
    while ceiling < x.index(x[-1]):
        ceiling = random.randint(100, 10000)
    """iterate over a list of songs, create a dictionary with key = song and value = random integer "ID" created for rearranging the list of songs"""
    procgen = [(dict(key=j, value=k)) for j,k in enumerate([(random.randint(100, ceiling)) for i in x])]
    """print all dictionaries in procgen"""
    """print(procgen)
    print("\n procgen before sort")"""

    """for i in procgen: print(i)"""
    
    
    """sort the songs by their generated ID's numerically using one of three randomly picked methods:"""
    """declare randomly picked sorting method"""
    sortmethod = random.randint(1,3)

    """define each sort method"""

    
    """1. randomly multiply each entry by 2 or 3 and then sort numerically (ascending or descending, chosen randomly)"""
    def meth1(l):
        
        for i in l:
            modchoice = random.choice([random.randint(2,3) for i in range(1, 100)])
            i["value"] = i["value"]*modchoice
        return sorted(l, key=lambda l: l["value"], reverse=random.choice([True, False]))
    sort = meth1(procgen)
    """print("\n procgen has been sorted")"""
    """2. sort numerically ascending"""
    

    """3. sort numerically descending"""

    
    """iterate through the list of songs and change the order according the the randomly generated order"""

    """ itearate through list of songs"""
    for i in enumerate(x):
        """verify that i is not more than halfway through the list"""
        if i[0] < x.index(x[-1])/2 - 1:
            """swap the index of i with procgen[i]["key"] and vice versa"""
            """create temp list before popping"""
            ind1 = i[0]
            ind2 = sort[i[0]]["key"]
            indeces = [ind1, ind2]
            values = [x[ind1], x[ind2]]
            x.pop(ind1), x.pop(ind2)
            x.insert(ind2, values[0]), x.insert(ind1, values[1])
            """print(f"performed swap number {i[0]}")"""
        else:
            print(x)
            print("successfully shuffled songs!")
            return
            """pop ind1 and ind2 and replace them with eachother"""
    """return the list of songs"""
    # print(x)
rng(testlist)
now = time.time()
diff = now - t
print(f"Shuffled successfully in {diff} seconds!")