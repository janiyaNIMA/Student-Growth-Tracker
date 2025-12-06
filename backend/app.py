from flask import Flask, render_template
import mysql.connector
import os

# Templates live in the frontend/ directory
HERE = os.path.dirname(__file__)
template_dir = os.path.abspath(os.path.join(HERE, '..', 'frontend'))
static_dir = os.path.abspath(os.path.join(HERE, '..', 'frontend', 'static'))

app.con

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)



