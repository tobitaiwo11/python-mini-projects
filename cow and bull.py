import random
print("cows and bulls")
string=""
a=random.randint(0,9)
s=str(a)
string=string+s
a2=random.randint(0,9)
s1=str(a2)
string=string+s1
a3=random.randint(0,9)
s2=str(a3)
string=string+s2
a4=random.randint(0,9)
s3=str(a4)
string=string+s3
i=int(string)
user=int(input("enter your number"))
n=str(user)
bull=0
cow=0
if(s==n[0]):
    cow=cow+1
else:
    bull=bull+1
if(s1==n[1]):
    cow=cow+1
else:
    bull=bull+1
if(s2==n[2]):
    cow=cow+1
else:
    bull=bull+1
if(s3==n[3]):
    cow=cow+1
else:
    bull=bull+1

print(i)
print("cow:",cow,"bull:",bull)

