from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from flask import Flask , render_template , request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get', methods=["POST","GET"])
def chat():
    text = request.form["msg"]
    return get_response(text)


def get_response(text):

    API_TOKEN = "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"
    API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    response = requests.post(API_URL, headers=headers, json=text)
    return response["generated_text"]
        




if __name__ == "__main__":
    app.run(debug = True)
