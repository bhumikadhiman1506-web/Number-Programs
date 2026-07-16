#Armstrong number
n=input("Enter a number")
count=len(n)
digit=0
original=int(n)
for i in n:
    square=pow(int(i),count)
    print(square)
    digit+=square
    print(digit)
if digit==original:
    print(" As the input number,",original,"=","the sum of their count of powers,",digit,"  so the number is an armstrong number")
else:
    print("The number is not an armstrong number")
