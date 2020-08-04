import pickle

with open('cornell_movie_dialogs_corpus\\cornell movie-dialogs corpus\\movie_conversations.txt','r') as file:
    i=0
    con={}
    for f in file:
        i=i+1
        a=f.split(" +++$+++ ")
        b=a[3]
        b=b.replace('[','')
        b=b.replace(']','')
        b=b.replace(' ','')
        b=b.replace("'","")
        b=b.replace('\n','')
        c=b.split(",")
        con[i]=c
        print(con[i])
    
with open('connections.pickle','wb') as f:
    pickle.dump(con,f,protocol=pickle.HIGHEST_PROTOCOL)
