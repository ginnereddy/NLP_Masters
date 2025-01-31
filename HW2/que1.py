import nltk

file=open("input3.txt",'r')
Lines = file.readlines()
a=[]
for i in range(len(Lines)):
    if Lines[i]=="Ingredients\n":
        while(True):
            i+=1
            if "Instructions" in Lines[i]:
                break
            elif Lines[i]=="\n":
                continue
            a.append(Lines[i])

for i in a:
    words=nltk.word_tokenize(i)
    tagged=nltk.pos_tag(words)
    chunkGram= r""" NP: {<CD>{1,2}<JJ>?<NN.?><IN>?<VB.?>*<JJ>*<NN.?>*} """
    chunkParser=nltk.RegexpParser(chunkGram)
    chunked=chunkParser.parse(tagged)
    chunked.draw()

file.close()