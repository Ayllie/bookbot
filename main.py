def main():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(word_count(file_contents))
    print(character_count(file_contents))

def word_count(word_string):
    words = word_string.split()
    return len(words)

def character_count(word_string):
    lower_string = word_string.lower()
    character_count = {}
    for i in range(0, len(lower_string)):
        if lower_string[i] in character_count:
            character_count[lower_string[i]] += 1
        else:
            character_count[lower_string[i]] = 1
    return character_count

main()