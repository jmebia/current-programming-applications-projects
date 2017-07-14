# problem no.1
def prob1():
    l = []
    while(True):
        i = input("Enter a value: ")
        if i == "exit": break
        l.append(i)
    print(l)

# problem no.2
def prob2():
    while(True):
        i = input("Enter a string: ")
        if (len(i) < 3): print(i)
        elif (i == 'stop'): print("Goodbye!"); break
        elif (i.endswith("ing")): print ( i +'ly')
        else: print ( i +'ing')

# problem no.3
def unite_unique(*_list):
    ol = []
    for l in _list: # checks every list in the parameter
        for i in l: # checks for every value in list
            b = False
            for j in ol: # checks if output list contains the value i
                if (j == i): b = True; break
            if (b == False): ol.append(i)

    print(ol)

# problem no.4
def reverse_complemen(_string = ""):
    out = ""
    for i in _string.upper():
        if (i == "A"): out = "T" + out
        elif (i == "T"): out = "A" + out
        elif (i == "C"): out = "G" + out
        elif (i == "G"): out = "C" + out
        elif(i == ""): break
        else: out = "INVALID"; break
    print(out)


# run problems
print("\nPROBLEM #1")
prob1()
print("\nPROBLEM #2")
prob2()
print("\nPROBLEM #3")
unite_unique ([1,2,3],[2,4,1])
print("\nPROBLEM #4")
reverse_complemen("TCGCAG")
