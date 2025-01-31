from nltk import pos_tag

def compareWordTypes (st1,  st2,  normalization):
    a=(getPOS(st1))
    b=(getPOS(st2))
    #as we are removing some elements length is calculated before
    a1,b1=len(a),len(b)
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

def getPOS(st):
    p=st.split()
    q=pos_tag(p)
    return(q)

st1=input("Enter String 1: ")
st2=input("Enter String 2: ")
nor=input("Is this normalization - y/n: ")
#all strings are turned into lower case
print(compareWordTypes(st1.lower(),st2.lower(), nor.lower()))