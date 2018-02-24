def part1(file):
    count = 0
    with open(file, "r") as data:
      for row in data:
        numbers = [int(value.replace("\n", "")) for value in row.split("\t")]
        count += max(numbers) - min(numbers)
    print(count)

def part2(file):
    pass

file = "data.txt"
part1(file)
print("-")
part2(file)
