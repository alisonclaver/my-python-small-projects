print("Welcome to my Quiz Game using Python DICTIONARY / Heaps Data Structure!")

play = input("Do you want to play? ")

if play != 'yes':
    quit()
print("Alrght, let's play! :) ")

#USING key value pairs or DICTIONARY
questAns = {
    "What does CPU stands for? " : 'Central Processing Unit',
    "What does GPU stands for? " : 'Graphics Processing Unit',
    "What does RAM stands for? " : 'Random Access Memory',
    "What does PU stands for? " : 'Power Supply',
    "What does LOGI stands for? " : 'Logitech'
}

score = 0

for k in range(len(questAns)):
    lols = list(questAns.keys())
    answer = input(lols[k])
    sagots = list(questAns.values())
    if answer == sagots[k]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")


print("SCORE: ", score)



    
    