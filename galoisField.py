def galoisFieldValue(n):
	if n == 0:
		value = 1
	else:
		value = galoisFieldValue(n - 1) * 2
		# if value > 255:
		# 	return value
	if value > 255:
		value = value ^ 285
	return value

def galoisSum(a,b):
	return a^b


def galoisFieldValueInverse(value):
	n = 0
	gVal = pow(2, n)
	while gVal != value:
		n += 1
		gVal = galoisFieldValue(n)
	return n