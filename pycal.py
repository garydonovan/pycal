# simple Python calculator in using basic operators /,*,+,-

# returns the sum of num1 and num2
def add(num1, num2):
	return num1 + num2

# returns the result of subtracting num1 - num2
def sub(num1, num2):
	return num1 - num2

# returns the result of multiplying  num1 * num2
def mul(num1, num2):
	return num1 * num2

# returns the result of dividing num1 / num2
def div(num1, num2):
	return num1 / num2

# Main function 

def main():
	operation = input("What do you want to do? (/,*,+,-): ")
	if (operation != '+' and operation != '-' and operation '*' and operation != '/'):
		#invalid operation
		print ("you must enter a valid operation")
	else
	var1 = int(input("Enter num1"))
	var2 = int(input("Enter num2"))
	if(operation == "+"):
		print (add(var1, var2))
	elif(operation == "-"):
		print (sub(var1, var2))
	elif(operation == "/"):
		print (div(var1, var2))
	else:
		print (mul(var1, var2))

main()