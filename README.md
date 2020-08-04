A chatbot created using with the help of tensorflow, incorporating an
Encoder - Decoder model ( RNN ) with bahdanau attention and GRU's



Files Description : 

1) Neural machine traslation model  - 
NMT.ipynb

2) Dataset - 
cornell_movie_dialogs_corpus

3) Trained model Checkpoints - 
training_checkpoints
training_checkpoints1
   
4) PreProcessing of Data  - 
bagofwords.py
combining.py
conversations.py
conversations.pickle
dummy.py ( To View processed Data )

5) Feature Creation - 
Features.py ( Creating features and labels as storing in pickle format )


The machine translation jupyter notebook can be trained for higher epochs to gain better accuracy , 
or pretrained (100 epochs) can be used to see the results.
The NMT.ipynb contains the model and a translator function in the end , which takes in a sentance as an
input and returns what the model thinks the reply should be

   
