import random
a=random.randint(1,9)
b=int(input("enter a number"))
if(b<a):
    print(a)
    print("guess is too low")
elif(b>a):
    print(a)
    print("guess is to high")
else:
    print("you are right")
