import json
with open('Dataset.json') as f:
	data = json.load(f)
# print(data)

class Normal:
	def __init__(self):
		self.dis = data
		self.disease = set()

	def findDisease(self,sym):
		tmp = set()
		for i in self.dis:
			if sym in self.dis[i]:
				tmp.add(i)
		return tmp

	def predict(self, symlist):
		for i in symlist:
			k = self.findDisease(i)
			print(k)
			if len((self.disease).intersection(k))==0:
				self.disease = self.disease.union(k)
			else:
				self.disease = self.disease.intersection(k)
		return list(self.disease)
