data = []

with open('names.txt', 'r', encoding='utf-8') as f:

    while '' not in data:
        data.append(f.readline().rstrip('\n'))

    data.remove('')


print(data)
