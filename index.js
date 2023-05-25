function handleMeaningClick() {
    let m_s_TextBox = document.getElementById('m-s-text');
    if(current_word != null){
        if(current_word.meaning == null)
            m_s_TextBox.innerHTML = "No sentence provided";
        else
            m_s_TextBox.innerHTML = current_word.meaning
    }
}

function handleSentenceClick() {
    let m_s_TextBox = document.getElementById('m-s-text');
    if(current_word != null){
        if(current_word.sentence == null)
            m_s_TextBox.innerHTML = "No sentence provided";
        else
            m_s_TextBox.innerHTML = current_word.sentence
    }
}

function isEmptyObject(obj){
    if (Object.keys(obj).length === 0) {
        return true;
    } else {
        return false;
    }
}

function handleBackClick() {
    if(!isEmptyObject(previous_word)){
        current_word = previous_word;
        renderWord();
    }
}

function handleNextClick() {
    fetchNextWord();
}

function renderWord() {
    let wordTextBox = document.getElementById('word-text');
    let m_s_TextBox = document.getElementById('m-s-text');
    wordTextBox.innerHTML = current_word.word
    m_s_TextBox.innerHTML = "";
}

let current_word = {};
let previous_word = {};

function fetchNextWord() {
    if(!isEmptyObject(current_word)){
        previous_word = current_word
    }
    let wordTextBox = document.getElementById('word-text');
    let m_s_TextBox = document.getElementById('m-s-text');
    wordTextBox.innerHTML = "";
    m_s_TextBox.innerHTML = "";

    axios.get('http://127.0.0.1:5000/nextWord')
        .then(response => {
            current_word = response.data.next_word;
            renderWord();
        })
        .catch(error => {
            console.error('Error:', error.message);
            m_s_TextBox.innerHTML = 'Could not connect to server!'
        });
}

async function handleAddWord() {
    var word = document.getElementById('word-input').value
    var meaning = document.getElementById('meaning-input').value
    var sentence = document.getElementById('sentence-input').value

    if(word.trim() === '') {
        alert('Word is empty. Please enter a word.');
        return;
    }
    if(meaning.trim() === '') {
        alert('Meaning is empty. Please enter a meaning.');
        return;
    }

    try {
        const response = await axios.post('http://127.0.0.1:5000/addWord', {
            word: word,
            meaning: meaning,
            sentence: sentence
        });
        let data = response.data;
        if (data.hasOwnProperty("message")) {
            alert(data.message);
        } else if (data.hasOwnProperty("error")) {
            alert(data.error);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

document.addEventListener('keydown', event => {
    if(event.key === 'Enter' || event.key === 'N' || event.key === 'n') {
        fetchNextWord(); 
    }else if(event.key === 'S' || event.key === 's'){
        handleSentenceClick();
    }else if(event.key === 'M' || event.key === 'm'){
        handleMeaningClick();
    }else if(event.key === 'B' || event.key === 'b'){
        handleBackClick();
    }
});
  
document.addEventListener('DOMContentLoaded', function() {
    if(window.location.href.includes("practice")) {
        var nextWord = document.getElementById("next-button");
        nextWord.addEventListener("click", handleNextClick);

        var back = document.getElementById("back-button");
        back.addEventListener("click", handleBackClick);
        
        var meaning = document.getElementById("meaning-button");
        meaning.addEventListener("click", handleMeaningClick);

        var sentence = document.getElementById("sentence-button");
        sentence.addEventListener("click", handleSentenceClick);

        fetchNextWord(); 
    }
    if(window.location.href.includes("add-word")){
        var addWord = document.getElementById("button-add-word");
        addWord.addEventListener("click", handleAddWord);
    }
});