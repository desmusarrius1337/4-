import json
def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    summmm = sum(item['score'] * item['weight'] for item in data)
    return round(summmm, 3)

print(task())
