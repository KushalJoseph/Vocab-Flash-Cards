# Vocab-Flash-Cards

A simple CLI-based Python Flash Cards app that helps you practice your vocabulary!
For people who just prefer based CLI rather than a UI

I have tried to make it as beautiful as possible xP.

## How to run
Just clone/download, modify the vocab.txt if you want (see next section), make sure you have python3 installed and run ./script (Note: for Windows, you will need to run "python3 script"

## How to write the vocab.txt file
The script basically parses your vocab file. This way, you can make it completely personalized, write your own "easy" ways to remember words, your own sentences, etc. 
Since we parse the vocab.txt file, it must follow a certain pattern (otherwise there will be an error)

word <hyphen> meaning \n
sentence (IN ONE LINE)
<space>
word <hyphen> meaning \n
sentence (IN ONE LINE)
<space>
  
See the vocab.txt file for example, or just use that itself! There are currently ~500 words there already
  
## Instructions
- Press "Return" or "n" for the next word
- Press "m" to see the meaning
- Press "s" to see a sentence
- Press "b" to go back to the previous word (in case you skipped by mistake)
- Press "q" to quit
