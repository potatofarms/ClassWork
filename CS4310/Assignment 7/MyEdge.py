#Date: 11/11/2016
#Class: CS4310
#Assignment: Assignment 7
#Author(s): Alex Dekau

class MyEdge:
	counter = 0 

	def __init__(self, label=None, value=None, directed=False):
		self.label 	= label
		self.value 	= value
		self.directed	= directed
		self.uid 	= MyEdge.counter 
		self.v1 	= None  		#edges always go v1 to v2 if directed
		self.v2 	= None
		MyEdge.counter 	= MyEdge.counter + 1

	def getUid(self):
		return self.uid

	def getLabel(self):
		return self.label

	def getValue(self):
		return self.value

	def is_directed(self):
		return self.directed == True

	def getVertex1(self):
		return self.v1
	
	def getVertex2(self):
		return self.v2

	def setVertex1(self, vtx):
		self.v1 = vtx

	def setVertex2(self, vtx):
		self.v2 = vtx

	def end_vertices(self):
		return [self.v1, self.v2]
