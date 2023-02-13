str1=input()
num1=0
for i in range (len(str1)-1):
    if str1[num1+1]=="=":
        str1 = str1.replace("=", "",1)
        str1 = str1.replace(str1[num1], "", 1)
        num1-=1
    else:
        num1+=1
print(str1)