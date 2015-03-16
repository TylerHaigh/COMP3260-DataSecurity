def fastExp(number, exponent, modVal):
	# Make copies of argumrents
	num = number
	exp = exponent
	result = 1

	# Loop the number of times to raise to exponent
	while exp != 0:
		
		# Check if exponent is even and can be halved
		while exp % 2 == 0:
			exp = exp / 2

			# Exponent was even so we can square the number

			# Update the base number by taking the
			# Square of the number and taking the modulus
			num = (num * num) % modVal

		# Exponent is now odd. We cannot square the number

		# Remove one from the exponent that we just did
		exp = exp - 1

		# Update the result
		result = (result * num) % modVal

	return result

# Testing
x = fastExp(5,117,19)
print x