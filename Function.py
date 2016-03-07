import random

def flip_coin():

	""" Simulates a coin flip. Returns a string of either "Heads" or "Tails". """
	
	number = random.randint(0,1)
	if number == 0:
		coin = 'Heads"
	else:
		coin = 'Tails'
		
	# Sends the coin value back to the main progrma	
	return coin
	
	#### Main Program Starts Here ####

print ("Let's simulate a coin flip. ")

HeadsOrTails = flip_coin()

print ("the coin is {}. " .format(HeadsOrTails)