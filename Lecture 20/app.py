from flask import Flask, templating, request, jsonify
import pickle

app = Flask(__name__)

with open('cv.pickle', 'rb') as f:
    m1 = pickle.load(f)

with open('nb.pickle', 'rb') as f:
    m2 = pickle.load(f)


@app.route('/')
def home():
    return templating.render_template('index.html')


@app.route('/submit/', methods=['POST'])
def submit():
    form = request.form
    data = m1.transform([form['message']])
    res = m2.predict(data)[0]
    if res == 'ham':
        return templating.render_template('result.html', url='Ham')
    else:
        return templating.render_template('result.html', url='Spam')


if __name__ == '__main__':
    app.run(debug=True, port=3005)
