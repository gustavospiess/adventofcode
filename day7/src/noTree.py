class Node():
  def __init__(self, name, sons, weight, father = None):
    self.name = name
    self.sons = sons
    self.weight = weight
    self.father = father
    self.totalWeight = None

  @staticmethod
  def nodeFromLine(line):
    split = line.rstrip().split(" ")
    name = split.pop(0)
    sons = [son.split(",")[0] for son in split[2:]]
    weight = int(split.pop(0)[1:-1])
    return Node(name, sons, weight)

  def __str__(self):
    return self.name + '(' + str(self.weight) + ')'


def getPull():
  pull = list()

  with open("day7/src/data.txt", "r") as data:
    for line in data:
      pull.append(Node.nodeFromLine(line))

  return pull


def sonsLenKey(node):
  return len(node.sons)

def part1():
  pull = getPull()
  control = 100
  while len(pull) > 1 and control:
    control = control - 1
    pull.sort(key = sonsLenKey)

    removeSet = set()

    for fnode in pull:
      for snode in pull:
        if (snode == fnode):
          break
        if (fnode.name in snode.sons):
          removeSet.add(fnode)
        if (snode.name in fnode.sons):
          removeSet.add(snode)

    for node in removeSet:
      pull.pop(pull.index(node))

  if (len(pull) == 1):
    return pull[0]

def part2():
  first = part1()
  pull = getPull()

  def calcTotal(node):
    node.totalWeight = node.weight
    for sub in pull:
      if sub.name in node.sons:
        a = str(sub)
        calcTotal(sub)
        node.totalWeight += sub.totalWeight

  calcTotal(first)

  for i in range(len(pull)):
    if (pull[i].name == first.name):
      pull[i] = first

  def calcDiference(node):
    message = ""
    sons = [son for son in pull if son.name in node.sons]
    balance = [fnode.totalWeight 
                for fnode in sons 
                  for snode in sons 
                    if  fnode != snode and 
                        fnode.totalWeight == snode.totalWeight]
    if not balance:
      return None
    else:
      balance = balance[0]
    diferenceNodes = [node for node in sons if node.totalWeight != balance]

    if (diferenceNodes):
      for diffNode in diferenceNodes:
        correctValue = diffNode.weight - (diffNode.totalWeight - balance)
        if (correctValue):
          if (message):
            message = message + "\n\n"
          message = ("the wrong node is: " + str(diferenceNodes[0]) + 
            "\nthe correct value is: " + str(correctValue))

    for son in sons:
      sonMessage = calcDiference(son)
      if sonMessage:
        return sonMessage

    return message


  print(calcDiference(first))

print("The head node is " + str(part1()))
part2()