import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()



ignore_words=['are','is','am','were','i','he','she','it']
neg_words=['dont','no','not','neith','nor',"don't"]

def checkNeg(words):
    for i in words:
        if i in neg_words:
            return True
    return False            

def Neg_PosSentences(entered_line):
    #list of words in sentences
    word_list=nltk.word_tokenize(entered_line)
    #removing ignore words from the lists
    words = [stemmer.stem(i.lower()) for i in word_list if i.lower() not in ignore_words]
    if(checkNeg(words)):
        #excludeSym(words)
    else:
        #includeSym(words)

    
    
entered_line=raw_input()
#the entered line is negative or positive
Neg_PosSentences(entered_line)
    


