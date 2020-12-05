import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

field_re = {
    'byr': r'\d{4}',
    'iyr': r'\d{4}',
    'eyr': r'\d{4}',
    'hgt': r'\d+(cm|in)',
    'hcl': r'#[0-9a-f]{6}',
    'ecl': r'(amb|blu|brn|gry|grn|hzl|oth)',
    'pid': r'\d{9}'
}

field_validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: hgt_validator(x),
}


def hgt_validator(input):
    # print(input)
    if input.endswith('cm'):
        a = int(input.rstrip('cm'))
        return 150 <= a <= 193
    if input.endswith('in'):
        a = int(input.rstrip('in'))
        return 59 <= a <= 76

def check(input):
    fields = {}
    for field in input.split(' '):
        parts = field.split(':')
        fields[parts[0]] = parts[1]
    for f in required_fields:
        if f not in fields.keys():
            return False
        v = fields[f]
        # Validate field
        if re.search(field_re[f], v) is None:
            print(f"{input} failed regex {field_re[f]}")
            return False
        l = field_validators.get(f, None)
        if f in field_validators.keys() and not l(v):
            print(f"{input} {f}: failed validator")
            return False
    return True
        

with open ('input.txt', 'r') as f:
    buff = ""
    valid = 0
    for line in f.readlines():
        buff += " " +line.strip()
        if line == '\n':
            buff = buff.strip()
            if check(buff):
                valid += 1
            buff = ""
    if check(buff.strip()):
        valid += 1
    print(valid)
