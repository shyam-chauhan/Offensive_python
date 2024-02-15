def gcd(num1,num2):
    if(num1==num2):
        return num1
    elif(num1 > num2):
        return gcd(num1-num2,num2)
    else:
        return gcd(num2-num1,num1)

x = gcd(8,2)
print(x)