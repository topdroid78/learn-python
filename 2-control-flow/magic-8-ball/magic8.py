#Setting up
name = "Alex"
question = "Will I win the lottery ?"
answer = ""

#Generating a random number

import random

random_number = random.randint(1, 12)


#print(random_number)

#Control Flow

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."  
elif random_number == 5:
  answer = "Better not tell you now."  
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."    
elif random_number == 9:
  answer ="Very doubtful." 
elif random_number == 10:
  answer ="I am not sure"
elif random_number == 11:
  answer ="It is a mistery" 
elif random_number == 12:
  answer ="Ask Obama"            
else :
  answer = "Error"


#Seeing the result

if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  if name == "":
    print("Question: " + question)
  else:
    print(name + " asks: " + question )
  
  print("Magic 8-Ball's answer: " + answer)    
