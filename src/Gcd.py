def gcd(num1, num2):
	if(num1 < num2):
		return gcd(num2, num1)

	# Declare a dynamically sized array
	array = []

	# Add the first two elements to the list
	array.append(num1)
	array.append(num2)

	i = 1

	# Calculate while next divisor is not 0
	while array[i] != 0:
		array.append(array[i-1] % array[i])
		i = i + 1

	# Return last calculated element which is greatest common divisor
	return array[i-1]

def dynGcd(num1, num2):
	while num2 != 0:
		temp = num2
		num2 = num1 % num2
		num1 = temp	
	return num1

def recGcd(num1, num2):
	if num2 == 0:
		return num1
	else:
		return recGcd(num2, num1 % num2)

def inverseGcd(num, mod):
	remainders = []
	#uselessArray = []
	inverses = []

	remainders.append(mod)
	remainders.append(num)

	#uselessArray.append(1)
	#uselessArray.append(0)
	inverses.append(0)
	inverses.append(1)
	i = 1

	while remainders[i] != 0:
		divisor = remainders[i-1] / remainders[i]
		remainder = remainders[i-1] - divisor * remainders[i]
		inverse = inverses[i-1] - divisor * inverses[i]

		remainders.append(remainder)
		#uselessArray.append(uselessArray[i-1] - divisor * uselessArray[i])
		inverses.append(inverse)
		i = i + 1

	# End while loop (remainders[i] == 0)
	result = inverses[i-1]
	if(result < 0):
		return result + mod
	else:
		return result


# Testing

x = gcd(100, 22)
print x

x = dynGcd(100, 22)
print x

x = recGcd(100, 22)
print x

x = inverseGcd(5,17)
print x