from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

#rotta da cancellare
@app.route("/")
def index():
    return "prova" 

if __name__ == "__main__":
    app.run(debug=True)