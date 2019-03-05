import nltk
import random
import string
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import json
with open('document(1).json') as json_data:
    data = json.load(json_data)


class Work1:
    def __init__(self):
        self.greet=True
        self.status=True
        self.diseases = set()
        self.di=data
        
    def SentenceProcessing(self):
        self.sentence = raw_input()
        self.greeting()
        self.checkNeg()
        self.diseases = self.possibleDiseases()
        #print(self.diseases)
        while len(self.diseases)!=1:
            self.askFurther()
            self.sentence = raw_input()
            self.checkNeg()
            if len((self.diseases).intersection(self.possibleDiseases()))==0:
                self.diseases = (self.diseases).union(self.possibleDiseases())
            else:
                self.diseases = (self.diseases).intersection(self.possibleDiseases())
            #print(self.diseases)
        output=list(self.diseases)        
        print("Possible disease is",output[0])
        

    def checkNeg(self):
        neg_words=['dont','no','not','neith','nor',"don't"]
        
        for i in self.sentence.split(" "):
            if i in neg_words:
                self.status=False
                break

    def askFurther(self):
        QUESTIONS=["tell me more about your disease","what has exactly happened to you?","tell me some symptoms of your illness","Tell me more! i will help you",
                   "whats wrong with you my friend?"]
        print(random.choice(QUESTIONS))
                

    

    def greeting(self):
        GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
        GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
        for word in self.sentence.split():
            if self.greet==True and word.lower() in GREETING_INPUTS:
                self.greet = False
                print(random.choice(GREETING_RESPONSES))
                break

    def possibleDiseases(self):
        ignore_words=['are','is','am','were','i','he','she','it']
        w=nltk.word_tokenize(self.sentence)
        words = [stemmer.stem(i.lower()) for i in w if i.lower() not in ignore_words]
        #print(words)
        li = []

        for i in words:
            for j in self.di:
                if i in self.di[j]:
                    li.append(j)
        #print(li)
        return set(li)
