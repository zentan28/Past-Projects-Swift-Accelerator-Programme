#importing libraries & modules
import random

#functions
def read_questions(file_name):
  """
  Reads the questions from the file and returns a list of dictionaries, 
  containing the question and its answer.

  For example:

  It turns: 
  What color is the sunset on Mars?
  A: Red
  B: Pink
  C: Blue*

  Into a dict: 
  question = {
    "question": "What color is the sunset on Mars?",
    "options" : {A: Red, B: Pink, C: Blue},
    "ans": "c",
  }

  It appends the indvidual question into a list of questions and returns that list. 
  """
  
  questions = []

  with open(file_name, 'r') as file:
    lines = file.readlines()

  for i in range(0, len(lines),
                 5):  #loop through each question that have 5 lines
    problem_statement = lines[i].strip() #get problem statement and remove whitespaces
    options = {}
    correct_answer = None

    for j in range(i + 1, i + 4):  #read the options
      option = lines[j].split(
          ":")  #option is now a list of 2 elements, ["A", " Red"]
      key = option[0].strip()
      value = option[1].strip()

      #the correct answer have a "*" behind it
      if value[-1] == "*":
        correct_answer = key
        value = value[0:-1] #removes the "*"

      options[key] = value

      question = {
          "question": problem_statement,
          "options": options,
          "ans": correct_answer
      }

    questions.append(question)

  return questions


def trivia_game(no_of_questions, max_wrong_cnt):
  """
  This function takes in the number of questions to be asked and 
  the maximum number of wrong answers allowed. 

  Then, it procedes to ask the questions and check the answers. 

  If the user gets the answer wrong, it will ask the user to try again. 
  But if the user gets the maximum allowed number of wrong ans, 
  the game will end. 

  After each question, the user will also have a chance to quit the game. 
  """

  print("Game Starts!\n")

  wrong_cnt = 0
  #max_wrong_cnt = 3
  #no_of_questions = 5
  score = 0

  random_questions = random.sample(questions, no_of_questions)

  #which question are we at? 
  question_number = 0

  for question in random_questions:
    question_number += 1
    
    #print scoring
    print("Current Score: ", score, "\t", "Wrong Answers: ", wrong_cnt, "/",
          max_wrong_cnt, "\n")

    #showing the question
    print(question["question"])
    print("A: ", question["options"]["A"])
    print("B: ", question["options"]["B"])
    print("C: ", question["options"]["C"])

    #getting ans from user
    ans = input("Enter your answer: ")
    print()  #new line

    #check ans and responses
    if ans == question["ans"] or ans == question["ans"].lower():  #if correct,
      #(accpets both upper and lower case)
      score += 100
      print("You are CORRECT! \nScore + 100! \n")

    else:  #if wrong
      print("WRONG!")
      input()
      print("The correct answer is: ", question["ans"], "\n")
      score -= 25
      wrong_cnt += 1

    if wrong_cnt == max_wrong_cnt:  #reached max wrong answers
      print("You have reached the maximum number of wrong answers. \n"
            "Game Over (╥﹏╥)")
      break

    if question_number < no_of_questions:  #last question don't need these anymore
      print("Do you want to continue the game? (y/n)")
      choice = input()
      if (choice == 'n'):
        break
      else:
        print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯" * 2, "\n")
        print("Next_question: \n")

  #every game when it ends, prints this:
  print("\n")
  print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯" * 2)
  print("Thank you for playing!")
  print("Final Score: ", score)
  print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯" * 2, "\n")



#start of main code
questions = []
questions = read_questions("questions.txt")

#play trivia_game of 5 questions with 3 max wrong ans
trivia_game(5, 3)





#another game idea for next time
"""
3 Letter Word Game

power move: 
reduces to 1 try: 
example sentence, 
definition,  
translation, 

get list of word: (10 tries)

"""