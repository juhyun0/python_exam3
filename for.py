print('숫자를 입력하세요')
num=int(input())

for i in range(1,10):
	print("{0} * {1} = {2}".format(num, i, num*i) )

print("")

dic={'애플': 'www.apple.com', '파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com'}
for k, v in dic.items():
	print("{0} : {1}".format(k,v))
