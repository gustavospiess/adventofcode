# AdventOfCode
### Recursive Circus
#### Intro
This is my [day7 chalenge](http://adventofcode.com/2017/day/7) repo. The [data.txt](https://github.com/gustavospiess/adventofcode/blob/master/src/data.txt) file contains the raw input to the given challenge. If You have not made it out by yourselve yet, I strongly recomend you to try before looking any further throu the fonts.
#### The Fonts
The [tree.py](https://github.com/gustavospiess/adventofcode/blob/master/src/tree.py) file contains the completeness of the classes and methods used to solve the shown problems:



```python
class Node():
    def __init__(self, name, sons, weight, father = None):
        ...

    @staticmethod
    def nodeFromLine(line):
        ...
        
    def __str__(self):
        ...
    
class NodeTree():
    def __init__(self):
  	    ...

    def printTree(self, simply = 0):
  	    ...

    def totalWeight(self, node):
  	    ...

    def allNodes(self, condition = None):
  	    ...

    def append(self, newNode):
  	    ...

pull = NodeTree()

with open("data.txt", "r") as data:
    for line in data:
        pull.append(Node.nodeFromLine(line))

pull.printTree(simply = 1)

```

When printed as ```pull.printTree(simply = 1)```, the tree show in the log:
```
a(1)(19)
    b(6)(6)
    c(2)(6)
        d(4)(4)
    e(0)(6)
        f(2)(3)
            h(1)(1)
        g(1)(3)
            i(1)(1)
            j(1)(1)
```
When ```pull.printTree(simply = 0)``` or ```pull.printTree()``` the tree show in the log:
```
\---a(1)(19)
    +---b(6)(6)
    +---c(2)(6)
    |   \---d(4)(4)
    \---e(0)(6)
        +---f(2)(3)
        |   \---h(1)(1)
        \---g(1)(3)
            +---i(1)(1)
            \---j(1)(1)
```
Of course, those tress are not imported from [data.txt](https://github.com/gustavospiess/adventofcode/blob/master/src/data.txt) but from [data_test.txt](https://github.com/gustavospiess/adventofcode/blob/master/src/data_test.txt). With that trees it's visible what is the first node, and with some effort, what node has the wrong weight, and calculate what'd be the correct weight.
#### The Answers
 - Whats the first node? 
   - It's ```rqwgj```.
 - What node has the wrong weight, and what'd be the correct one?
   - It's ```aobgmc```, its weight is ```341``` but should be ```333```.