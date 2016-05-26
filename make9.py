# Author : Sanford Ren
# Date : March 13th 2016

import random

ready = raw_input("Enter ready when you're ready: ")
ready = ready.lower()
score = 0

if ready == "ready":
	print("\n Instructions: Try to get as close to 9 points as possible without going over. \
You will start with 0 points and be asked if you would like more points. Type 'y' to receive more points or 'n' to stop receiving them. \n")
	choice = "y"
	
	
	while score < 9.0 and choice == "y":
		choice = raw_input("Your score is {}. Do you want more points? ".format(score))
		choice = choice.lower()
		if choice == "y":
			score += random.uniform(0.0, 3.0)
		elif choice == "n":
			print("Your final score is {}. Nice.".format(score))


if score > 9.0:
	print("You lose")
	print("You score was {}.".format(score))

if ready != "ready":
		print("Aww, why don't you want to play?")

