def NumberOfWords(book):
    word_list = book.split()
    return len(word_list)

def UniqueCharacters(book):
    character_dict = {}
    word_list = book.split()
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    for word in word_list:
        for character in word:
            letter = character.lower()
            if letter in ALPHABET:
                if letter not in character_dict:
                    character_dict[letter] = 1
                else:
                    character_dict[letter] += 1
    return character_dict

def main():
    total = 0
    book_string = ""
    with open("books/frankenstein.txt", 'r') as f:
        book_string = f.read()
    
    num_words = NumberOfWords(book_string)
    unique_characters = UniqueCharacters(book_string)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")
    
    for entry in unique_characters:
        print(f"The {entry} character was found {unique_characters[entry]} times")

main()