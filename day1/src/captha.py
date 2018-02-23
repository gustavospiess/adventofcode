def part1():
    with open("data.txt", "r") as data:
      for line in data:
        current = None
        last = None
        first = None
        counter = 0
        for d in line:
            current = int(d)
            if not first:
                first = current
            if last == current:
                counter += current
            last = current
        if first == last:
            counter += last
        print(counter)

def part2():
    pass;