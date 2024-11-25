def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report(word_count(file_contents), char_count(file_contents))

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowered_text = text.lower()
    response = {}
    for char in lowered_text:
        if char.isalpha():
            if char not in response:
                response[char] = 1
            else:
                response[char] += 1
    return response

def report(word_count, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    print("")
    for key, value in chars.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

main()