realpassword = 'a123456'
x = 3
while x >= 0:
	inputpassword = input('請輸入密碼: ')
	x = x - 1
	if inputpassword != realpassword:
		print('密碼錯誤!還有 ', x ,'次機會')
	else:
		print('登入成功')
		break
	
