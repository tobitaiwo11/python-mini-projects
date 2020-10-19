import random
while True:
    print("do you want a password(y/n) ")
    ch=input("y or n")
    if(ch=="y"):
        print("what type of password do you want")
        a="qwertyuioplkjhgfdsazxcvbnm"
        b="QWERTYUIOPLKJHGFDSAZXCVBNM"
        c="!@#$%^&*()_-+\}{][|"
        c1=str(c)
        s=""
        c=0
        r=random.randint(0,25)
        r0=random.randint(0,25)
        r2=random.randint(0,19)
        r3=random.randint(0,25)
        r4=random.randint(0,25)
        r5=random.randint(0,25)
        r6=random.randint(0,25)
        r7=random.randint(0,25)
        r8=random.randint(0,25)
        s=s+b[r0]+a[r]+a[r3]+a[r4]+a[r5]+a[r6]+a[r7]+a[r8]+c1[r2]
    if(ch=="n"):
        break
    print(s)
#add a choice:password is strong or weak
#password shold not have duplicate characters
    

            

