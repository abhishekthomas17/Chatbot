import pickle
from nltk.tokenize import TweetTokenizer
import gc
import numpy as np
import re
tk=TweetTokenizer()

with open('conversations2.pickle', 'rb') as handle:
    all_words = pickle.load(handle)

with open('words.pickle', 'rb') as handle:
    words = pickle.load(handle)

all_words1=all_words

print(len(all_words1))

print(len(words))


##
##bog=[]
##bog1=[]
##c=0
##noob=[]
##s=[]
##s1=[]
##d=0
##
##for i in all_words:
##    l=len(all_words[i])
##    c=c+1
##    
##    for j in range(0,len(all_words[i])):
##        if j == (len(all_words[i])-1):
##            break
##        else:
##            a=tk.tokenize(all_words1[i][j])
##            for word in words:
##                bog.append(a.count(word))
##            b=tk.tokenize(all_words1[i][j+1])
##            for word in words:
##                bog1.append(b.count(word))
##            s.append(bog)
##            s1.append(c)
##            bog=[]
##            bog1=[]
##    if c == 1000:
##        c=0
##        d=d+1                
##        ##with open('features.pickle', 'rb') as handle:
##        ##    s = pickle.load(handle)
##        ##s.append(bog)
##        with open('featurefolder/features{}.pickle'.format(d),'wb') as f:
##            pickle.dump(s,f,protocol=pickle.HIGHEST_PROTOCOL)
##        s=[]
##        ##
##        ##with open('labels.pickle', 'rb') as handle:
##        ##    s1 = pickle.load(handle)
##        ##s1.append(bog1)
##        with open('featurefolder/labels{}.pickle'.format(d),'wb') as f:
##            pickle.dump(s1,f,protocol=pickle.HIGHEST_PROTOCOL)
##        s1=[]
##        
##    if d==1:
##        break
          
                

def process(w):
    w = w.lower().strip()

    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)

    w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w)

    w = w.rstrip().strip()

    w=w.replace(" ."," ")
    w=w.replace("!"," ")
    w=w.replace("?"," ")
    

    w = '<start> ' + w + ' <end>'
    return w

    

s1=[]
s2=[]

print(len(all_words1))

for i in all_words1:
    
    l=len(all_words1[i])
    for j in range(0,len(all_words1[i])):
        if j == (len(all_words1[i])-1):
            break
        else:
            if(len(tk.tokenize(all_words1[i][j]))>30):
                continue
            elif(len(tk.tokenize(all_words1[i][j+1]))>30):
                continue
            sentance=process(all_words1[i][j])
            sentance1=process(all_words1[i][j+1])

            s1.append(sentance)
            s2.append(sentance1)
            #print(len(sentance))
                
            
print("done")

with open('features.pickle','wb') as f:
    pickle.dump(s1,f,protocol=pickle.HIGHEST_PROTOCOL)
    
with open('labels.pickle','wb') as f:
    pickle.dump(s2,f,protocol=pickle.HIGHEST_PROTOCOL)

print("done")
