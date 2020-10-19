l=[]
m=0
s1=""
al="qwertyuioplkjhgfdsazxcvbnm "
string=input("enter a word or a phrase")
for c in string:
    m=m+1
j=m*" _"

for c in string:
    if c not in al:
        print("not allowed")
    

print(j)
char=input("enter a character")
a=string.count(char)
print("number of times",a)
while True:
    s=""
    if char not in al:
        print("not allowed")
    if char in string:
        print("charachter exist")
    else:
        print("character dosent exist")
    for c in string:
        if(c==char):
            s +=c
        else:
            s +=" -"
    print(s)
    if(len(string)==(len(s))):
              break
    char=input("enter a character")
    a=string.count(char)
    print("number of times",a)
    
    




        
