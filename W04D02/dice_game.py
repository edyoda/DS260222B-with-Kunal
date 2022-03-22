import random as rn

choice = input("Enter the choice Yes/No:")
dice = list(range(1,7))

while choice.lower() == "yes":
	 print(f"{rn.choice(dice)} is your dice number")
	 choice = input("Enter the choice Yes/No:")