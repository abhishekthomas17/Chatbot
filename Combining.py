import pickle

with open('connections.pickle', 'rb') as handle:
    con = pickle.load(handle)

with open('words.pickle', 'rb') as handle:
    all_words = pickle.load(handle)


count=0
new={}
with open('cornell_movie_dialogs_corpus\\cornell movie-dialogs corpus\\movie_lines.txt','r') as file:
    for sent in file:
        a=sent.split(" +++$+++ ")
        count=count+1
        if count==50000:
            print("done")
            count=0
        for i in con:
            nlist=con[i]
            for j in con[i]:
                if j == a[0]:
                    b=a[4]
                    b=b.replace('\n','')
                    b=b.replace('---',',')
                    b=b.replace('--',',')
                    nlist=[b if x==j else x for x in nlist]
                    con[i]=nlist


print("done")

with open('conversations1.pickle','wb') as f:
    pickle.dump(con,f,protocol=pickle.HIGHEST_PROTOCOL)
    
print("done")
