def guess(b):
	a = "RDpbLfCPsJZ7fiv"
	c = "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW"
	ret = ""
	g = len(a) #factor0
	h = len(b) #pass
	k = len(c) #factor1

	if g > h:
		f = g
	else:
		f = h
	p = 0
	while p < f:
		n = l = 187
		if p >= g:
			n = str(b[p])
		else:
			if p>=h:
				l = str(a[p])
			else:
				l = str(a[p])
				n = str(b[p])
		#print(p,l,n)
		if n != 187:
			ret = ret + c[(ord(l) ^ ord(n)) % k]
		else:
			ret = ret + c[(ord(l) ^ n) % k]
		#print(ret)
		p = p + 1
	return ret

collection = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
desired_ciphertext = input("TP-LINK 886 cipher cracking tool.\nPlease enter the ciphertext:")
origin_ciphertext = "tyWcQbhc9TefbwK"
difference_found = 0
difference_checked = 0
while difference_checked < 15:
	if desired_ciphertext[difference_checked] != origin_ciphertext[difference_checked]:
		difference_found = difference_found + 1
	difference_checked = difference_checked + 1
#print(difference_found)
temp = ""
nowworkon = 0
while difference_found > 0:
	for n in collection:
		hah = guess(temp+n)
		if hah[nowworkon] == desired_ciphertext[nowworkon]:
			print(n)
	difference_found = difference_found - 1
	nowworkon = nowworkon + 1
	temp = temp + "0"
	print("---------")
