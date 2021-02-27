
for i in range(1,101):
	is_search7 = False
	if (i%7) == 0:
		continue
	else:
		temp = i
		k = temp // 10
		while k > 0:
			if (temp%10) == 7:
				is_search7=True
				break
			k=temp = temp // 10
	if is_search7 == True:
		continue
	print(i)
		
				
