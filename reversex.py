#Reverse a number
n=int(input("Enter a number"))
rev=0
while n>0: 
    mod=n%10    #modulus with 10 basically gives the last digit of the no.in remainder that is divided by 10 . So first we extracted the last digit
    print(mod)
    n=n//10 #Floor div because it removes the after decimal part (the last value). And we have already extracted it ie. mod=6(for the first iteration).. so in order to work the same with other numbers .. we have to remove the last extracted value
    print(n)
    rev=(rev*10)+mod #multiplied by 10 .. rev=4(before), now we need to make space for the next no. as well and then a space(0) is made for the next no. then we add the next no. to curr rev and it gives the reverse acc.. Because if we directly added the next mod val then it would not give the desired o/p
    #print(rev)
print("The reversed number is:",rev)