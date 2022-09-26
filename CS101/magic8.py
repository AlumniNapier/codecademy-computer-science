#importation random
import random
#variables 
random_number = random.randint(1, 9)
question_user = "Would I be rich ?"
name_user = "Steve"
ball_answer = ""
#control for random number with answer assignation 
if random_number == 1:
	ball_answer = "Yes - definitely."
elif random_number == 2:
	ball_answer = "It is decidedly so."
elif random_number == 3:
	ball_answer = "Without a doubt."
elif random_number == 4:
	ball_answer = "Reply hazy, try again."
elif random_number == 5:
	ball_answer = "Ask again later."
elif random_number == 6:
	ball_answer = "Better not tell you now."
elif random_number == 7:
	ball_answer = "My sources say no."
elif random_number == 8:
	ball_answer = "Outlook not so good."
else: 
	ball_answer = "Very doubtful."
#output control 
if question_user and name_user:
	print(name_user, "asks: ", question_user)
elif question_user and not name_user:
	print("Your question is: ", question_user)
if question_user and name_user:
	print("Magic 8-Ball's answer: " + ball_answer)
elif question_user and not name_user:
	print("Magic 8-Ball's answer: " + ball_answer)
elif not question_user and name_user: 
	print("The Magic 8-Ball's can't answer you, if you don't ask her a question. Please retry again " + name_user + ".")
else: 
	print("You don't have a question ?")


#by Isaac LOTFI aka Sayf ;)  
