driving =  input("你有沒有開過車?:")
if driving != "有" and driving != "沒有" :
	print("只能輸入有或沒有")
	raise SystemExit
age = input("請問你今年幾歲?:")
age = int(age)
if driving == "有" :
	if age >= 18 :
		print("你通過測驗")
	else :
		print("你還未成年，怎麼會開過車")
elif driving == "沒有" :
	if age >= 18 :
		print("你已經可以考駕照，怎麼還不去考")
	else :
		print("很好，再過幾年就可以考了")