import sys
from stats import get_word_count, get_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with status code 1
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    
    print(
        "============ BOOKBOT ============\n"  
        f"Analyzing book found at {file_path}...\n"
        "----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        "--------- Character Count -------\n"
    )
    get_char_count(text)
    

main()