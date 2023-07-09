M = input("Enter your password: ")
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_#%^&*()[\]{}|;:></?"
digits="0123456789"
count={}
p=0
q=0
r=0
s=0
if (len(M) >= 10):
    for i in M:
        if (i in smallalphabets):
            p+=1
        elif (i in capitalalphabets):
            q+=1
        elif (i in digits):
            r+=1
        elif(i in specialchar):
            s+=1
if (p>=1 and q>=1 and r>=1 and s>=1 and p+q+r+s==len(M)):
    print("Valid Password")
    print("small alphabets are : ",p)
    print("capital alphabets are : ",q)
    print("digits are : ",r)
    print("special characters are : ",s)
    for j in M:
        if j in count:
            count[j]+=1
        else:
            count[j]=1
    print("count : ", count)
else:
    print("Invalid Password")



