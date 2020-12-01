

with open('input.txt', 'r') as f:
    lines = list(map(lambda x: int(x), f.readlines()))

for i in range(0, len(lines)):
    for j in range(0, len(lines)):
        num1 = lines[i]
        num2 = lines[j]
        if num1 + num2 == 2020:
            print(f"{num1} + {num2} = 2020. {num1*num2}")

for i in range(0, len(lines)):
    num1 = lines[i]
    for j in range(0, len(lines)):
        num2 = lines[j]
        for k in range(0, len(lines)):
            num3 = lines[k]
            if num1 + num2 + num3 == 2020:
                print(f"{num1} + {num2} + {num3} = 2020. {num1*num2*num3}")
