import random,sys
print("I am thinking of a number from 1 to 30.")
secretNumber = random.randint(1,30)
guessesTaken = 0
while guessesTaken < 6:
	print("Type in a guess and press enter:")
	guess = input()
	guess = int(guess)
	guessesTaken = guessesTaken + 1
	if guess < secretNumber:
		print('Too Small!')
	if guess > secretNumber:
		print('Too Big!')
	if guess == secretNumber:
		print("You have guessed my number in " + str(guessesTaken)+"tries" + " The Number is: "+ str(secretNumber))
		sys.exit()
print("Nope!! my number was" +" " + str(secretNumber))
