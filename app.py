from flask import Flask, render_template, request, redirect, url_for
import os
from histogram import Histogram
from dictonary_words import returnSentence
from sample import sample
from random import randint


app = Flask(__name__)

def get_sentence(count=50):
    dictonary_words = Histogram.histogram()
    sentence = ''
    navBar_message = ''

    while count > 0:
        sentence += sample(dictonary_words)+" "
        if count < 10:
            navBar_message += sample(dictonary_words)+" "

        count -= 1

    return [sentence, navBar_message]

def check_number(num):
    try:
        count = int(num)
        return count
    except ValueError as verr:
        print("Invalid number enter a number")
        return False
    except Exception as ex:
        print(ex)
        return False



# home page
@app.route('/')
def home_route():
    tweet = get_sentence(50)
    print(tweet[0])
    return render_template('index.html', tweet=tweet[0], navBar_message=tweet[1])


# get # of words in a tweets 
@app.route('/limit/<num>')
def limit_words_route(num):
    count = check_number(num)
    tweet = get_sentence(count)
    return render_template('index.html', tweet=tweet[0], navBar_message=tweet[1])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
