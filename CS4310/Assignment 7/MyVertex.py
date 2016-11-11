class MyVertex:
	counter = 0 

	def __init__(self, label=None, value=None):
		self.label = label
		self.value = value
		self.uid = MyVertex.counter 
		self.degree = 0
		MyVertex.counter = MyVertex.counter + 1

		# Edges that belong to this vertex.
		self.Ei = {} # Incoming
		self.Eo = {} # Outgoing

		# Incident edges list
		self.iedges = []

	def getUid(self):
		return self.uid

	def getLabel(self):
		return self.label

	def getValue(self):
		return self.value

	def add_incoming_edge(self, edge):
		self.Ei[edge.getUid()] = edge

	def add_outgoing_edge(self, edge):
		self.Eo[edge.getUid()] = edge

	def remove_edge(self, edge):
		del self.Ei[edge.getUid()]
		del self.Eo[edge.getUid()]

	def add_incident_edge(self, edge):
		self.iedges.append(edge)
