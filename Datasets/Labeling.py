import json
import chinese_converter

SOURCE = 'samples.json'
TARGET = 'labels.json'


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    with open(SOURCE, 'r', encoding='utf-8') as source_file, open(TARGET, 'r', encoding='utf-8') as target_file:
        data = json.load(source_file)
        labels = json.load(target_file)

    if labels:
        titles = list(map(lambda x: x['title'], labels))
    else:
        titles = []

    print("Rate titles by a number between 0 and 1. The larger the score is, the more familiar you are with the topic. "
          "Input any other string to exit.")

    for sample in data:
        if sample in titles:
            continue
        response = input(f'{chinese_converter.to_traditional(sample)}：')
        if is_float(response.strip()) and 0 <= float(response) <= 1:
            new_label = {'title': sample, 'score': float(response)}
            labels.append(new_label)
        else:
            print(f"Exit. There are {len(labels)} labelled titles now.")
            break

    with open(TARGET, 'w', encoding='utf-8') as target_file:
        json.dump(labels, target_file, ensure_ascii=False, indent=4)
