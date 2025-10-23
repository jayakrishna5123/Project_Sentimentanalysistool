from flask import Flask, request, render_template
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    result = analyze_sentiment(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
