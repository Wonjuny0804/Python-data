from linkedlistFIFO import linkedlistFIFO

class HashTableLL(object):
	def __init__(self, size):
		self.size = size
		self.slots = []
		self._createHashTable()

	def _createHashTable(self):
		for i in range(self.size):
			self.slots.append(linkedlistFIFO())