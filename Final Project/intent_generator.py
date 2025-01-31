from nltk.tokenize import TreebankWordTokenizer
import json
import sys
from lexrank import STOPWORDS, LexRank
from path import Path

f=open(sys.argv[1])
token = TreebankWordTokenizer()
s=[]
temp_dict={}
resp=""
flag=0
prev_line_count = 10
document = []
for lines in f:
    result = token.tokenize(lines)
    if (len(result)<=3) and prev_line_count>3 and len(result)>0:
        if flag!=0:
            temp_dict["responses"]=[]
            lxr = LexRank(document, stopwords=STOPWORDS['en'])
            summary = lxr.get_summary(document, summary_size=2, threshold=.1)
            print(summary)
            temp_dict["responses"].append(summary)
            s.append(temp_dict)
            resp=""
            flag=0
        temp_dict=dict(tag= lines[:-1].strip(" "), patterns= [])
        temp_dict["patterns"].append(lines[:-1].strip(" "))
        temp_dict["patterns"].append("how to "+lines[:-1].strip(" "))
    else:
        #resp+=lines.strip(" ")
        document.append(str(lines.strip(" ").encode('utf-8')))
        flag+=1 
    prev_line_count = len(result)

n_dict = {
    "intents":[
        {"tag": "greeting",
         "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day"],
         "responses": ["Hello, thanks for visiting", "Good to see you again", "Hi there, how can I help?"],
         "context_set": ""
        },
        {"tag": "goodbye",
         "patterns": ["Bye", "See you later", "Goodbye"],
         "responses": ["See you later, thanks for visiting", "Have a nice day", "Bye! Come back again soon."]
        },
        {"tag": "thanks",
         "patterns": ["Thanks", "Thank you", "That's helpful"],
         "responses": ["Happy to help!", "Any time!", "My pleasure"]
        }
    ]
}

for i in s:
    n_dict["intents"].append(i)
json_obj = json.dumps(n_dict,indent=4)
json_obj_mod = json.loads(json_obj)
with open (sys.argv[2],"w") as out:
    out.write(json_obj)

