from nltk import pos_tag

def compareBigramTypes (st1,  st2,  normalization):
    a=(getBIPOS(st1))
    b=(getBIPOS(st2))
    #as we are removing some elements lenth is calculated before
    a1,b1=len(st1)-st1.count(' '),len(st2)-st2.count(' ') # spaces are removed
    simi=0 #similar words
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

st1=input("Enter String 1: ")
st2=input("Enter String 2: ")
nor=input("Is this normalization - y/n: ")
#all strings are turned into lower case
print(compareBigramTypes(st1.lower(),st2.lower(), nor.lower()))