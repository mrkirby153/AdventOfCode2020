
with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))

valid = 0
valid_2 = 0

for line in lines:
    parts = line.split(':')
    (requirements, letter) = parts[0].split(' ')
    password = parts[1].strip()
    (min_letters, max_letters) = requirements.split('-')
    min_letters = int(min_letters)
    max_letters = int(max_letters)

    cnt = 0
    for l in password:
        if l == letter:
            cnt += 1
    
    if cnt >= int(min_letters) and cnt <= int(max_letters):
        valid += 1

    print(f"Checking {password}")
    if password[min_letters-1] != letter:
        print(f"Position {min_letters-1} is not {letter}")
        # The 2nd character must be equal
        if password[max_letters-1] == letter:
            valid_2 += 1
            print(f"{password} is valid")
        else:
            print(f"{password} is not valid")
    else:
        print(f"Position {min_letters-1} is {letter}")
        # The 2nd character must not be equal
        if password[max_letters-1] != letter:
            valid_2 += 1
            print(f"{password} is valid")
        else:
            print(f"{password} is not valid")


print(f"Part 1: There are {valid} valid passwords")
print(f"Part 2: There are {valid_2} valid passwords")
