def get_book_text(path_to_file):
    file_contents = ""

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents


def get_num_words(text_file):
    num_words = len(text_file.split())

    print(f"Found {num_words} total words")


def get_num_chars(text_file):
    lower_text_file = text_file.lower()

    char_count = {}

    for char in lower_text_file:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    counts = [{"char": char, "num": count} for char, count in char_count.items()]

    counts.sort(key=lambda item: item["num"], reverse=True)

    for i in counts:
        print(f"{i['char']}: {i['num']}")


