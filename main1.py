from stats import *
import sys

def main():
    argument_check = sys.argv

    if len(argument_check) == 2:
        target_file = get_book_text(sys.argv[1])

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")

        print("----------- Word Count ----------")
        get_num_words(target_file)

        print("--------- Character Count -------")
        get_num_chars(target_file)
        
    else:
        print('Usage: python3 main.py <path_to_book>')

    
main()
