from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://cat-fact.herokuapp.com/facts/random?amount=1" # 1. Insert API request URL

@app.route('/')
def index():
    # 2. Some APIs need a payload or extra data in the fields, set them up here:
    payload = {}
    
    # 3. Get the API Response in JSON
    cat_fact = requests.get(API_URL, params=payload).json()
    
    # 4. Extract the information for the template
    fact = cat_fact["text"]

    # 5. Return the Template with your data
    return render_template("index.html", fact=fact, image_url="https://cataas.com/cat")

if __name__ == '__main__':
    app.run()