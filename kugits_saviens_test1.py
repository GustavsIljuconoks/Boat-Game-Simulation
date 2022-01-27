#arr cooardinates
arrCooardinates = [
[0, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]]

#key value pairs
letterIndexes = { 
"A" : 0,
"B" : 1,
"C" : 2,
"D" : 3}

numberIndexes = {
"1" : 0,
"2" : 1,
"3" : 2,
"4" : 3} 

#user input
userInput = "B2"

"""
def valueCheck():
    if userInput in letterIndexes and numberIndexes:
        print("Sākam darbu!")
    else:
        print("Jūsu ievadītais skaitlis ir nepiemērots.")
"""

#value spliting
letter = userInput[0]
number = numberIndexes[userInput[1]]
index = letterIndexes[letter]



print(arrCooardinates[number][index])

#def arrCooardinatesReturn():
#   modifiedValues=arrCooardinates[number][index]
#    print(modifiedValues)
