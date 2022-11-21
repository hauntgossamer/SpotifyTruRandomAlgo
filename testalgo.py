import random,time

t = time.time()

testlist = [f"test song {i}" for i in range(1, 1000)]

def rng(x):
    ceiling = random.randint(100, 10000)
    
    while ceiling < x.index(x[-1]):
        ceiling = random.randint(100, 10000)

    procgen = [(dict(key=j, value=k)) for j,k in enumerate([(random.randint(100, ceiling)) for i in x])]
    procgen.pop(-1)
    
    def meth1(l):
        for i in l:
            modchoice = random.choice([random.randint(2,3) for i in range(1, 100)])
            i["value"] = i["value"]*modchoice
        return sorted(l, key=lambda l: l["value"], reverse=random.choice([True, False]))
 
    def meth2(l):
        return sorted(l, key=lambda l: l["value"], reverse=True)
    
    def meth3(l):
        return sorted(l, key=lambda l: l["value"], reverse=False)
    
    sortmethod = random.randint(1,3)
    sort = meth1(procgen) if sortmethod == 1 else meth2(procgen) if sortmethod == 2 else meth3(procgen)

    print(f"sorted using sort method {sortmethod}")

    for i in enumerate(x):
        if i[0] < (x.index(x[-1])/2) - 1:
            ind1, ind2 = i[0], sort[i[0]]["key"]
            indeces, values = [ind1, ind2], [x[ind1], x[ind2]] 
            x.pop(ind1), x.pop(ind2)
            x.insert(ind2, values[0]), x.insert(ind1, values[1])
        else:
            print(x), print(f"successfully shuffled {len(x) + 1} songs!")
            return

diff = time.time() - t
print(time.time(), t)
rng(testlist)
print(f"Shuffled successfully in {diff} seconds!")


# shuffle algorithm for perceivably true random shuffling

# generate test list for use in rng function, !uncomment for use!
#
#  testlist = [f"test song {i}" for i in range(1, 1000)]  
# print(testlist)
# print("\n this is test list")  
# 
# generate a random ceiling for the rng and save it in a variable
# 
# verify that ceiling is larger than the size of the song list and regenerate until true
# 
# iterate over a list of songs, create a dictionary with key = song and value = random integer "ID" created for rearranging the list of songs
# 
# sort the songs by their generated ID's numerically using one of three randomly picked methods:
# 
# define each sort method
# 
# 1. randomly multiply each entry by 2 or 3 and then sort numerically (ascending or descending, chosen randomly)
# 2. sort numerically ascending
# 3. sort numerically descending
# 
# declare randomly picked sorting method
# translation:
#   if sortmethod == 1:
#       sort = meth1(procgen) 
#   elif sortmethod == 2:
#       sort = meth2(procgen)
#   else:
#       sort = meth3(procgen)  
# iterate through the list of songs and change the order according the the randomly generated order
# 
# iterate through list of songs
# 
# sort using randomly generated sort method
# 
# verify that i is not more than halfway through the list
#
#  swap the index of i with sort[i[0]]["key"] and vice versa
#
#  print the list of songs
