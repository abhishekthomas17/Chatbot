import pickle
from nltk.tokenize import word_tokenize

with open('features.pickle', 'rb') as handle:
    all_words = pickle.load(handle)


with open('labels.pickle', 'rb') as handle:
    all_words1 = pickle.load(handle)


##for i in all_words:
##    print(i)

print(len(all_words),len(all_words1))

print(all_words[0],all_words1[1],word_tokenize(all_words1[1]))

##with open('words2.pickle', 'rb') as handle:
##    words = pickle.load(handle)
##
##words=set(words)
##
##with open('words.pickle','wb') as f:
##    pickle.dump(words,f,protocol=pickle.HIGHEST_PROTOCOL)
##    
##for i in all_words:
##    nlist=[]
##    for j in all_words[i]:
##        nlist.append(j.lower())
##    all_words[i]=nlist
##        
##
####for i in range(0,len(all_words)):
####    print("FIRST ",all_words1[i],"\n SECOND",all_words[i])
##
##with open('conversations2.pickle','wb') as f:
##    pickle.dump(all_words,f,protocol=pickle.HIGHEST_PROTOCOL)
