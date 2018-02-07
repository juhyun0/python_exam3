#bool 자료형
a=3>2
print(a)
a=2>3
print(a)
type(a)

print("")

print(not 'ABC') # 비어있지 않은 문자열을부정
print(not '') # 빈 문자열을 부정
print(not(1,2,3)) # 비어있지 않은 튜플을 부정
print(not ()) # 빈 튜플을 부정
print(not []) # 빈 리스트를 부정
print(not {}) # 빈 딕셔너리를 부정

print("")

print(True and True) #AND
print(True and False)

print("")

print(False or False)#OR
print(True or False)

print("")
	
print(bool(False))
print(bool(()))
