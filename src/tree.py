class Node():
	def __init__(self, name, sons, weight, father = None):
		self.name = name
		self.sons = sons
		self.weight = weight
		self.father = father

	@staticmethod
	def nodeFromLine(line):
		split = line.rstrip().split(" ")
		name = split.pop(0)
		sons = [son.split(",")[0] for son in split[2:]]
		weight = int(split.pop(0)[1:-1])
		return Node(name, sons, weight)

class NodePull():
	def __init__(self):
		self.headPull = []

	def allNodes(self, condition = None):
		nodes = []
		def subNodes(node):
			subs = [node]
			if type(node) != str:
				for sub in node.sons:
					subs += subNodes(sub)
			return subs


		for headNode in self.headPull:
			nodes += subNodes(headNode)

		if condition:
			return [node for node in nodes if condition(node)]
		else:
			return nodes

	def append(self, newNode):
		removeList = []
		for headNodeIndex in range(len(self.headPull)):
			headNode = self.headPull[headNodeIndex]
			for sonIndex in range(len(newNode.sons)):
				son = newNode.sons[sonIndex]
				if son == headNode.name:
					newNode.sons[sonIndex] = headNode
					headNode.father = newNode
					removeList.append(headNode)
		for node in removeList:
			self.headPull.remove(node)
		for sub in self.allNodes(lambda x: type(x) == str or x.sons and [y for y in x.sons if type(y) == str]):
			if type(sub) == str:
				if son == newNode.name:
					sub.sons[sonIndex] = newNode
					newNode.father = sub
			else:
				for sonIndex in range(len(sub.sons)):
					son = sub.sons[sonIndex]
					if son == newNode.name:
						sub.sons[sonIndex] = newNode
						newNode.father = sub
						break
				if newNode.father:
					break
		if not newNode.father:
			self.headPull.append(newNode)
		
pull = NodePull()

with open("data.txt", "r") as data:
	for line in data:
		pull.append(Node.nodeFromLine(line))

def p(node, indent):
	if type(node) == str:
		print(indent + node + "(str)")
		return
	print(indent + node.name)
	for son in node.sons:
		p(son, indent + "	")

for node in pull.headPull:
	p(node, "")