def part1():
    with open("data.txt", "r") as data:
      for line in data:
        current = None
        last = None
        first = None
        counter = 0
        for digit in line:
            current = int(digit)
            if not first:
                first = current
            if last == current:
                counter += current
            last = current
        if first == last:
            counter += last
        print(counter)

def part2():
    with open("data.txt", "r") as data:
      for line in data:
        counter = 0
        for index in range(len(line)/2):
            if line[index] == line[index+len(line)/2]:
                counter += 2*int(line[index])
        print(counter)

part2()