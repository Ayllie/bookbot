def main():
    file_contents = None
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(word_count(file_contents), character_count(file_contents))

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

def sort_on(dict):
    return dict[1]

def print_report(number_words, count_of_characters):
    list_of_character_dicts = list(count_of_characters.items())
    list_only_alpha = []
    for entry in list_of_character_dicts:
        if entry[0].isalpha():
            list_only_alpha.append(entry)
    list_only_alpha.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_words} words found in the document")
    print(" ")
    for entry in list_only_alpha:
        print(f"The '{entry[0]}' character was found {entry[1]} times")
    print("--- End report ---")


main()