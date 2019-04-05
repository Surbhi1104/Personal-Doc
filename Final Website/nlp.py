import nltk
import random
import string
from nn import NN
#from jd import Normal
import json
with open('Dataset.json') as f:
	data = json.load(f)



k=NN()
# n = Normal()
class NLP:
	def __init__(self):
		self.disease=set()
		self.symptoms=set()
		self.sentence=''
		self.greet = True
		self.status = 1
		self.dis = data
		self.greeting_input = ("hello", "hi", "greetings", "sup", "what's up","hey",)
		self.greeting_response = ["hi", "hey", "*nods*", "hi there", "hello"]
		self.newquestions=["what has exactly happened to you?","I am glad! You are talking to me","whats wrong with you my friend?"]
		self.repeatquestions = ["tell me more about your disease","tell me some symptoms of your illness","Tell me more! i will help you"]
		self.ignore_words=['are','is','am','were','i','he','she','it','you','your','yours','we','they','them','me','mine','hers','her','him','his']




	def verifyGreeting(self):
		for word in self.sentence.split():
			if  word.lower() in self.greeting_input:
				#self.greet = False
				return True
		return False



	def verifySymptoms(self):
		symlist = k.getSymptoms()
		if 'pain chest' in symlist:
			print('yeah')
		tmp = set()
		flag = False
		for word in self.sentence.split():
			#print(word)
			#print(word)
			if word not in self.ignore_words:
				for sm in symlist:
					if word in sm:
						#print(tmp)
						tmp.add(sm)
						flag = True

		for i in symlist:
			if i in self.sentence:
				if i not in tmp:
					tmp.add(i)
				flag = True
		print(tmp)
		# for i in tmp:
		# 	self.symptoms.add(i)
		for i in tmp:
			self.symptoms.add(i)
			dise = self.findDisease(i)
			# print(dise)
			if len((self.disease).intersection(dise))==0:
				self.disease = self.disease.union(dise)
			else:
				self.disease = self.disease.intersection(dise)
			# print(self.disease)

		return flag


	# def predict(self):
	# 	return n.predict(list(self.symptoms))

	def findDisease(self,sym):
		tmp = set()
		for i in self.dis:
			if sym in self.dis[i]:
				tmp.add(i)
		return tmp



	def refresh(self):
		self.greet  = True
		self.disease = set()
		self.symptoms = set()
		self.status = 1

	def changeStatus(self,status):
		self.status=status

	def getStatus(self):
		return self.status









	def processing(self,req):
		self.sentence = req
		self.sentence  = self.sentence.lower()
		# if self.sentence == 'thank you':
		# 	k= self.predict()
		# 	if len(k)==0:
		# 		return (1,"Sorry unable to detect your problem")
		# 	if len(k)==1:
		# 		return (1,"You are suffering from "+','.join(k))
		# 	else:
		# 		return (1,"You may suffer from one of these diseases - "+','.join(k))
		print(self.sentence)
		if 'disease' in self.sentence:

			return (1,"You may suffer from one of these diseases - "+','.join(self.disease)+'<br>'+random.choice(self.repeatquestions))


		if self.verifyGreeting() and self.greet:
			self.greet = False
			return (0,random.choice(self.greeting_response))
		k = self.verifySymptoms()
		if len(self.disease)==1:
			k=self.disease
			self.refresh()
			return (1,'You are suffering from '+','.join(k))


		elif k:
			return (0,random.choice(self.repeatquestions))
		else:
			return (0,random.choice(self.newquestions))
