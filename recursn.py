def my_recursion(m):
	if (m>=0):
		result = m + my_recursion(m-1)
		print(result)
	else:
		return 0
	return result
print("\noutput:")
my_recursion(4)



i = 1
while i < 6:
        print(i)
        i += 1

















