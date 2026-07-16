n=int(input("Enter a number:"))
factorial=1
for i in range(1,n+1):
    if (i==0):
        factorial=1
    factorial=factorial*i
print("Factorial of",n,"is",factorial)
