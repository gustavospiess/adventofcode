def part1(captcha):
    current = None
    last = None
    first = None
    counter = 0
    for digit in captcha:
        current = int(digit)
        if not first:
            first = current
        if last == current:
            counter += current
        last = current
    if first == last:
        counter += last
    print(counter)

def part2(captcha):
    counter = 0
    for index in range(len(captcha)/2):
        if captcha[index] == captcha[index+len(captcha)/2]:
            counter += 2*int(captcha[index])
    print(counter)


file = "day1/src/data.txt"
with open(file, "r") as data:
  for captcha in data:
    part1(captcha)
    print("-")
    part2(captcha)