from flask import Flask, render_template, request, redirect, url_for
import os
from histogram import histogram
from dictonary_words import returnSentence
from sample import sample
from random import randint


app = Flask(__name__)

@app.route('/')
def home_route():
    dictonary_words = histogram()
    sentence = ''
    index = 50

    while index > 0:
        sentence += sample(dictonary_words)+" "
        index -= 1


    print(sentence)

    return render_template('index.html', sentence=sentence)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
