from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/square", methods=['POST'])
def test():
    data = request.args
    val = data['val']
    return str(int(val)**2)
    
if __name__ == "__main__":
    app.run(debug=True)