"""
app.py is the file representing the dashboard application

@author     Daphne Marie Tapia
@version    1.0
@since      11/5/2019
"""

from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)