print "Hi, I'm Shasekh!  Let's play 3 games of Rock Paper Scissors!"

from random import choice
def function(input1, computer_score, human_score):
	x = choice("rps")
	if move == "r" and x == "r":
		print "My move is rock."
		print "It's a tie!"
		return computer_score, human_score
	elif move == "r" and x == "p":
		print "My move is paper."
		print "I won! Good job!"
		return computer_score, human_score + 1
	elif move == "r" and x == "s":
		print "My move is scissors."
		print "You won! Good job!"
		return computer_score, human_score + 1
	elif move == "p" and x == "r":
		print "My move is rock."
		print "You won!"
		return computer_score + 1, human_score
	elif move == "p" and x == "p":
		print "My move is paper."
		print "It's a tie!"
		return computer_score, human_score
	elif move == "p" and x == "s":
		print "My move is scissors."
		print "I won!"
		return computer_score + 1, human_score
	elif move == "s" and x == "r":
		print "My move is rock."
		print "I won!"
		return computer_score + 1, human_score
	elif move == "s" and x == "p":
		print "My move is paper."
		print "You won! Good job!"
		return computer_score, human_score + 1
	elif move == "s" and x == "s":
		print "My move is scissors."
		print "It's a tie!"
		return computer_score, human_score
	else:
		print "Sorry, you didn't write r, p, or s, so I didn't understand that."

x = 0
y = 0
#Kristain, Jenni, and Trinity saved my life today.  Anna was my partner but for the most part we worked individually.
	
move = raw_input("Make your move. Write r, p, or s; or q to quit.")
while move != "q":
	x, y = function(move, x, y)
	move = raw_input("Make your move. Write r, p, or s; or q to quit.")

print "Final Score is Shasekh: %d, You: %d" % (x, y)
print "Good Game!"
