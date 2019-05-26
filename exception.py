def division(a, b):
	c=a/b
	print("{} divide by {} is:{}".format(a,b,c))

num1 = int(input("ENTER FIRST NUMBER:"))
num2 = int(input("ENTER SECOND NUMBER:"))
try:
	division(num1,num2)

except ZeroDivisionError:
	print("ERR")
print("Progam terminated")