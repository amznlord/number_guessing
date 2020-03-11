import random
import time

#basic info
__author__ = "Jakub Mareš"
__copyright__ = "Copyright 2020, Jakub Mareš"
__contact__ = "instagram: @kubamari"

life = 0
difficulty = 0
range_from = 0
range_to = 0
#aktuální čas v ms
milliseconds = int(round(time.time() * 1000))

#vytvoření seedu pro generátor
random.seed(milliseconds)

print("Vítej, děkuji ji ti za stažení programu :)\n")

print("Zvol si rozsah generovaných čísel\n")
range_from = int(input("od: "))
range_to = int(input("do: "))

#generátor náhodného čísla se seedem aktuálního času v ms
secret_number = random.randint(range_from, range_to)

difficulty = int(input("Zvol si počet životů: "))

while life < difficulty:
	print("Zadejte číslo od", range_from, "do", range_to)
	guess = int(input())

	if guess == secret_number:
		print("Gratulace! Vyhrál jsi.\n")
		break

	elif guess < secret_number:
		print("Trochu přidej!\n")
		life += 1

	else:
		print("Trochu uber!\n")
		life += 1

	if life == difficulty:
		print("Prohrá jsi, ale to se stává. Hledané číslo bylo:", secret_number, "\n")