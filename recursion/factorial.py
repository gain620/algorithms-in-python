def factorial(num):
    if num <= 1:
    	if num < 0:
    		return 'Can not take negative number!'
    	elif num == 0:
    		return 1
    	else:
        	return num
    else:
        return num * factorial(num - 1)

print('factorial(5)=', factorial(5))
print('factorial(-2)=', factorial(-2))
print('factorial(0)=', factorial(0))
print('factorial(998)=', factorial(998))