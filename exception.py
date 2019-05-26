def getint(message):
	while True:
		try:
			number = int(input(message))
			return number
		except ValueError:
			print("Invalid number entered")

num1 = getint("Enter First Number:")
num2 = getint("Enter Second Number:")

try:
	print("{} divided by {} is {}".format(num1, num2, num1/num2))
except ZeroDivisionError:
	print("You cant divide by Zero:")