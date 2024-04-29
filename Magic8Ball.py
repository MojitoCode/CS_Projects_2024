#imported modules
import random

#variable definitions
name = "Sam"
question = "Is pizza your favorite food?"
answer = ""
random_number = random.randint(1,11)

#test - output random values to the screen
#print(random_number)

#main program functions
#if question is blank, print the following message
if question == "":
  print("The magic 8 Ball is ready to answer your deepest questions!")
else:
  #else, update the answer variable, based on random number 1 - 11
  if random_number == 1:
    answer = "Yes - definitely"
  elif random_number == 2:
    answer = "It is decidedly so"
  elif random_number == 3:
    answer = "Without a doubt"
  elif random_number == 4:
    answer = "Reply hazy, try again"
  elif random_number == 5:
    answer = "Ask again later"
  elif random_number == 6:
    answer = "Better not tell you now"
  elif random_number == 7:
    answer = "My sources say no"
  elif random_number == 8:
    answer = "Outlook not so good"
  elif random_number == 9:
    answer = "Very doubtful"
  elif random_number == 10:
    answer = "No way"
  elif random_number == 11:
    answer = "Absolutely"
  else:
    answer = "Error"

  #if name is blank, update the format to just output the question and answer
  if name == "":
    print(f"Question: {question}")
    print(f"Magic 8-Ball's answer: {answer}.")
  else:
    #otherwise, incorporate the user's name into the output message
    print(f"{name} asks: {question}")
    print(f"Magic 8-Ball's answer: {answer}.")
