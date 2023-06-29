from flask import Flask, jsonify, request
from flask_cors import CORS
import yaml
import random
app = Flask(__name__)
CORS(app)

@app.route('/nextWord', methods=['GET'])
def get_next_word():
    # Your logic to generate the next word goes here
    next_word = getNextWord()
    print(next_word)
    return jsonify({'next_word': next_word})

@app.route('/addWord', methods=['POST'])
def add_word():
    data = request.get_json()
    try:
        addToWords(data)
        return jsonify({'message': 'Word added successfully'})
    except:
        return jsonify({'error': 'Something went wrong. Could not add word. '}), 400

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

if __name__ == '__main__':
    setup()
    print("Setup Done")
    app.run(host='0.0.0.0', port=5000)