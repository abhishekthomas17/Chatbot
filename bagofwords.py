from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tokenize import TweetTokenizer
import pickle
from nltk.corpus import words


tk=TweetTokenizer()
words1=[]
with open('cornell_movie_dialogs_corpus\\cornell movie-dialogs corpus\\movie_lines.txt','r') as file:
    for f in file:
        a=f.split(" +++$+++ ")
        b=a[4]
        b=b.replace("\n","")
        b=b.replace('---',' ')
        b=b.replace('--',' ')
        b=b.replace('-',' ')
        b=b.replace('...',' ')
        b=b.replace('..',' ')
        b=b.replace('....',' ')
        for i in tk.tokenize(b):
            words1.append(i)

print("done")
unique_words1=set(words1)

fin_words=[]
for i in unique_words1:
    if len(i) < 4:
        if i.lower() in words.words():
            fin_words.append(i.lower())
    else:
        if i.lower() in words.words():
            fin_words.append(i.lower())
    
print(len(unique_words1))

with open('words1.pickle','wb') as f:
    pickle.dump(fin_words,f,protocol=pickle.HIGHEST_PROTOCOL)

print("done")
