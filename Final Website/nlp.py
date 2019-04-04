import nltk
import random
import string
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()



class NLP:
	def __init__(self):
		self.symptoms=set()
		self.sentence=''
		self.greet=True

	def askFurther(self):
		QUESTIONS=["tell me more about your disease","what has exactly happened to you?","tell me some symptoms of your illness","Tell me more! i will help you","whats wrong with you my friend?"]
		return random.choice(QUESTIONS)


	def greeting(self):
		GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
		GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
		for word in self.sentence.split():
			if self.greet==True and word.lower() in GREETING_INPUTS:
				self.greet = False
				return random.choice(GREETING_RESPONSES)
	


	def processing(self,req):
		self.sentence = req
		if self.greet == True :
			return self.greeting()
		else : 
			return self.askFurther()
