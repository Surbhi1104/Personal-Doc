import pandas as pd
import pickle as pi
import numpy as np

data = pd.read_excel('Dataset3.xlsx')
sym = data.columns.tolist()[1:]
dis = data['Start'].tolist()

#print(dis)

class NN:
	def __init__(self):
		self.diseases=[]
		self.symptoms=[]
		self.input = []
		self.model=None
		self.output = ''

	def setDiseases(self):
		self.diseases = dis

	def setSymptoms(self):
		self.symptoms = sym

	def getDiseases(self):
		self.setDiseases()
		return self.diseases

	def getSymptoms(self):
		self.setSymptoms()
		return self.symptoms

	
	def generateInput(self,symlist):
		tmp=[]
		print(symlist)
		for i in symlist:
			tmp.append(self.symptoms.index(i))
		#print(tmp)
		inp = [0]*len(self.symptoms)
		for i in tmp:
			inp[i]=1

		self.input.append(inp)
		print(self.input)

	def loadModel(self):
		self.model = pi.load(open('clf.pickle','rb'))

	def predictDisease(self):
		self.loadModel()
		index = self.model.predict(self.input)
		return self.diseases[index[0]]






# k = NN()
# k.setDiseases()
# k.setSymptoms()
# k.generateInput(['cough'])
# k.loadModel()
# disease=k.predictDisease()
# print(disease)
