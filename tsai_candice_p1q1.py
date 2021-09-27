# Quiz Creation Activity


# Quiz has 5 questions the user will answer.
# It will keep track of score and give
# A final result
score = 0
total_amount_of_questions = 0
name = (input("Welcome to the Genshin Impact quiz! What is your name? 🤗 "))
print(f'Alright {name}, lets get started shall we? 😁')
print()

primogems = (input('1. How many primogems does one fate cost? ☄️ '))
if primogems == "160":
    print("Yes, well done!")
    score = score + 1
    print(f'Your score is {score}')
else:
    print("You'll get it next time.")
    print("The answer is: 160")
    print(f'Your score is {score}')

print()
print("-------------------------------------------------------")
total_amount_of_questions = total_amount_of_questions + 1
print('2. Which on of the following reactions is caused when applying cryo to electro? ❄️⚡️ ')
print("A. Melt")
print("B. Crystalize")
print("C. Burning.")
print("D. Superconduct.")
print("E. Vaporize.")
reaction = input()
if reaction == "Superconduct":
    print("Nice job!")
    score = score + 1
    print(f'Your score is {score}')
elif reaction == "superconduct":
    print("Nice job!")
    score = score + 1
    print(f'Your score is {score}')
elif reaction == "D":
    print("Nice job!")
    score = score + 1
    print(f'Your score is {score}')
elif reaction == "d":
    print("Nice job!")
    score = score + 1
    print(f'Your score is {score}')
else:
    print("That's wrong.")
    print("The answer is: D. Superconduct")
    print(f'Your score is {score}')

print()
print("-------------------------------------------------------")
total_amount_of_questions = total_amount_of_questions + 1
region = (input('3. What is the name of the 3rd and newest region in Teyvat? 🏯 '))
if region == "inazuma":
    print("You got it right!")
    score = score + 1
    print(f'Your score is {score}')
elif region == "Inazuma":
    print("You got it right!")
    score = score + 1
    print(f'Your score is {score}')
else:
    print("Darn")
    print("The answer is: Inazuma")
    print(f'Your score is {score}')

print()
print("-------------------------------------------------------")
total_amount_of_questions = total_amount_of_questions + 1
print('4. Tartaglia is which number of the Fatui Harbingers?🎭')
print("A. 13")
print("B. 11")
print("C. 17.")
print("D. 7.")
print("E. 9.")
harbingers = input()
if harbingers == "11":
    print("Excellent!")
    score = score + 1
    print(f'Your score is {score}')
elif harbingers == "eleven":
    print("Excellent!")
    score = score + 1
    print(f'Your score is {score}')
elif harbingers == "Eleven":
    print("Excellent!")
    score = score + 1
    print(f'Your score is {score}')
elif harbingers == "b":
    print("Excellent!")
    score = score + 1
    print(f'Your score is {score}')
elif harbingers == "B":
    print("Excellent!")
    score = score + 1
    print(f'Your score is {score}')
else:
    print("That was not the answer.")
    print("The answer was B. 11")
    print(f'Your score is {score}')

print()
print("-------------------------------------------------------")
total_amount_of_questions = total_amount_of_questions + 1
vision = (input('4. Which elemental vision type does Keqing wield?🐱 '))
if vision == "electro":
    print("Correct!")
    score = score + 1
    print(f'Your score is {score}')
elif vision == "Electro":
    print("Correct!")
    score = score + 1
    print(f'Your score is {score}')
elif vision == "electric":
    print("Correct!")
    score = score + 1
    print(f'Your score is {score}')
elif vision == "Electric":
    print("Correct!")
    score = score + 1
    print(f'Your score is {score}')
else:
    print("Wrong")
    print("The answer is: Electro")
    print(f'Your score is {score}')

print()
print("-------------------------------------------------------")
total_amount_of_questions = total_amount_of_questions + 1
cat = (input('6. Is Keqing a cat?🤔 '))
if cat == "No":
    print("You are on a roll!")
    score = score + 1
    print(f'Your score is {score}')
elif cat == "no":
    print("You are on a roll!")
    score = score + 1
    print(f'Your score is {score}')
elif cat == "Yes":
    print("You are on a roll!")
    score = score + 1
    print(f'Your score is {score}')
elif cat == "yes":
    print("You are on a roll!")
    score = score + 1
    print(f'Your score is {score}')
else:
    print("Ha ha very funny")
    print("The answer is: No/Yes")
    print(f'Your score is {score}')

print()
print("-------------------------------------------------------")
total_amount_of_questions = total_amount_of_questions + 1
elements = (input('7. How many elements are in the Genshin universe?💭 '))
if elements == "7":
    print("That is correct!")
    score = score + 1
    print(f'Your score is {score}')
else:
    print("That is incorrect>")
    print(f'Your score is {score}')

print()
print("-------------------------------------------------------")
was_this_fun = (input('Was this a fun quiz?😊 '))
print(f'{was_this_fun}? Great to hear!😄')
print()
final_score = round(score / total_amount_of_questions * 100)
print(f'Your final score is: {final_score}%')
if final_score > 99:
    print("Full score! Wonderful!")
elif final_score > 80:
    print("Nice job!")
elif final_score > 60:
    print("Hmm, not bad")
elif final_score > 40:
    print("Alright then!")
else:
    print("Osmanthus wine tastes the same as I remember 😕")