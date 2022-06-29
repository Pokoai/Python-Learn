import json

numbers = [12, 3, 54, 65, 4, 7]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    num_in = json.load(f_obj)
    print(num_in)
