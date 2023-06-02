from os import get_terminal_size
welcome = "Welcome to GRE Custom Vocab flashcards console application. " + "How to use:"
preGuide = "See the README.md file on how to format your vocab file. \nName it vocab.txt, and keep it in the same directory as this script. Run 'python3 script'"
modeOption = "Press any key to practice regular words, \n'f' to practice forgotten words\n'a' to practice advanced words\n"
guide = "You will be shown a word, \n - Press m for meaning, \n - s for sentence, \n - f if you forgot the word, and want to add to 'forgotten' list\n - Return or n for next word, \n - b to go back to the previous word (only one step back), \n - q to quit"
recent_words_option = 'Press l or r to practice your recent words, or any other key to practice all words\n'
separator = '-' * int(get_terminal_size().columns)
no_sentence = "You have not added a sentence for this"
invalid_help = 'M for meaning, S for sentence, N for next word, Q to quit'
no_forgotten_words = "You have not added any 'forgotten words'.\n Switching to regular mode"
add_to_forgotten = "Added this word to your forgotten list\n"
already_in_f_mode = "You are already in forgotten mode. You cannot press f here\n"