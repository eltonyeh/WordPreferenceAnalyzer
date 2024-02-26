import json
from random import sample, shuffle

IMPORTANCE = {
    'A++': 100,
    'A+': 100,
    'A': 80,
    'B': 30,
    'C': 5,
    'D': 0.5,
    'E': 0.1,
    'N': 1
}
SAMPLE_SIZE = 1000
COUNTERS = dict()
TOTAL_ITEM = 0
with open('titles.json', 'r', encoding='utf-8') as file:
    TITLES = json.load(file)


def populate_counters():
    for rating in TITLES:
        count = len(TITLES[rating])
        COUNTERS[rating] = count
        global TOTAL_ITEM
        TOTAL_ITEM += count

    print(COUNTERS)


def sample_items(dest):
    raw_sample_count = 0
    SAMPLES = []
    for rating in COUNTERS:
        raw_sample_count += COUNTERS[rating] * IMPORTANCE[rating]

    for rating in COUNTERS:
        SIZE = int(SAMPLE_SIZE * (COUNTERS[rating] * IMPORTANCE[rating]) / raw_sample_count)
        print(rating, SIZE)
        SAMPLES.extend(sample(TITLES[rating], SIZE))
    shuffle(SAMPLES)
    with open(dest, 'w', encoding='utf-8') as samples:
        json.dump(SAMPLES, samples, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    populate_counters()
    sample_items('samples.json')
