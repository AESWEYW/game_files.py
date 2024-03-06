from ast import While
from tkinter import YES

def start_quiz_game():
    max_attempts = 3
    attempts = 0
    score = 0

print("welcome to a game", "i did a bad job sO GOOD LUCK!" )

playing = input("do you want to play? (yes/no) ").lower()

if playing.lower() != "yes":
    quit()

print("okay! lets play: )")
score = 0

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print('Correct!')
        score += 1  # Increment the score
        break  # Exit the loop if the answer is correct
    else:
        print('Try again')
        attempts += 1

if attempts == max_attempts:
    print(f"incorrect; The correct answer is 'Central Processing Unit'.")

attempts = 0

while attempts <max_attempts:   
    answer = input("what dose PSU stand for? ")
    if answer.lower() == "power supply unit":
        print('correct')
        score += 1
        break
    else: 
        print('Try again')
        attempts += 1

if attempts == max_attempts:
    print(f"incorrect; The correct answer is 'power supply unit'.")        


attempts = 0

while attempts <max_attempts:     
    answer = input("what dose GPU stand for? ")
    if answer.lower() == "graphics processing unit":
        print('correct')
        score += 1
        break
    else: 
        print('Try again')
        attempts += 1
        
if attempts == max_attempts:
    print(f"incorrect; The correct answer is 'graphics processing unit'.")             

attempts = 0

while attempts <max_attempts:  
    answer = input("what dose TPU stand for? ")
    if answer.lower() == "tensor processing units":
        print('correct')
        score += 1
        break
    else: 
        print('Try again')
        attempts += 1
        
if attempts == max_attempts:
    print(f"incorrect; The correct answer is 'tensor processing units'.")        
    

attempts = 0

while attempts <max_attempts: 
    answer = input("what dose APU stand for? ")
    if answer.lower() == "accelerated processing unit":
        print('correct')
        score += 1
        break
    else: 
        print('Try again')
        attempts += 1
        
if attempts == max_attempts:
    print(f"incorrect; The correct answer is 'accelerated processing unit'.")        
    
print('you got ' + str(score)+  "questions correct" )
print('you got ' + str((score / 5) * 100) + "%.") 