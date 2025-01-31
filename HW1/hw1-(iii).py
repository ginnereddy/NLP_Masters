import os
from nltk import pos_tag

def plagiarismDetector ( file1, file2, Type, nor, t ):
    st1=file1.read()
    st2=file2.read()
    result=0
    if(Type == 'u'):
        result=compareWordTypes(st1,st2,nor)
        print("Output is:",result)
    elif(Type == 'b'):
        result=compareBigramTypes(st1,st2,nor)
        print("Output is:",result)
    else:
        print("Given type is invalid")
    if(result>=t):
        return("Plagiarized Text")
    elif(result<t):
        return("Non plagiarized text")

    
def compareWordTypes (st1,  st2,  normalization):
    a=(getPOS(st1))
    b=(getPOS(st2))
    #as we are removing some elements lenth is calculated before
    a1,b1=len(a),len(b)
    simi=0
    for i in a:
        for j in b:
            if(i==j):
                simi+=1
                #removing the common element in 2nd set so that when 2 words match with one word, only 1 common is taken
                b.remove(j)
                break
    if(normalization=='y'):
        return(simi/((a1+b1)/2))
    elif (normalization=='n'):
        return(simi)
    else:
        return("Invalid entry for normalization")

def getPOS(st):
    p=st.split()
    q=pos_tag(p)
    return(q)

def compareBigramTypes (st1,  st2,  normalization):
    a=(getBIPOS(st1))
    b=(getBIPOS(st2))
    #as we are removing some elements lenth is calculated before
    a1,b1=len(st1)-st1.count(' '),len(st2)-st2.count(' ') # spaces are removed
    simi=0
    for i in a:
        for j in b:
            if(i==j):
                simi+=1
                #removing the common element in 2nd set so that when 2 words match with one word, only 1 common is taken
                b.remove(j)
                break
    if(normalization=='y'):
        return(simi/((a1+b1)/2))
    elif (normalization=='n'):
        return(simi)
    else:
        return("Invalid entry for normalization")

def getBIPOS(st):
    p=st.split()
    #oneword POS tagging
    q=pos_tag(p)
    #biword POS tagging
    q2=[]
    for i in range(len(q)-1):
        temp=q[i]+q[i+1]
        q2.append(temp)
    return(q2)


file1=os.getcwd()+'/example4file1.txt'
file2=os.getcwd()+'/example4file2.txt'
f1=open(file1,"r")
f2=open(file2,"r")
nor=input("Is this normalization - y/n: ")
Type=input("Please choose the type.\nU/u for unigram B/b for bigram: ")
t=float(input("Enter a Threshold value: "))
#all strings are turned into lower case
print(plagiarismDetector ( f1, f2, Type.lower(), nor.lower(), t ))
f1.close()
f2.close()
