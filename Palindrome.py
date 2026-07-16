#Palindrome number
n=int(input("Enter a number"))
rev=0
original=n      #Stored the original value first because in loop .. the value of n ends out at 0 .. which will always give false for even a palindrome no. 
print(original)
while n>0:
    mod=n%10
    print(mod)
    n=n//10
    print(n)
    rev=(rev*10)+mod
print("The reversed number is:",rev)
if rev==original:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
