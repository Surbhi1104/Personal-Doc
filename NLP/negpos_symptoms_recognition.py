import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import RegexpStemmer
stemmer = RegexpStemmer('ing$|s$|e$|able$')

#stemmer = LancasterStemmer()
ignore_words=['are','is','am','were','i','he','she','it','you','your','yours','we','they','them','me','mine','hers','her','him','his']

neg_words=['dont','no','not','neith','nor',"don't","donot","can't","cannot","couldnot","couldn't","mustn't","shouldn't"]



def checkNeg(words):
    for p in range(len(words)):
        if words[p]=="n't" or words[p]=="'t":
            words[p-1]=words[p-1]+words[p]
            words[p]=""
    
    for i in words:
        if i in neg_words:

            return True

    return False            



def Neg_PosSentences(entered_line):
    w=nltk.word_tokenize(entered_line)
    for p in range(len(w)):
        if w[p]=="n't" or w[p]=="'t":
            w[p-1]=w[p-1]+w[p]
            w[p]=""

    #list of words in sentences

    #word_list=nltk.word_tokenize(w)
    

    #removing ignore words from the lists

    words = [stemmer.stem(i.lower()) for i in w if i.lower() not in ignore_words]
    
    if(checkNeg(words)):
        if('but' in entered_line):
            r=entered_line.split('but')
            for i in r:
                Neg_PosSentences(i)       
        #excludeSym(words)
    else:
        def process_content(entered_line):
            r=nltk.word_tokenize(entered_line)
            symptoms=[]
            try:
                for i in r:
                    words=nltk.word_tokenize(i)
                    tagged=nltk.pos_tag(words)
                    if(tagged[0][1]=='NN' or tagged[0][1]=='JJ') and (tagged[0][0] not in ignore_words):
                        symptoms.append(tagged[0][0])
                print("Your symptoms are:")
                for i in symptoms:
                    print(stemmer.stem(i.lower()))
            except Exception as e:
                print(str(e))
        process_content(entered_line)

        #includeSym(words)


entered_line=input()

#the entered line is negative or positive

Neg_PosSentences(entered_line)



#POS tagging





