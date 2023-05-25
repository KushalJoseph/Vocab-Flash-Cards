#!/usr/bin/env python3
import random
from datetime import date
from os import get_terminal_size
import yaml

class Htmlfont:
    PARA = '<p>'
    ENDPARA = '</p>'
    WORD = '<span style="color: #c0a000; font-weight: bold; text-decoration: underline;">'
    ENDULINE = '</span>'

# ------------------------------------------------------------------------------------------------------------- #
global words
global words_list
words = {}
words_list = []

def setup():
    global words, words_list
    words = dict(yaml.safe_load(open('./vocab.yaml')))
    words_list = list(words.keys())


def getNextWord():
    global words, words_list

    word = random.choice(words_list)   
    word_dict = words[word]
    
    sentence = word_dict['sentence']
    split_sentence = sentence.split(' ')
    output = f"{Htmlfont.PARA}"
    for item in split_sentence:
        if('(' in word):
            word = word.split('(')[0].strip()
        if(len(word) <= 3 and word in item.lower()):
            output += f"{Htmlfont.WORD}{item}{Htmlfont.ENDULINE} "
        elif(word in item.lower() or word[:-1] in item.lower() or word[:-2] in item.lower()):
            output += f"{Htmlfont.WORD}{item}{Htmlfont.ENDULINE} "
        else:
            output += item + ' '
    output += f"{Htmlfont.ENDPARA}"

    return {
        'word': word_dict['word'],
        'meaning': word_dict['meaning'],
        'sentence': output
    }

def addToWords(word_dict: dict):
    word, meaning, sentence = word_dict['word'], word_dict['meaning'], word_dict['sentence']
    words_list.append(word)
    words[word] = word_dict

    with open('./vocab.yaml', 'w+') as vocab_file:
        yaml.dump(words, vocab_file)


