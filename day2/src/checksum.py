def part1(file):
    count = 0
    with open(file, "r") as data:
      for row in data:
        numbers = [int(value) 
            for value in row.replace("\n", "").split("\t")]
        count += max(numbers) - min(numbers)
    print(count)

def part2(file):
    count = 0
    with open(file, "r") as data:
      for row in data:
        numbers = [int(value) 
            for value in row.replace("\n", "").split("\t")]
        combination = [(x, y) 
            for x in range(len(numbers)) 
                for y in range(len(numbers)) if x != y]
      	divs = [numbers[c[0]]/numbers[c[1]]
          for c in combination if not (numbers[c[0]]%numbers[c[1]])]
      	count += sum(divs)
      print(count)

file = "day2/src/data.txt"
part1(file)
print("-")
part2(file)