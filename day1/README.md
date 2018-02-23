### Inverse Captcha
***
#### Intro
This is my [day1 chalenge](http://adventofcode.com/2017/day/1) resolution. The [data.txt](./src/data.txt) file contains the raw input to the given challenge, and [data_test.txt](./src/data_test.txt) contains a raw input to test. If You have not made it out by yourselve yet, I strongly recomend you to try before looking any further throu the fonts.
#### The Fonts
The [captcha.py](./src/captcha.py) contain both, the first and the second part of the chalenge, in a simple way:
```python
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


file = "data.txt"
with open(file, "r") as data:
  for captcha in data:
    part1(captcha)
```
It is simple enouth to do not demand a explanation (as long as you know the chalenge).