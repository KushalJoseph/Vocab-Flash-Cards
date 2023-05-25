from flask import Flask, jsonify, request
from flask_cors import CORS
from backend import setup, getNextWord, addToWords
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

if __name__ == '__main__':
    setup()
    print("Setup Done")
    app.run(debug=True)