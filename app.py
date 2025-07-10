from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    input_text = data['text']
    result = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
    return jsonify({'summary': result[0]['summary_text']})

if __name__ == '__main__':
    app.run(debug=True)
