num=0

while True:
	print('숫자를 입력하세요 : ')
	num2=int(input())
	
	if (num2<0):
		break

	num=num+num2
	print("현재까지 합 {0}".format(num))
	

