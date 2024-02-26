import json

DATABASE = []

DATA_FILE = 'zhwiki-latest-all-titles.txt'
DATA_DEST = 'titles.json'


def read_file(file_name):
    count = 0
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            if count % 1000 == 0:
                print(count)
            count += 1
            if count == 1:  # avoiding the first line
                continue
            data = line.split("	")
            namespace = int(data[0])
            if namespace == 0:
                title = '	'.join(data[1:]).strip()
                DATABASE.append(title)

    return DATABASE


def write_file(dest, content):
    with open(dest, 'w', encoding='utf-8') as file:
        json.dump(content, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    write_file(DATA_DEST, read_file(DATA_FILE))
