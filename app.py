from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json
from urllib.parse import quote_plus

app = Flask(__name__)

# MongoDB Atlas connection
username = quote_plus("aditya")
password = quote_plus("Aditya@6398")
client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.qwqqxw5.mongodb.net/?appName=Cluster0")

db = client['flaskdb']
collection = db['aditya']

# 1️⃣ API route to return data from file
@app.route('/api')
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

# 2️⃣ Form routes
@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        data = {"name": name, "email": email}
        collection.insert_one(data)
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
