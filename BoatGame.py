#imports randint module
from random import randint 

#game condition set to true
gameCondition = True 


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

print('Spēles laukums ir 4x4 jeb no A-D un no 1-4')


"""
Actual game code
"""


while gameCondition:
    userShot = 5
    userResult = 0

    #boat location randomizer
    letterIndexesRandom = randint(0,3)
    numberIndexesRandom = randint(0,3)

    #tuple creation with random boat coordinates
    boatLocation = letterIndexesRandom, numberIndexesRandom
    (boatLetter, boatNumber) = boatLocation
    print(boatLetter)
    print(boatNumber)

    while True:
        #user input
        userInput = input('Kur izšausiet: ')
        letter = letterIndexes[userInput[0]]
        number = numberIndexes[userInput[1]]

        #user shots down boat
        if letter == boatLetter and number == boatNumber:
            print('Jūs trāpijāt pa kuģi!')
            userResult += 1
            break
        #user misses boat
        else:
            print('Jūs netrāpijāt pa kuģi!')
            userShot -= 1
            print('Tev ir atlikuši',userShot,'šavieni!')
            
        #userShot is zero
        if userShot == 0:
            print('Jūs netrāpijāt pa kuģīti!')
            print('Jūs ieguvāt',userResult,'punktus!')
            break

    #game continue decision
    userAnswer=input('Vai Jūs vēlaties spēli turpināt? : Y/N ')
    if userAnswer == 'Y':
        gameCondition = True

    if userAnswer =='N':
        gameCondition = False