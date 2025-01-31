from nltk.sem.logic import *
import os

file1=os.getcwd()+'/file.txt'
f1=open(file1,"r")
st1=f1.readlines()
a=[]
for line in st1:
    a.append(line)

read_expr = Expression.fromstring

x1=read_expr(a[0]).simplyfy()
x2=read_expr(a[1]).simplyfy()

print(x1==x2)