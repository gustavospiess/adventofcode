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

  def __str__(self):
    return self.name + '(' + str(self.weight) + ')'

class NodeTree():
  def __init__(self):
    self.headPull = []

  def printTree(self, simply = 0):
    def p(node, indent = "", last = 1, head = 1, simply = 0):
      prefix = "" if simply else ("\---" if last or head else "+---")
      print(indent + prefix + str(node) + '(' + str(self.totalWeight(node)) + ')')
      indent += "    " if simply or last else "|   "
      for son in node.sons:
        p(son, simply = simply, indent = indent, last = (son == node.sons[-1]), head = 0)

    for node in pull.headPull:
      p(node, simply = simply)

  def totalWeight(self, node):
    weight = node.weight
    for son in node.sons:
      weight += self.totalWeight(son)
    return weight

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
    
pull = NodeTree()

with open("day7/src/data.txt", "r") as data:
  for line in data:
    pull.append(Node.nodeFromLine(line))

pull.printTree(simply = 1)