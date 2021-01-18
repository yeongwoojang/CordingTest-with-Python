# in연산자와 not in 연산자
# X in 리스트 : 리스트 안에 X가 들어 있을 때 True반환
# X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 True반환

# 간단한 조건문

score = 85
if score>=80 : result ="Success";
else : result ="Fail";
print(result)

result = "Success" if score>=80 else "Fail"
print(result)

a= [1,2,3,4,5,5,5,] # list
remove_set = {3,5} #set

# 리스트에서 또 다른 리스트를 생성하는 일반적인 방법
result = []
for i in a :
    if i not in remove_set :
        result.append(i)
print(result)

# 더 간편한 방법
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set] #리스트 컴프리헨션
print(result)
