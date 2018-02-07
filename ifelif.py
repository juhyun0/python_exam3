print('과목 1 : ')
n1=int(input())
print('과목 2 : ')
n2=int(input())

if (0<n1 and n1<=100)and(0<n2 and n2<=100):
	n3=(n1+n2)/2
	print("평균 : ")
	print(n3)

	if (n3>=90):
		print('A')
	elif (n3>=80):
		print('B')
	elif (n3>=70):
		print('C')
	else:
		print('F')
else:
	print('계산할 수 없는 숫자 입니다.')
